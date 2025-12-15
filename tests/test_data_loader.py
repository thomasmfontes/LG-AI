import pytest
from src.data_loader import DataLoader


class TestDataLoader:
    def test_get_lista_redes(self, mock_data_loader):
        """Testa obtenção de lista de redes"""
        redes = mock_data_loader.get_lista_redes()
        assert isinstance(redes, list)
        assert len(redes) == 2
        assert 'MAGAZINE LUIZA' in redes
    
    def test_get_lista_campos(self, mock_data_loader):
        """Testa obtenção de lista de campos"""
        campos = mock_data_loader.get_lista_campos()
        assert isinstance(campos, list)
        assert 'NUM_CUPOM_NOTA' in campos
    
    def test_get_canal_for_rede(self, mock_data_loader):
        """Testa mapeamento rede -> canal"""
        canal = mock_data_loader.get_canal_for_rede('MAGAZINE LUIZA')
        assert canal == 'VAREJO'
    
    def test_cache_get_canal(self, mock_data_loader):
        """Testa cache do mapeamento"""
        # Primeira chamada
        canal1 = mock_data_loader.get_canal_for_rede('MAGAZINE LUIZA')
        # Segunda chamada (deve usar cache)
        canal2 = mock_data_loader.get_canal_for_rede('MAGAZINE LUIZA')
        assert canal1 == canal2
