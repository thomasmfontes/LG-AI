from datetime import datetime
import json
from pathlib import Path
from typing import List, Dict
from collections import Counter

from .logger import setup_logger

logger = setup_logger(__name__)


class Analytics:
    """Rastreia e analisa uso da aplicação"""
    
    def __init__(self, log_file: Path = Path("analytics.jsonl")):
        self.log_file = log_file
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def log_query(self, rede: str, campo: str, resultado: str) -> None:
        """
        Registra uma consulta.
        
        Args:
            rede: Nome da rede consultada
            campo: Campo consultado
            resultado: Resultado da validação
        """
        event = {
            'timestamp': datetime.now().isoformat(),
            'rede': rede,
            'campo': campo,
            'resultado': resultado
        }
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(json.dumps(event, ensure_ascii=False) + '\n')
            logger.debug(f"Query registrada: {rede} - {campo}")
        except Exception as e:
            logger.error(f"Erro ao registrar query: {e}")
    
    def get_stats(self) -> Dict[str, any]:
        """
        Obtém estatísticas de uso.
        
        Returns:
            Dicionário com estatísticas
        """
        if not self.log_file.exists():
            return {
                'total_queries': 0,
                'top_redes': [],
                'top_campos': []
            }
        
        try:
            queries = []
            with open(self.log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    queries.append(json.loads(line))
            
            redes = [q['rede'] for q in queries]
            campos = [q['campo'] for q in queries]
            
            return {
                'total_queries': len(queries),
                'top_redes': Counter(redes).most_common(5),
                'top_campos': Counter(campos).most_common(5)
            }
        except Exception as e:
            logger.error(f"Erro ao obter estatísticas: {e}")
            return {
                'total_queries': 0,
                'top_redes': [],
                'top_campos': []
            }
