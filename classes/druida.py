from typing import Dict, List
from classes.classe_base import ClasseBase

class Druida(ClasseBase):
    """Implementa a classe Druida do Old Dragon (subclasse do Clérigo)"""
    
    def __init__(self):
        super().__init__()
        self.dado_vida = 6  # d6 como clérigos
        self.jogada_protecao_base = 15
    
    def get_requisitos_atributos(self) -> Dict[str, int]:
        """Druidas precisam de Sabedoria 12+ e Carisma 15+"""
        return {
            "Sabedoria": 12,
            "Carisma": 15
        }
    
    def get_habilidades(self) -> List[Dict[str, str]]:
        """Retorna as habilidades especiais do druida"""
        return [
            {
                "nome": "Magias da Natureza",
                "descricao": "Conjura magias divinas relacionadas à natureza"
            },
            {
                "nome": "Forma Animal",
                "descricao": "Pode se transformar em animais (7º nível+)"
            },
            {
                "nome": "Comunicação com Animais",
                "descricao": "Pode se comunicar com animais naturalmente"
            },
            {
                "nome": "Imunidade a Charme",
                "descricao": "Imune a encantos de fadas e seres feéricos (7º nível+)"
            },
            {
                "nome": "Passo sem Rastros",
                "descricao": "Move-se pela natureza sem deixar rastros"
            },
            {
                "nome": "Resistência aos Elementos",
                "descricao": "Resistência a fogo e frio (3º nível+)"
            },
            {
                "nome": "Linguagem Secreta",
                "descricao": "Conhece a linguagem secreta dos druidas"
            }
        ]
    
    def get_racas_permitidas(self) -> List[str]:
        """Apenas humanos e halflings podem ser druidas"""
        return ["Humano", "Halfling"]
    
    def get_armas_permitidas(self) -> List[str]:
        """Druidas só podem usar armas naturais"""
        return [
            "Clava",
            "Adaga",
            "Dardos",
            "Lança",
            "Bastão",
            "Funda",
            "Cimitarra"
        ]
    
    def get_armaduras_permitidas(self) -> List[str]:
        """Druidas só podem usar armaduras de materiais naturais"""
        return [
            "Armadura de couro",
            "Armadura de couro batido",
            "Escudo de couro ou madeira"
        ]
    
    def get_restricoes(self) -> List[str]:
        """Retorna as restrições específicas dos druidas"""
        return [
            "Deve ser neutro",
            "Não pode usar metais trabalhados (armas/armaduras)",
            "Não pode acumular mais tesouros que consegue carregar",
            "Deve proteger a natureza",
            "Hierarquia druídica limitada"
        ]
    
    def get_formas_animais_disponiveis(self, nivel: int) -> List[str]:
        """Retorna as formas animais disponíveis por nível"""
        if nivel < 7:
            return []
        
        formas = ["Lobo", "Urso", "Javali", "Águia"]
        
        if nivel >= 10:
            formas.extend(["Urso das Cavernas", "Tigre", "Puma"])
        
        if nivel >= 12:
            formas.extend(["Elemental menor da Terra", "Elemental menor da Água"])
        
        return formas
    
    def get_magias_por_nivel(self, nivel: int, nivel_magia: int) -> int:
        """Calcula quantas magias o druida pode conjurar por dia"""
        # Tabela similar ao clérigo, mas com progressão ligeiramente diferente
        tabela_magias = {
            1: {1: 0},
            2: {1: 1},
            3: {1: 2},
            4: {1: 2, 2: 1},
            5: {1: 2, 2: 2},
            6: {1: 3, 2: 2, 3: 1},
            7: {1: 3, 2: 3, 3: 2},
            8: {1: 3, 2: 3, 3: 2, 4: 1},
            9: {1: 4, 2: 3, 3: 3, 4: 2},
            10: {1: 4, 2: 4, 3: 3, 4: 2, 5: 1}
        }
        
        if nivel in tabela_magias and nivel_magia in tabela_magias[nivel]:
            return tabela_magias[nivel][nivel_magia]
        return 0
    
    def usos_forma_animal_por_dia(self, nivel: int) -> int:
        """Calcula quantas vezes por dia pode usar forma animal"""
        if nivel < 7:
            return 0
        return min(3, (nivel - 6) // 2 + 1)