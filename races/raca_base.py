from abc import ABC, abstractmethod
from typing import Dict, List

class RacaBase(ABC):
    """Classe abstrata base para todas as raças"""
    
    def __init__(self):
        # Características comuns a todas as raças
        self.movimento: int = 9  # Metros
        self.infravisao: int = 0  # Metros (0 = não possui)
        self.alinhamento: str = "Qualquer"  # Tendência de alinhamento
        
    @abstractmethod
    def get_modificadores_atributos(self) -> Dict[str, int]:
        """Retorna os modificadores de atributos da raça"""
        pass
    
    @abstractmethod
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais da raça"""
        pass
    
    @abstractmethod
    def get_restricoes(self) -> List[str]:
        """Retorna as restrições da raça"""
        pass
    
    def get_descricao(self) -> str:
        """Retorna a descrição da raça"""
        return f"Movimento: {self.movimento}m, Infravisão: {self.infravisao}m, Alinhamento: {self.alinhamento}"
    
    def aplicar_modificadores_personagem(self, personagem) -> None:
        """Aplica modificadores específicos da raça ao personagem"""
        # Implementação padrão - pode ser sobrescrita pelas raças filhas
        pass