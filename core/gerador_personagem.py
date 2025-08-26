from models import personagem
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



def exibir_info_raca(self, raca) -> None:
    """Exibe informações detalhadas de uma raça"""
    print(f"\n📋 INFORMAÇÕES: {raca.__class__.__name__.upper()}")
    print("="*40)
    print(f"Movimento: {raca.movimento}m")
    print(f"Infravisão: {raca.infravisao}m" if raca.infravisao > 0 else "Infravisão: Não")
    print(f"Alinhamento: {raca.alinhamento}")
    
    modificadores = raca.get_modificadores_atributos()
    if modificadores:
        print("\nModificadores de Atributos:")
        for attr, mod in modificadores.items():
            sinal = "+" if mod >= 0 else ""
            print(f"  {attr}: {sinal}{mod}")
    
    print("\nHabilidades Especiais:")
    for hab in raca.get_habilidades():
        print(f"  • {hab['nome']}: {hab['descricao']}")
    
    restricoes = raca.get_restricoes()
    if restricoes:
        print("\nRestrições:")
        for rest in restricoes:
            print(f"  • {rest}")
    
def exibir_info_classe(self, classe) -> None:
    """Exibe informações detalhadas de uma classe"""
    print(f"\n📋 INFORMAÇÕES: {classe.__class__.__name__.upper()}")
    print("="*40)
    print(f"Dado de Vida: d{classe.get_dado_vida()}")
    print(f"Jogada de Proteção: {classe.get_jogada_protecao_base()}")
    
    requisitos = classe.get_requisitos_atributos()
    if requisitos:
        print("\nRequisitos:")
        for attr, valor in requisitos.items():
            print(f"  {attr}: {valor}+")
    
    print("\nHabilidades:")
    for hab in classe.get_habilidades():
        print(f"  • {hab['nome']}: {hab['descricao']}")
    
    print(f"\nArmas Permitidas: {', '.join(classe.get_armas_permitidas()[:3])}...")
    print(f"Armaduras Permitidas: {', '.join(classe.get_armaduras_permitidas()[:3])}...")
            
def exibir_personagem_completo(self, personagem: Personagem) -> None:
    """Exibe as informações completas do personagem"""
    resumo = personagem.obter_resumo()
    
    print("\n" + "="*60)
    print(f"           PERSONAGEM: {resumo['nome'].upper()}")
    print("="*60)
    
    # Informações básicas
    print(f"🏷️  Raça: {resumo['raca']}")
    print(f"⚔️  Classe: {resumo['classe']}")
    print(f"📊 Nível: {resumo['nivel']}")
    print(f"❤️  Pontos de Vida: {resumo['pontos_vida']}")
    print(f"🛡️  Classe de Armadura: {resumo['classe_armadura']}")
    print(f"🎲 Jogada de Proteção: {resumo['jogada_protecao']}")
    
    # Atributos
    print(f"\n📈 ATRIBUTOS:")
    print("-"*30)
    
    for nome, valor in result['atributos'].items():
        modificador = personagem.get_modificador_atributo(nome)
        sinal = "+" if modificador >= 0 else ""
        nivel = personagem.atributos.interpretar_nivel(valor)
        print(f"{nome:12}: {valor:2d} ({sinal}{modificador}) - {nivel}")
        # Características da raça
    if result['raca'] != "Nenhuma":
        print(f"\n🏃 CARACTERÍSTICAS DA RAÇA:")
        print("-"*30)
        print(f"Movimento: {result['movimento']}m")
    if result['infravisao'] > 0:
        print(f"Infravisão: {result['infravisao']}m")
        print(f"Alinhamento: {result['alinhamento_tendencia']}")
        
        # Habilidades
        if 'habilidades_raca' in result and result['habilidades_raca']:
            print(f"\n🌟 HABILIDADES DA RAÇA:")
            print("-"*30)
            for hab in result['habilidades_raca']:
                print(f"• {hab}")
        
        if 'habilidades_classe' in result and result['habilidades_classe']:
            print(f"\n⚡ HABILIDADES DA CLASSE:")
            print("-"*30)
            for hab in result['habilidades_classe']:
                print(f"• {hab}")
        
        # Estatísticas
        stats = ValidadorPersonagem.calcular_pontuacao_atributos(personagem)
        print(f"\n📊 ESTATÍSTICAS:")
        print("-"*30)
        print(f"Soma Total: {stats['soma_total']}")
        print(f"Média: {stats['media']}")
        print(f"Maior Atributo: {stats['maior_atributo']}")
        print(f"Menor Atributo: {stats['menor_atributo']}")
        print(f"Atributos ≥15: {stats['atributos_acima_15']}")
        print(f"Atributos ≤8: {stats['atributos_abaixo_8']}")
    
        def exibir_atributos_simples(self, atributos: Atributos) -> None:
            """Exibe apenas os atributos (modo antigo)"""
            print("\n" + "="*50)
            print("           ATRIBUTOS GERADOS")
            print("="*50)
            
            todos_atributos = atributos.obter_todos_atributos()
            
            for nome, valor in todos_atributos.items():
                nivel = atributos.interpretar_nivel(valor)
                print(f"{nome:12}: {valor:2d} ({nivel})")
            
            # Estatísticas simples
            valores = list(todos_atributos.values())
            media = sum(valores) / len(valores)
            print(f"\nMédia dos atributos: {media:.1f}")
            print(f"Maior atributo: {max(valores)}")
            print(f"Menor atributo: {min(valores)}")
    
        def executar(self) -> None:
            """Executa o programa principal"""
            print("🐉 Bem-vindo ao Gerador de Personagens do Old Dragon! 🐉")
            
            while True:
                self.exibir_menu_principal()
                
                try:
                    opcao = input("\nDigite sua opção: ").strip()
                    
                    if opcao == "0":
                        print("Saindo... Que suas aventuras sejam épicas! 🌟")
                        break
                    elif opcao == "1":
                        # Criar personagem completo
                        personagem = self.criar_personagem_completo()
                        if personagem:
                            self.exibir_personagem_completo(personagem)
                            
                            # Opção de salvar (simplificada)
                            salvar = input("\nDeseja ver o resumo novamente? (s/n): ").strip().lower()
                            if salvar in ['s', 'sim']:
                                self.exibir_personagem_completo(personagem)
                        
                        input("\nPressione ENTER para continuar...")
                        
                    elif opcao == "2":
                        # Apenas gerar atributos (modo antigo)
                        estilo = self.escolher_estilo()
                        if estilo:
                            atributos = self.gerar_atributos(estilo)
                            self.exibir_atributos_simples(atributos)
                        
                        input("\nPressione ENTER para continuar...")
                        
                    else:
                        print("Opção inválida! Tente novamente.")
                
                except KeyboardInterrupt:
                    print("\n\nPrograma interrompido pelo usuário.")
                    break
                except Exception as e:
                    print(f"Erro inesperado: {e}")
                    input("Pressione ENTER para continuar...")


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