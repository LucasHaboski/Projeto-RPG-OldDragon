from models.atributos import Atributos
from generators.estilo_geracao import EstiloGeracao
from generators.estilo_classico import EstiloClassico
from generators.estilo_aventureiro import EstiloAventureiro
from generators.estilo_heroico import EstiloHeroico

class GeradorPersonagem:
    """Classe principal responsável por gerenciar a criação de personagens"""
    
    def __init__(self):
        self.estilos = {
            "1": EstiloClassico(),
            "2": EstiloAventureiro(),
            "3": EstiloHeroico()
        }
    
    def exibir_menu(self) -> None:
        """Exibe o menu de opções"""
        print("\n" + "="*50)
        print("    GERADOR DE ATRIBUTOS - OLD DRAGON")
        print("="*50)
        print("\nEscolha o estilo de geração:")
        print("1. Estilo Clássico")
        print("2. Estilo Aventureiro") 
        print("3. Estilo Heroico")
        print("0. Sair")
        print("-"*50)
    
    def gerar_personagem(self, estilo: EstiloGeracao) -> Atributos:
        """Gera um personagem usando o estilo especificado"""
        print(f"\n{estilo.get_descricao()}")
        
        atributos = Atributos()
        valores = estilo.gerar_valores()
        estilo.aplicar_valores(atributos, valores)
        
        return atributos
    
    def exibir_personagem(self, atributos: Atributos) -> None:
        """Exibe os atributos do personagem gerado"""
        print("\n" + "="*50)
        print("           PERSONAGEM GERADO")
        print("="*50)
        
        todos_atributos = atributos.obter_todos_atributos()
        
        for nome, valor in todos_atributos.items():
            nivel = atributos.interpretar_nivel(valor)
            print(f"{nome:12}: {valor:2d} ({nivel})")
        
        # Estatísticas
        valores = list(todos_atributos.values())
        media = sum(valores) / len(valores)
        print(f"\nMédia dos atributos: {media:.1f}")
        print(f"Maior atributo: {max(valores)}")
        print(f"Menor atributo: {min(valores)}")
    
    def executar(self) -> None:
        """Executa o programa principal"""
        print("Bem-vindo ao Gerador de Atributos do Old Dragon!")
        
        while True:
            self.exibir_menu()
            
            try:
                opcao = input("\nDigite sua opção: ").strip()
                
                if opcao == "0":
                    print("Saindo... Que suas aventuras sejam épicas!")
                    break
                elif opcao in self.estilos:
                    estilo = self.estilos[opcao]
                    personagem = self.gerar_personagem(estilo)
                    self.exibir_personagem(personagem)
                    
                    input("\nPressione ENTER para continuar...")
                else:
                    print("Opção inválida! Tente novamente.")
            
            except KeyboardInterrupt:
                print("\n\nPrograma interrompido pelo usuário.")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")