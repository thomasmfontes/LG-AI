from typing import Dict, Optional
from config import Config
from .data_loader import DataLoader
from .utils import normalize_campo, ValidationError, sanitize_input
from .logger import setup_logger

logger = setup_logger(__name__)


class Validator:
    """Valida campos de acordo com rede e canal"""
    
    def __init__(self, data_loader: DataLoader):
        self.data_loader = data_loader
    
    def validar_campo(self, rede: str, campo: str) -> Dict[str, any]:
        """
        Valida campo de acordo com rede e canal.
        
        Args:
            rede: Nome da rede
            campo: Nome do campo
        
        Returns:
            Dicionário com resultado da validação:
            {
                'status': 'obrigatorio' | 'opcional' | 'branco',
                'campo_formatado': str,
                'rede': str,
                'canal': str,
                'status_texto': str,
                'formato': str | None
            }
        
        Raises:
            ValidationError: Se rede ou campo inválidos
        """
        # Sanitização
        try:
            rede = sanitize_input(rede, max_length=100)
            campo = sanitize_input(campo, max_length=100)
        except ValidationError as e:
            logger.warning(f"Input inválido: {e}")
            raise
        
        if not rede or not campo:
            raise ValidationError("Rede e campo são obrigatórios")
        
        logger.info(f"Validando campo '{campo}' para rede '{rede}'")
        
        # Normalização
        campo_formatado = campo.strip().upper()
        campo_norm = normalize_campo(campo)
        
        # Obter canal
        canal = self.data_loader.get_canal_for_rede(rede.strip())
        
        if not canal:
            raise ValidationError(f"Canal não encontrado para a rede {rede}")
        
        if canal not in self.data_loader.df_campos.columns:
            raise ValidationError(f"Canal '{canal}' não existe na planilha de campos")
        
        # Buscar campo na tabela
        linha = self.data_loader.df_campos[
            self.data_loader.df_campos['CAMPO_NORMALIZADO'] == campo_norm
        ]
        
        if linha.empty:
            logger.warning(f"Campo '{campo}' não encontrado na tabela")
            raise ValidationError(f"Campo '{campo_formatado}' não encontrado na tabela de obrigatoriedade")
        
        # Obter valor
        valor = linha.iloc[0][canal]
        
        # Determinar status
        if valor == '✓':
            status = 'obrigatorio'
            status_texto = f"O campo {campo_formatado} é OBRIGATÓRIO para a rede {rede} (Canal: {canal})."
        elif valor == '✗':
            status = 'branco'
            status_texto = f"O campo {campo_formatado} deve ficar em branco para a rede {rede} (Canal: {canal})."
        else:
            status = 'opcional'
            status_texto = f"O campo {campo_formatado} é opcional para a rede {rede} (Canal: {canal})."
        
        # Buscar formato/comentário
        formato = self._get_formato(campo_norm)
        
        logger.info(f"Validação concluída: {status}")
        
        return {
            'status': status,
            'campo_formatado': campo_formatado,
            'rede': rede,
            'canal': canal,
            'status_texto': status_texto,
            'formato': formato
        }
    
    def _get_formato(self, campo_norm: str) -> Optional[str]:
        """
        Obtém formato/comentário para um campo.
        
        Args:
            campo_norm: Campo normalizado
        
        Returns:
            Texto do comentário ou None
        """
        # Aplicar sinônimos
        campo_para_comentario = Config.SINONIMOS_COMENTARIOS.get(
            campo_norm, 
            campo_norm
        )
        
        # Buscar comentário
        campo_real = next(
            (c for c in self.data_loader.comentarios.keys()
             if c.replace("__", "_") == campo_para_comentario),
            campo_para_comentario
        )
        
        return self.data_loader.comentarios.get(campo_real)
