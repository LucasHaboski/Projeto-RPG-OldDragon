from models.atributos import Atributos
from models.personagem import Personagem
from generators.estilo_geracao import EstiloGeracao
from generators.estilo_classico import EstiloClassico
from generators.estilo_aventureiro import EstiloAventureiro
from generators.estilo_heroico import EstiloHeroico
from races.humano import Humano
from races.elfo import Elfo
from races.anao import Anao
from races.halfling import Halfling
from classes.guerreiro import Guerreiro
from classes.clerigo import Clerigo
from classes.druida import Druida
from core.validador import ValidadorPersonagem

class GeradorPersonagem:
    """Classe principal responsável por gerenciar a criação de personagens"""
    
    def __init__(self):
        self.estilos = {
            "1": EstiloClassico(),
            "2": EstiloAventureiro(),
            "3": EstiloHeroico()
        }
        
        self.racas = {
            "1": Humano(),
            "2": Elfo(),
            "3": Anao(),
            "4": Halfling()
        }
        
        self.classes = {
            "1": Guerreiro(),
            "2": Clerigo(),
            "3": Druida()
        }
    
    def exibir_menu_principal(self) -> None:
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("    GERADOR DE PERSONAGENS - OLD DRAGON")
        print("="*50)
        print("\nEscolha uma opção:")
        print("1. Criar novo personagem completo")
        print("2. Apenas gerar atributos")
        print("0. Sair")
        print("-"*50)
    
    def exibir_menu_estilos(self) -> None:
        """Exibe o menu de estilos de geração"""
        print("\n" + "="*40)
        print("    ESTILOS DE GERAÇÃO")
        print("="*40)
        print("1. Estilo Clássico (3d6 em ordem)")
        print("2. Estilo Aventureiro (3d6 distribuível)")
        print("3. Estilo Heroico (4d6, descarta menor)")
        print("0. Voltar")
        print("-"*40)
    
    def exibir_menu_racas(self) -> None:
        """Exibe o menu de raças disponíveis"""
        print("\n" + "="*40)
        print("    ESCOLHA DA RAÇA")
        print("="*40)
        for num, raca in self.racas.items():
            nome = raca.__class__.__name__
            print(f"{num}. {nome}")
            print(f"   {raca.get_descricao()}")
        print("0. Voltar")
        print("-"*40)
    
    def exibir_menu_classes(self, personagem: Personagem = None) -> None:
        """Exibe o menu de classes disponíveis"""
        print("\n" + "="*40)
        print("    ESCOLHA DA CLASSE")
        print("="*40)
        
        classes_viaveis = []
        if personagem:
            classes_viaveis = ValidadorPersonagem.sugerir_classes_viaveis(personagem)
        
        for num, classe in self.classes.items():
            nome = classe.__class__.__name__
            viavel = nome in classes_viaveis if personagem else True
            status = "✓" if viavel else "✗"
            print(f"{num}. {status} {nome}")
            print(f"   {classe.get_descricao()}")
            
            if personagem:
                requisitos = classe.get_requisitos_atributos()
                req_texto = ", ".join([f"{k}:{v}+" for k, v in requisitos.items()])
                print(f"   Requisitos: {req_texto}")
        
        print("0. Voltar")
        print("-"*40)
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