# generators/estilo_aventureiro.py
from typing import List
from models.dado import Dado
from models.atributos import Atributos
from generators.estilo_geracao import EstiloGeracao

class EstiloAventureiro(EstiloGeracao):
    """Implementa o estilo aventureiro de geração de atributos"""
    
    def gerar_valores(self) -> List[int]:
        """Gera 6 valores usando 3d6"""
        return [Dado.rolar_3d6() for _ in range(6)]
    
    def aplicar_valores(self, atributos: Atributos, valores: List[int]) -> None:
        """
        Em uma aplicação web, a distribuição de valores é feita pela
        lógica do servidor (controller/rota) e não pela classe de estilo,
        para evitar a necessidade de input do usuário.
        Portanto, este método não precisa realizar nenhuma ação.
        """
        pass
    
    def get_descricao(self) -> str:
        return "Estilo Aventureiro: Role 3d6 seis vezes e distribua como desejar"