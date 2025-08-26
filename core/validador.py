from typing import List, Tuple
from models.personagem import Personagem

class ValidadorPersonagem:
    """Classe responsável por validar as regras de criação de personagem"""
    
    @staticmethod
    def validar_atributos_minimos(personagem: Personagem) -> Tuple[bool, List[str]]:
        """Valida se os atributos estão dentro dos limites permitidos"""
        erros = []
        atributos = personagem.atributos.obter_todos_atributos()
        
        for nome, valor in atributos.items():
            if valor < 3:
                erros.append(f"{nome} não pode ser menor que 3 (atual: {valor})")
            elif valor > 18:
                erros.append(f"{nome} não pode ser maior que 18 (atual: {valor})")
        
        return len(erros) == 0, erros
    
    @staticmethod
    def validar_combinacao_raca_classe(personagem: Personagem) -> Tuple[bool, List[str]]:
        """Valida se a combinação de raça e classe é permitida"""
        erros = []
        
        if not personagem.raca:
            erros.append("Personagem deve ter uma raça")
            return False, erros
        
        if not personagem.classe:
            erros.append("Personagem deve ter uma classe")
            return False, erros
        
        # Verifica se a raça pode ser da classe escolhida
        racas_permitidas = personagem.classe.get_racas_permitidas()
        if racas_permitidas is not None:
            nome_raca = personagem.raca.__class__.__name__
            if nome_raca not in racas_permitidas:
                erros.append(f"Raça {nome_raca} não pode ser da classe {personagem.classe.__class__.__name__}")
        
        return len(erros) == 0, erros
    
    @staticmethod
    def validar_requisitos_classe(personagem: Personagem) -> Tuple[bool, List[str]]:
        """Valida se o personagem atende aos requisitos da classe"""
        erros = []
        
        if not personagem.classe:
            erros.append("Personagem deve ter uma classe")
            return False, erros
        
        pode_ser, mensagem = personagem.pode_ser_classe(personagem.classe)
        if not pode_ser:
            erros.append(mensagem)
        
        return len(erros) == 0, erros
    
    @staticmethod
    def validar_alinhamento_druida(personagem: Personagem) -> Tuple[bool, List[str]]:
        """Valida restrições específicas do druida"""
        erros = []
        
        if personagem.classe and personagem.classe.__class__.__name__ == "Druida":
            # Druidas devem ser neutros - isso seria implementado se tivéssemos sistema de alinhamento
            # Por agora, apenas uma validação conceitual
            pass
        
        return len(erros) == 0, erros
    
    @staticmethod
    def validar_personagem_completo(personagem: Personagem) -> Tuple[bool, List[str]]:
        """Executa todas as validações do personagem"""
        todos_erros = []
        
        # Validar atributos
        valido, erros = ValidadorPersonagem.validar_atributos_minimos(personagem)
        todos_erros.extend(erros)
        
        # Validar combinação raça/classe
        valido, erros = ValidadorPersonagem.validar_combinacao_raca_classe(personagem)
        todos_erros.extend(erros)
        
        # Validar requisitos da classe
        valido, erros = ValidadorPersonagem.validar_requisitos_classe(personagem)
        todos_erros.extend(erros)
        
        # Validações específicas
        valido, erros = ValidadorPersonagem.validar_alinhamento_druida(personagem)
        todos_erros.extend(erros)
        
        return len(todos_erros) == 0, todos_erros
    
    @staticmethod
    def sugerir_classes_viaveis(personagem: Personagem) -> List[str]:
        """Sugere classes que o personagem pode escolher baseado nos atributos"""
        from classes.guerreiro import Guerreiro
        from classes.clerigo import Clerigo
        from classes.druida import Druida
        
        classes_disponiveis = [Guerreiro(), Clerigo(), Druida()]
        classes_viaveis = []
        
        for classe in classes_disponiveis:
            pode_ser, _ = personagem.pode_ser_classe(classe)
            if pode_ser:
                classes_viaveis.append(classe.__class__.__name__)
        
        return classes_viaveis
    
    @staticmethod
    def calcular_pontuacao_atributos(personagem: Personagem) -> dict:
        """Calcula pontuações derivadas dos atributos"""
        atributos = personagem.atributos.obter_todos_atributos()
        
        return {
            "soma_total": sum(atributos.values()),
            "media": round(sum(atributos.values()) / len(atributos), 1),
            "maior_atributo": max(atributos.values()),
            "menor_atributo": min(atributos.values()),
            "atributos_acima_15": sum(1 for v in atributos.values() if v >= 15),
            "atributos_abaixo_8": sum(1 for v in atributos.values() if v <= 8)
        }