from typing import List
from models.dado import Dado
from models.atributos import Atributos
from generators.estilo_geracao import EstiloGeracao

class EstiloClassico(EstiloGeracao):
    """Implementa o estilo clássico de geração de atributos"""
    
    def gerar_valores(self) -> List[int]:
        """Gera 6 valores usando 3d6"""
        return [Dado.rolar_3d6() for _ in range(6)]
    
    def aplicar_valores(self, atributos: Atributos, valores: List[int]) -> None:
        """Aplica os valores na ordem fixa: Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma"""
        for i, nome in enumerate(Atributos.NOMES_ATRIBUTOS):
            atributos.definir_atributo(nome, valores[i])
    
    def get_descricao(self) -> str:
        return "Estilo Clássico: Role 3d6 seis vezes na ordem fixa dos atributos"