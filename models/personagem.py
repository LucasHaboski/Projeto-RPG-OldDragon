from typing import Optional
from models.atributos import Atributos
import json  # <--- Alteração: Importação adicionada

class Personagem:
    """Classe que representa um personagem completo de Old Dragon"""
    
    def __init__(
        self,
        atributos: Optional[Atributos] = None,
        raca: Optional[object] = None,
        classe: Optional[object] = None,
        nome: str = ""
    ):
        self.nome = nome
        self.atributos = atributos if atributos is not None else Atributos()
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.pontos_vida = 0
        self.classe_armadura = 10
        self.jogada_protecao = 15

        # Aplica modificadores e cálculos se raça/classe já vierem preenchidos
        if self.raca:
            self.definir_raca(self.raca)
        if self.classe:
            self.definir_classe(self.classe)
    
    def definir_raca(self, raca) -> None:
        """Define a raça do personagem e aplica seus modificadores"""
        self.raca = raca
        # Aplica modificadores de atributos da raça
        modificadores = raca.get_modificadores_atributos()
        for nome_atributo, modificador in modificadores.items():
            valor_atual = self.atributos.obter_atributo(nome_atributo)
            novo_valor = max(3, min(18, valor_atual + modificador))  # Mantém entre 3-18
            self.atributos.definir_atributo(nome_atributo, novo_valor)
    
    def definir_classe(self, classe) -> None:
        """Define a classe do personagem"""
        self.classe = classe
        self.calcular_pontos_vida()
        self.calcular_classe_armadura()
        self.calcular_jogada_protecao()
    
    def calcular_pontos_vida(self) -> None:
        """Calcula os pontos de vida baseado na classe e constituição"""
        if self.classe:
            dado_vida = self.classe.get_dado_vida()
            modificador_con = self.get_modificador_atributo("Constituição")
            self.pontos_vida = max(1, dado_vida + modificador_con)
    
    def calcular_classe_armadura(self) -> None:
        """Calcula a classe de armadura baseada na destreza"""
        modificador_des = self.get_modificador_atributo("Destreza")
        self.classe_armadura = 10 - modificador_des  # CA menor é melhor no Old Dragon
    
    def calcular_jogada_protecao(self) -> None:
        """Calcula a jogada de proteção baseada na classe"""
        if self.classe:
            self.jogada_protecao = self.classe.get_jogada_protecao_base()
    
    def get_modificador_atributo(self, nome_atributo: str) -> int:
        """Calcula o modificador de um atributo seguindo as regras do Old Dragon"""
        valor = self.atributos.obter_atributo(nome_atributo)
        if valor <= 3:
            return -3
        elif valor <= 5:
            return -2
        elif valor <= 8:
            return -1
        elif valor <= 12:
            return 0
        elif valor <= 15:
            return 1
        elif valor <= 17:
            return 2
        else:  # 18+
            return 3
    
    def pode_ser_classe(self, classe) -> tuple[bool, str]:
        """Verifica se o personagem pode ser da classe especificada"""
        requisitos = classe.get_requisitos_atributos()
        for nome_atributo, valor_minimo in requisitos.items():
            valor_atual = self.atributos.obter_atributo(nome_atributo)
            if valor_atual < valor_minimo:
                return False, f"Requisito não atendido: {nome_atributo} deve ser pelo menos {valor_minimo} (atual: {valor_atual})"
        
        # Verifica restrições de raça
        racas_permitidas = classe.get_racas_permitidas()
        if racas_permitidas and self.raca:
            if self.raca.__class__.__name__ not in racas_permitidas:
                return False, f"Raça {self.raca.__class__.__name__} não pode ser {classe.__class__.__name__}"
        
        return True, "Requisitos atendidos"
    
    def obter_resumo(self) -> dict:
        """Retorna um resumo completo do personagem"""
        resumo = {
            "nome": self.nome,
            "nivel": self.nivel,
            "pontos_vida": self.pontos_vida,
            "classe_armadura": self.classe_armadura,
            "jogada_protecao": self.jogada_protecao,
            "atributos": self.atributos.obter_todos_atributos(),
            "raca": self.raca.__class__.__name__ if self.raca else "Nenhuma",
            "classe": self.classe.__class__.__name__ if self.classe else "Nenhuma"
        }
        
        # Adiciona informações da raça
        if self.raca:
            resumo["movimento"] = self.raca.movimento
            resumo["infravisao"] = self.raca.infravisao
            resumo["alinhamento_tendencia"] = self.raca.alinhamento
            resumo["habilidades_raca"] = [hab["nome"] for hab in self.raca.get_habilidades()]
        
        # Adiciona informações da classe
        if self.classe:
            resumo["habilidades_classe"] = [hab["nome"] for hab in self.classe.get_habilidades()]
        
        return resumo

    # <--- Alteração: Método salvar_json adicionado aqui --->
    def salvar_json(self, nome_arquivo="personagem_salvo.json"):
        """Salva a instância do personagem em um arquivo JSON usando __dict__"""
        
        # Cria uma cópia do dicionário da instância atual
        dados = self.__dict__.copy()
        
        # Precisamos converter os objetos complexos internos também para dicionários
        if self.atributos:
            dados['atributos'] = self.atributos.__dict__['atributos']
            
        if self.raca:
            # Salva o nome da classe da raça (ex: "Humano") e seus atributos
            dados_raca = self.raca.__dict__.copy()
            dados_raca['nome_raca'] = self.raca.__class__.__name__
            dados['raca'] = dados_raca
            
        if self.classe:
             # Salva o nome da classe (ex: "Guerreiro") e seus atributos
            dados_classe = self.classe.__dict__.copy()
            dados_classe['nome_classe'] = self.classe.__class__.__name__
            dados['classe'] = dados_classe

        # Salva no arquivo
        try:
            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            print(f"\n✅ Personagem salvo com sucesso em '{nome_arquivo}'!")
        except Exception as e:
            print(f"\n❌ Erro ao salvar arquivo: {e}")