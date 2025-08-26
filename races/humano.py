from typing import Dict, List
from races.raca_base import RacaBase

class Humano(RacaBase):
    """Implementa a raça Humano do Old Dragon"""
    
    def __init__(self):
        super().__init__()
        self.movimento = 9
        self.infravisao = 0  # Humanos não possuem infravisão
        self.alinhamento = "Qualquer"
    
    def get_modificadores_atributos(self) -> Dict[str, int]:
        """Humanos não possuem modificadores de atributos"""
        return {}
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais dos humanos"""
        return [
            {
                "nome": "Aprendizado",
                "descricao": "Humanos ganham 10% de experiência adicional"
            },
            {
                "nome": "Adaptabilidade", 
                "descricao": "Podem ser de qualquer classe sem restrições"
            }
        ]
    
    def get_restricoes(self) -> List[str]:
        """Humanos não possuem restrições"""
        return []
    
    def aplicar_modificadores_personagem(self, personagem) -> None:
        """Aplica o bônus de experiência dos humanos"""
        # O bônus de experiência será aplicado quando o personagem ganhar XP
        pass