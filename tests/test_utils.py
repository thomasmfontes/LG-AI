import pytest
from pathlib import Path
from src.utils import (
    normalize_campo,
    sanitize_input,
    validate_file_exists,
    ValidationError,
    FileNotFoundError as LGAIFileNotFoundError
)


class TestNormalizeCampo:
    def test_lowercase(self):
        assert normalize_campo("NUM_CUPOM") == "num_cupom"
    
    def test_double_underscore(self):
        assert normalize_campo("NUM__CUPOM") == "num_cupom"
    
    def test_hyphen(self):
        assert normalize_campo("NUM-CUPOM") == "num_cupom"
    
    def test_space(self):
        assert normalize_campo("NUM CUPOM") == "num_cupom"
    
    def test_combined(self):
        assert normalize_campo("NUM__CUPOM-NOTA FISCAL") == "num_cupom_nota_fiscal"


class TestSanitizeInput:
    def test_valid_input(self):
        assert sanitize_input("  test  ") == "test"
    
    def test_max_length(self):
        with pytest.raises(ValidationError):
            sanitize_input("a" * 101, max_length=100)
    
    def test_non_string(self):
        with pytest.raises(ValidationError):
            sanitize_input(123)


class TestValidateFileExists:
    def test_existing_file(self, tmp_path):
        file = tmp_path / "test.txt"
        file.write_text("test")
        validate_file_exists(file)  # Should not raise
    
    def test_non_existing_file(self, tmp_path):
        file = tmp_path / "nonexistent.txt"
        with pytest.raises(LGAIFileNotFoundError):
            validate_file_exists(file)
    
    def test_directory(self, tmp_path):
        with pytest.raises(LGAIFileNotFoundError):
            validate_file_exists(tmp_path)
