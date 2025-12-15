from typing import Dict
from config import Config


class ResponseFormatter:
    """Formata respostas para exibição na interface"""
    
    @staticmethod
    def format_response(resultado: Dict[str, any]) -> str:
        """
        Formata resultado da validação em HTML.
        
        Args:
            resultado: Dicionário com resultado da validação
        
        Returns:
            HTML formatado
        """
        status = resultado['status']
        campo_formatado = resultado['campo_formatado']
        rede = resultado['rede']
        canal = resultado['canal']
        status_texto = resultado['status_texto']
        formato = resultado['formato']
        
        # Status HTML com cores
        if status == 'obrigatorio':
            status_html = "<span style='color:#ff4d4d'><b>Obrigatório 🔴</b></span>"
        elif status == 'branco':
            status_html = "<span style='color:#aaa'><b>Deve ficar em branco ⚪</b></span>"
        else:
            status_html = "<span style='color:#00cc66'><b>Opcional 🟢</b></span>"
        
        # Formato
        if formato:
            formato_humano = f"Padrão de preenchimento: {formato}"
        else:
            formato_humano = (
                "Este campo não possui orientações específicas de preenchimento no modelo atual. "
                f"Você pode consultar o <a href='{Config.MANUAL_URL}' "
                "target='_blank' style='color:#4EA1FF'>manual oficial</a> para mais informações."
            )
        
        return f"""
        <div class='resposta-ia'>
            <b>📊 Resultado da verificação:</b><br>
            <b>🏷️ Campo:</b> {campo_formatado}<br>
            <b>🏢 Rede:</b> {rede}<br>
            <b>🧭 Canal:</b> {canal}<br>
            <b>🔒 Status:</b> {status_html}<br>
            <div class='resposta-bloco' style='margin-top:15px'>💬 <i>{status_texto}</i></div>
            <div class='resposta-bloco' style='margin-top:15px'>📝 <b>{formato_humano}</b></div>
        </div>
        """
    
    @staticmethod
    def format_error(error_message: str) -> str:
        """
        Formata mensagem de erro.
        
        Args:
            error_message: Mensagem de erro
        
        Returns:
            HTML formatado
        """
        return f"<div style='color:red'><b>Erro:</b> {error_message}</div>"
