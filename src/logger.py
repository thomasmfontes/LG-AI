import logging
import sys
from pathlib import Path
from typing import Optional
from config import Config


def setup_logger(
    name: str = "lg_ai",
    level: Optional[str] = None,
    log_file: Optional[Path] = None
) -> logging.Logger:
    """
    Configura logger estruturado para a aplicação.
    
    Args:
        name: Nome do logger
        level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Caminho opcional para arquivo de log
    
    Returns:
        Logger configurado
    """
    logger = logging.getLogger(name)
    
    # Define nível
    log_level = level or Config.LOG_LEVEL
    logger.setLevel(getattr(logging, log_level))
    
    # Remove handlers existentes
    logger.handlers.clear()
    
    # Formatter
    formatter = logging.Formatter(
        Config.LOG_FORMAT,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (opcional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, log_level))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
