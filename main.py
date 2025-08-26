"""
Sistema Completo de Criação de Personagens - Old Dragon RPG

Este programa implementa um sistema completo para criar personagens
seguindo as regras do Old Dragon RPG, incluindo:
- 3 estilos de geração de atributos
- 4 raças principais (Humano, Elfo, Anão, Halfling)
- 3 classes (Guerreiro, Clérigo, Druida)
- Validação automática de requisitos
- Interface completa e intuitiva

Autor: Sistema Old Dragon
Versão: 2.0
"""

from core.gerador_personagem import GeradorPersonagem

def main():
    """Função principal do sistema"""
    try:
        gerador = GeradorPersonagem()
        gerador.executar()
    except Exception as e:
        print(f"\nErro fatal no sistema: {e}")
        print("Por favor, verifique a instalação e tente novamente.")
        input("Pressione ENTER para sair...")

if __name__ == "__main__":
    main()