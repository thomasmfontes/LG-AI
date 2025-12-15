import pytest
import pandas as pd
from pathlib import Path
import sys

# Adiciona src ao path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_loader import DataLoader
from src.validator import Validator
from src.formatter import ResponseFormatter


@pytest.fixture
def mock_data_loader():
    """Cria DataLoader com dados mockados"""
    loader = DataLoader()
    
    # Mock df_redes
    loader.df_redes = pd.DataFrame({
        'Rede': ['MAGAZINE LUIZA', 'CASAS BAHIA'],
        'Canal': ['VAREJO', 'VAREJO']
    })
    
    # Mock df_campos
    loader.df_campos = pd.DataFrame({
        'CAMPO': ['NUM_CUPOM_NOTA', 'DATA_VENDA', 'OBSERVACAO'],
        'CAMPO_NORMALIZADO': ['num_cupom_nota', 'data_venda', 'observacao'],
        'VAREJO': ['✓', '✓', '']
    })
    
    # Mock comentarios
    loader.comentarios = {
        'num_cupom_nota': 'Número do cupom fiscal',
        'data_venda': 'Data no formato DD/MM/AAAA'
    }
    
    # Mock mapa
    loader.mapa_rede_canal = {
        'MAGAZINE LUIZA': 'VAREJO',
        'CASAS BAHIA': 'VAREJO'
    }
    
    loader._loaded = True
    
    return loader


@pytest.fixture
def validator(mock_data_loader):
    """Cria Validator com dados mockados"""
    return Validator(mock_data_loader)


@pytest.fixture
def formatter():
    """Cria ResponseFormatter"""
    return ResponseFormatter()
