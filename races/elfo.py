from typing import Dict, List
from races.raca_base import RacaBase

class Elfo(RacaBase):
    """Implementa a raça Elfo do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.movimento = 9
        self.infravisao = 18  # 18 metros de infravisão
        self.alinhamento = "Ordem ou Neutralidade"
    
    def get_modificadores_atributos(self) -> Dict[str, int]:
        """Elfos ganham +1 em Destreza e -1 em Constituição"""
        return {
            "Destreza": 1,
            "Constituição": -1
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais dos elfos"""
        return [
            {
                "nome": "Gracioso",
                "descricao": "Bônus de +1 em testes de Destreza"
            },
            {
                "nome": "Resistência à Magia",
                "descricao": "Resistência natural contra magias e efeitos mágicos"
            },
            {
                "nome": "Arcos Élficos",
                "descricao": "Proficiência especial com arcos e armas élficas"
            },
            {
                "nome": "Detectar Portas Secretas",
                "descricao": "Chance maior de encontrar portas e passagens secretas"
            }
        ]
    
    def get_restricoes(self) -> List[str]:
        """Restrições dos elfos"""
        return [
            "Não podem ser ressuscitados por magias",
            "Sensíveis ao ferro frio"
        ]