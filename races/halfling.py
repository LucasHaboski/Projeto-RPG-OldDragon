from typing import Dict, List
from races.raca_base import RacaBase

class Halfling(RacaBase):
    """Implementa a raça Halfling do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.movimento = 6  # Movimento reduzido devido ao tamanho
        self.infravisao = 0  # Halflings não possuem infravisão
        self.alinhamento = "Neutralidade"
    
    def get_modificadores_atributos(self) -> Dict[str, int]:
        """Halflings ganham +1 em Destreza e -1 em Força"""
        return {
            "Destreza": 1,
            "Força": -1
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais dos halflings"""
        return [
            {
                "nome": "Furtividade",
                "descricao": "Habilidade natural para se esconder e se mover silenciosamente"
            },
            {
                "nome": "Armas de Projétil",
                "descricao": "Bônus especial com fundas, arcos e outras armas de arremesso"
            },
            {
                "nome": "Resistência",
                "descricao": "Resistência aprimorada contra medo e efeitos mentais"
            },
            {
                "nome": "Sorte",
                "descricao": "Uma vez por dia pode rolar novamente um teste falhado"
            }
        ]
    
    def get_restricoes(self) -> List[str]:
        """Restrições dos halflings"""
        return [
            "Movimento reduzido (6 metros)",
            "Só podem usar armas médias como armas de duas mãos",
            "Limitações com armaduras pesadas"
        ]