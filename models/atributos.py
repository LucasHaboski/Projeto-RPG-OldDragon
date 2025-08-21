from typing import Dict

class Atributos:
    """Classe que representa os atributos de um personagem"""
    
    NOMES_ATRIBUTOS = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    
    def __init__(self):
        self.atributos: Dict[str, int] = {nome: 0 for nome in self.NOMES_ATRIBUTOS}
    
    def definir_atributo(self, nome: str, valor: int) -> None:
        """Define o valor de um atributo específico"""
        if nome in self.atributos:
            self.atributos[nome] = valor
        else:
            raise ValueError(f"Atributo '{nome}' não existe")
    
    def obter_atributo(self, nome: str) -> int:
        """Obtém o valor de um atributo específico"""
        return self.atributos.get(nome, 0)
    
    def obter_todos_atributos(self) -> Dict[str, int]:
        """Retorna todos os atributos"""
        return self.atributos.copy()
    
    def interpretar_nivel(self, valor: int) -> str:
        """Interpreta o nível de um atributo baseado no valor"""
        if valor <= 3:
            return "Terrível"
        elif 4 <= valor <= 5:
            return "Ruim"
        elif 6 <= valor <= 8:
            return "Abaixo da média"
        elif 9 <= valor <= 12:
            return "Mediano"
        elif 13 <= valor <= 16:
            return "Influente"
        elif 17 <= valor <= 18:
            return "Ídolo"
        else:
            return "Lendário"