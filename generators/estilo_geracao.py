from abc import ABC, abstractmethod
from typing import List
from models.atributos import Atributos

class EstiloGeracao(ABC):
    """Classe abstrata para definir estilos de geração de atributos"""
    
    @abstractmethod
    def gerar_valores(self) -> List[int]:
        """Método abstrato para gerar os valores dos atributos"""
        pass
    
    @abstractmethod
    def aplicar_valores(self, atributos: Atributos, valores: List[int]) -> None:
        """Método abstrato para aplicar os valores aos atributos"""
        pass
    
    @abstractmethod
    def get_descricao(self) -> str:
        """Retorna a descrição do estilo"""
        pass