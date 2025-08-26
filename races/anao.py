from typing import Dict, List
from races.raca_base import RacaBase

class Anao(RacaBase):
    """Implementa a raça Anão do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.movimento = 6  # Movimento reduzido devido ao tamanho
        self.infravisao = 18  # 18 metros de infravisão
        self.alinhamento = "Ordem"
    
    def get_modificadores_atributos(self) -> Dict[str, int]:
        """Anões ganham +1 em Constituição e -1 em Carisma"""
        return {
            "Constituição": 1,
            "Carisma": -1
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais dos anões"""
        return [
            {
                "nome": "Mineradores",
                "descricao": "Conhecimento especial sobre mineração e construções subterrâneas"
            },
            {
                "nome": "Vigoroso",
                "descricao": "Resistência aprimorada contra venenos e doenças"
            },
            {
                "nome": "Armas Grandes",
                "descricao": "Podem usar armas de duas mãos mesmo sendo pequenos"
            },
            {
                "nome": "Inimigos Tradicionais",
                "descricao": "Bônus de ataque contra orcs, goblins e gigantes"
            },
            {
                "nome": "Resistência à Magia",
                "descricao": "Resistência natural contra magias baseada na Constituição"
            }
        ]
    
    def get_restricoes(self) -> List[str]:
        """Restrições dos anões"""
        return [
            "Movimento reduzido (6 metros)",
            "Dificuldade com magias arcanas"
        ]