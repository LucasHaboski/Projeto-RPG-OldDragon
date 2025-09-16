from typing import Dict, List
from models.classe_base import ClasseBase

class Guerreiro(ClasseBase):
    """Implementa a classe Guerreiro do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.dado_vida = 8  # d8 para guerreiros
        self.jogada_protecao_base = 14  # Melhor jogada de proteção
    
    def get_requisitos_atributos(self) -> Dict[str, int]:
        """Guerreiros precisam de Força 9+"""
        return {
            "Força": 9
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais do guerreiro"""
        return [
            {
                "nome": "Especialização em Armas",
                "descricao": "Pode se especializar em tipos específicos de armas"
            },
            {
                "nome": "Ataques Múltiplos",
                "descricao": "Ganha ataques adicionais em níveis superiores"
            },
            {
                "nome": "Liderança",
                "descricao": "Pode comandar tropas e seguidores em níveis altos"
            },
            {
                "nome": "Fortaleza",
                "descricao": "Pode construir uma fortaleza e atrair seguidores no nível 9"
            }
        ]
    
    def get_racas_permitidas(self) -> List[str]:
        """Todas as raças podem ser guerreiros"""
        return None  # None significa todas as raças
    
    def get_armas_permitidas(self) -> List[str]:
        """Guerreiros podem usar todas as armas"""
        return [
            "Todas as armas corpo a corpo",
            "Todas as armas de projétil",
            "Armas exóticas com treinamento"
        ]
    
    def get_armaduras_permitidas(self) -> List[str]:
        """Guerreiros podem usar todas as armaduras"""
        return [
            "Armadura de couro",
            "Armadura de couro batido", 
            "Cota de malha",
            "Armadura de escamas",
            "Brunea",
            "Armadura de placas",
            "Escudo"
        ]
    
    def calcular_bonus_ataque_nivel(self, nivel: int) -> int:
        """Calcula o bônus de ataque baseado no nível"""
        return nivel  # Guerreiros ganham +1 ataque por nível
    
    def get_ataques_por_rodada(self, nivel: int) -> float:
        """Calcula quantos ataques o guerreiro pode fazer por rodada"""
        if nivel >= 15:
            return 2.0
        elif nivel >= 8:
            return 1.5
        else:
            return 1.0