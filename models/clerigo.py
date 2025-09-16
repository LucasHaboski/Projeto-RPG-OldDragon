from typing import Dict, List
from models.classe_base import ClasseBase

class Clerigo(ClasseBase):
    """Implementa a classe Clérigo do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.dado_vida = 6  # d6 para clérigos
        self.jogada_protecao_base = 15
    
    def get_requisitos_atributos(self) -> Dict[str, int]:
        """Clérigos precisam de Sabedoria 9+"""
        return {
            "Sabedoria": 9
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais do clérigo"""
        return [
            {
                "nome": "Magias Divinas",
                "descricao": "Pode conjurar magias divinas baseadas na Sabedoria"
            },
            {
                "nome": "Afastar Mortos-vivos",
                "descricao": "Pode afastar ou destruir criaturas mortas-vivas"
            },
            {
                "nome": "Cura Milagrosa",
                "descricao": "Uma vez por dia pode curar ferimentos graves"
            },
            {
                "nome": "Detecção do Mal",
                "descricao": "Pode detectar presenças malignas próximas"
            },
            {
                "nome": "Proteção Divina",
                "descricao": "Resistência aprimorada contra efeitos malignos"
            }
        ]
    
    def get_racas_permitidas(self) -> List[str]:
        """Raças que podem ser clérigos"""
        return ["Humano", "Anao", "Halfling"]  # Elfos geralmente não são clérigos
    
    def get_armas_permitidas(self) -> List[str]:
        """Clérigos têm restrições com armas cortantes"""
        return [
            "Martelo de guerra",
            "Clava",
            "Maça",
            "Bastão",
            "Mangual",
            "Funda",
            "Dardos"
        ]
    
    def get_armaduras_permitidas(self) -> List[str]:
        """Clérigos podem usar a maioria das armaduras"""
        return [
            "Armadura de couro",
            "Armadura de couro batido",
            "Cota de malha", 
            "Armadura de escamas",
            "Brunea",
            "Escudo"
        ]
    
    def get_magias_por_nivel(self, nivel: int, nivel_magia: int) -> int:
        """Calcula quantas magias o clérigo pode conjurar por dia"""
        # Tabela simplificada de magias por dia
        tabela_magias = {
            1: {1: 0},  # Nível 1 não tem magias
            2: {1: 1},
            3: {1: 2},
            4: {1: 2, 2: 1},
            5: {1: 2, 2: 2},
            6: {1: 2, 2: 2, 3: 1},
            7: {1: 3, 2: 2, 3: 2},
            8: {1: 3, 2: 3, 3: 2, 4: 1},
            9: {1: 4, 2: 3, 3: 3, 4: 2}
        }
        
        if nivel in tabela_magias and nivel_magia in tabela_magias[nivel]:
            return tabela_magias[nivel][nivel_magia]
        return 0
    
    def pode_afastar_mortos_vivos(self, nivel: int) -> Dict[str, int]:
        """Calcula a capacidade de afastar mortos-vivos"""
        return {
            "usos_por_dia": 3 + (nivel // 3),
            "nivel_maximo": nivel + 1
        }