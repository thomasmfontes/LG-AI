"""
LG-AI - Assistente Técnico Clube LG
Módulos principais para validação de campos de vendas
"""

__version__ = "2.0.0"
__author__ = "Thomas MF"

from .data_loader import DataLoader
from .validator import Validator
from .formatter import ResponseFormatter
from .logger import setup_logger

__all__ = [
    "DataLoader",
    "Validator",
    "ResponseFormatter",
    "setup_logger"
]
