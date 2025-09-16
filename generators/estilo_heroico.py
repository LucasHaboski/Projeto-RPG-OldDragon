# generators/estilo_heroico.py
from typing import List
from models.dado import Dado
from models.atributos import Atributos
from generators.estilo_geracao import EstiloGeracao

class EstiloHeroico(EstiloGeracao):
    """Implementa o estilo heroico de geração de atributos"""
    
    def gerar_valores(self) -> List[int]:
        """Gera 6 valores usando 4d6 eliminando o menor"""
        return [Dado.rolar_4d6_drop_lowest() for _ in range(6)]
    
    def aplicar_valores(self, atributos: Atributos, valores: List[int]) -> None:
        """
        Em uma aplicação web, a distribuição de valores é feita pela
        lógica do servidor (controller/rota) e não pela classe de estilo,
        para evitar a necessidade de input do usuário.
        Portanto, este método não precisa realizar nenhuma ação.
        """
        pass
    
    def get_descricao(self) -> str:
        return "Estilo Heroico: Role 4d6 eliminando o menor, seis vezes e distribua como desejar"