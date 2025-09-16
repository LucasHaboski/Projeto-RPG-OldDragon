from abc import ABC, abstractmethod
from typing import Dict, List

class ClasseBase(ABC):
    """Classe abstrata base para todas as classes de personagem"""
    
    def __init__(self):
        self.dado_vida = 6  # d6 padrão
        self.jogada_protecao_base = 15
        self.nivel = 1
    
    @abstractmethod
    def get_requisitos_atributos(self) -> Dict[str, int]:
        """Retorna os requisitos mínimos de atributos para a classe"""
        pass
    
    @abstractmethod
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais da classe"""
        pass
    
    @abstractmethod
    def get_racas_permitidas(self) -> List[str]:
        """Retorna as raças que podem ser desta classe (None = todas)"""
        pass
    
    def get_dado_vida(self) -> int:
        """Retorna o valor do dado de vida da classe"""
        return self.dado_vida
    
    def get_jogada_protecao_base(self) -> int:
        """Retorna a jogada de proteção base da classe no nível 1"""
        return self.jogada_protecao_base
    
    def get_descricao(self) -> str:
        """Retorna a descrição da classe"""
        return f"Dado de Vida: d{self.dado_vida}, Jogada de Proteção: {self.jogada_protecao_base}"
    
    @abstractmethod
    def get_armas_permitidas(self) -> List[str]:
        """Retorna as armas que a classe pode usar"""
        pass
    
    @abstractmethod
    def get_armaduras_permitidas(self) -> List[str]:
        """Retorna as armaduras que a classe pode usar"""
        pass