from pathlib import Path
from typing import Optional


class LGAIException(Exception):
    """Exceção base para erros do LG-AI"""
    pass


class FileNotFoundError(LGAIException):
    """Erro quando arquivo necessário não é encontrado"""
    pass


class InvalidDataError(LGAIException):
    """Erro quando dados estão em formato inválido"""
    pass


class ValidationError(LGAIException):
    """Erro de validação de dados"""
    pass


def validate_file_exists(filepath: Path) -> None:
    """
    Valida se arquivo existe e é acessível.
    
    Args:
        filepath: Caminho do arquivo
    
    Raises:
        FileNotFoundError: Se arquivo não existe ou não é acessível
    """
    if not filepath.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    if not filepath.is_file():
        raise FileNotFoundError(f"Caminho não é um arquivo: {filepath}")


def normalize_campo(campo: str) -> str:
    """
    Normaliza nome de campo removendo caracteres especiais.
    
    Args:
        campo: Nome do campo original
    
    Returns:
        Campo normalizado (lowercase, underscores)
    
    Examples:
        >>> normalize_campo("NUM__CUPOM-NOTA")
        'num_cupom_nota'
    """
    return (
        campo.strip()
        .lower()
        .replace("__", "_")
        .replace("-", "_")
        .replace(" ", "_")
    )


def sanitize_input(text: str, max_length: int = 100) -> str:
    """
    Sanitiza input do usuário.
    
    Args:
        text: Texto a sanitizar
        max_length: Comprimento máximo permitido
    
    Returns:
        Texto sanitizado
    
    Raises:
        ValidationError: Se input inválido
    """
    if not isinstance(text, str):
        raise ValidationError("Input deve ser string")
    if len(text) > max_length:
        raise ValidationError(f"Input muito longo (max: {max_length})")
    return text.strip()[:max_length]
