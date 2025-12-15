from pathlib import Path
from typing import Dict


class Config:
    """Configurações centralizadas do projeto"""
    
    # Diretórios
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    ASSETS_DIR = BASE_DIR / "assets"
    SRC_DIR = BASE_DIR / "src"
    
    # Arquivos de dados
    REDES_FILE = DATA_DIR / "Redes_Codigo_Canal.xlsx"
    CAMPOS_FILE = DATA_DIR / "Campos_por_Canal.xlsx"
    MODELO_FILE = DATA_DIR / "Modelo_Arquivo_Vendas.xlsx"
    MANUAL_FILE = DATA_DIR / "Manual_Upload_de_Arquivos_Facilitador.pdf"
    
    # Assets
    FAVICON_FILE = ASSETS_DIR / "favicon.png"
    
    # Mapeamento de canais
    MAPEAMENTO_CANAIS: Dict[str, str] = {
        "DISTRIBUIDOR IT": "IT",
        "ESPECIALIZADO AC": "AC",
        "VAREJO": "VAREJO",
        "ATACADO": "ATACADO",
        "ID B2B": "ID B2B",
        "AC B2B": "AC B2B",
        "DIST": "DIST",
        "DISTGC": "DISTGC",
        "ECOMMERCE": "ECOMMERCE"
    }
    
    # Sinônimos para comentários
    SINONIMOS_COMENTARIOS: Dict[str, str] = {
        "data": "data_venda",
        "cpf_subgerente": "cpf_sub_gerente",
        "nome_subgerente": "nome_sub_gerente",
    }
    
    # Configurações de logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    # URLs
    MANUAL_URL = "https://huggingface.co/spaces/ThomasMF7/ia-clube-lg/resolve/main/Manual_Upload_de_Arquivos_Facilitador.pdf"
