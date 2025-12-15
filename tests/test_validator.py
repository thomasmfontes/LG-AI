import pytest
from src.validator import Validator
from src.utils import ValidationError


class TestValidator:
    def test_campo_obrigatorio(self, validator):
        """Testa validação de campo obrigatório"""
        resultado = validator.validar_campo(
            rede="MAGAZINE LUIZA",
            campo="NUM_CUPOM_NOTA"
        )
        assert resultado['status'] == 'obrigatorio'
        assert resultado['campo_formatado'] == 'NUM_CUPOM_NOTA'
        assert resultado['canal'] == 'VAREJO'
    
    def test_campo_opcional(self, validator):
        """Testa validação de campo opcional"""
        resultado = validator.validar_campo(
            rede="MAGAZINE LUIZA",
            campo="OBSERVACAO"
        )
        assert resultado['status'] == 'opcional'
    
    def test_campo_com_formato(self, validator):
        """Testa campo com comentário/formato"""
        resultado = validator.validar_campo(
            rede="MAGAZINE LUIZA",
            campo="DATA_VENDA"
        )
        assert resultado['formato'] is not None
        assert 'DD/MM/AAAA' in resultado['formato']
    
    def test_campo_invalido(self, validator):
        """Testa campo inexistente"""
        with pytest.raises(ValidationError):
            validator.validar_campo(
                rede="MAGAZINE LUIZA",
                campo="CAMPO_INEXISTENTE"
            )
    
    def test_rede_invalida(self, validator):
        """Testa rede inexistente"""
        with pytest.raises(ValidationError):
            validator.validar_campo(
                rede="REDE_INEXISTENTE",
                campo="NUM_CUPOM_NOTA"
            )
    
    def test_input_vazio(self, validator):
        """Testa inputs vazios"""
        with pytest.raises(ValidationError):
            validator.validar_campo(rede="", campo="")
    
    def test_normalizacao_campo(self, validator):
        """Testa normalização automática de campos"""
        resultado = validator.validar_campo(
            rede="MAGAZINE LUIZA",
            campo="NUM__CUPOM-NOTA"  # Com caracteres especiais
        )
        assert resultado['status'] == 'obrigatorio'
