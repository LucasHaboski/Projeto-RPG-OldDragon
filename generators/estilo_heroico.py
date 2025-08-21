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
        """Permite ao jogador distribuir os valores como desejar"""
        print("\n=== DISTRIBUIÇÃO DE ATRIBUTOS ===")
        print(f"Valores obtidos: {valores}")
        print("\nAtributos disponíveis:")
        for i, nome in enumerate(Atributos.NOMES_ATRIBUTOS):
            print(f"{i+1}. {nome}")
        
        valores_disponiveis = valores.copy()
        
        for nome in Atributos.NOMES_ATRIBUTOS:
            while True:
                try:
                    print(f"\nValores disponíveis: {valores_disponiveis}")
                    escolha = int(input(f"Escolha um valor para {nome} (digite o valor): "))
                    
                    if escolha in valores_disponiveis:
                        atributos.definir_atributo(nome, escolha)
                        valores_disponiveis.remove(escolha)
                        break
                    else:
                        print("Valor inválido ou já usado!")
                except ValueError:
                    print("Por favor, digite um número válido!")
    
    def get_descricao(self) -> str:
        return "Estilo Heroico: Role 4d6 eliminando o menor, seis vezes e distribua como desejar"