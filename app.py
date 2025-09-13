"""
Aplicação Web com Flask para o Sistema de Criação de Personagens - Old Dragon RPG

Este script serve como a interface web para o gerador de personagens,
substituindo a interação via linha de comando por uma página HTML interativa.

Funcionalidades:
- Tela inicial com formulário para escolher nome, estilo, raça e classe.
- Processa a seleção do usuário e redireciona para uma nova página.
- Exibe a ficha completa do personagem gerado em uma tela dedicada.

Autor: Sistema Old Dragon (Adaptação para Web)
Versão: 3.2
"""
from flask import Flask, render_template, request, redirect, url_for, session

# Importa as classes principais do seu projeto.
from core.gerador_personagem import GeradorPersonagem
from models.personagem import Personagem
from models.atributos import Atributos

# Inicializa a aplicação Flask
app = Flask(__name__)
# Uma 'secret_key' é necessária para usar o objeto 'session' do Flask,
# que armazena os dados do personagem entre as requisições.
app.secret_key = 'uma-chave-secreta-muito-segura-para-o-projeto-rpg'

# Cria uma instância global do gerador para ter acesso às listas de estilos, raças e classes.
try:
    gerador = GeradorPersonagem()
except Exception as e:
    print(f"ERRO: Falha ao inicializar o GeradorPersonagem. Verifique os arquivos do projeto. Erro: {e}")
    gerador = None

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Rota principal que renderiza o formulário de criação.
    Se a requisição for POST, gera o personagem, armazena na sessão e redireciona.
    """
    if not gerador:
        return "<h1>Erro Crítico</h1><p>Não foi possível carregar as classes do gerador de personagens.</p>", 500

    if request.method == 'POST':
        try:
            nome_personagem = request.form.get('nome', 'Aventureiro(a)')
            estilo_key = request.form.get('estilo')
            raca_key = request.form.get('raca')
            classe_key = request.form.get('classe')

            estilo_obj = gerador.estilos.get(estilo_key)
            raca_obj = gerador.racas.get(raca_key)
            classe_obj = gerador.classes.get(classe_key)

            if estilo_obj and raca_obj and classe_obj:
                atributos = Atributos()
                valores_gerados = estilo_obj.gerar_valores()

                # Lógica adaptada para a web: estilos que antes pediam input do usuário
                # agora são tratados de forma automática.
                if estilo_key in ["2", "3"]: # Aventureiro e Heroico
                    # Ordena os valores do maior para o menor para uma distribuição otimizada.
                    valores_gerados.sort(reverse=True)
                    for i, nome_attr in enumerate(Atributos.NOMES_ATRIBUTOS):
                        atributos.definir_atributo(nome_attr, valores_gerados[i])
                else: # Clássico
                    # Usa o método original que não precisa de interação.
                    estilo_obj.aplicar_valores(atributos, valores_gerados)

                personagem_final = Personagem(
                    nome=nome_personagem,
                    atributos=atributos,
                    raca=raca_obj,
                    classe=classe_obj
                )

                # Armazena o resumo do personagem na sessão do usuário
                session['character'] = personagem_final.obter_resumo()

                # Redireciona o usuário para a nova página da ficha de personagem
                return redirect(url_for('exibir'))

        except Exception as e:
            print(f"Ocorreu um erro durante a geração do personagem: {e}")
            # Em caso de erro, apenas recarrega a página principal.
            return redirect(url_for('home'))

    # Se for uma requisição GET, apenas mostra o formulário de criação.
    return render_template('index.html',
                           estilos=gerador.estilos,
                           racas=gerador.racas,
                           classes=gerador.classes)

@app.route('/character-sheet')
def exibir():
    """
    Esta nova rota exibe a ficha do personagem que foi armazenada na sessão.
    """
    # Recupera os dados do personagem da sessão.
    personagem = session.get('character', None)

    # Se não houver personagem na sessão (ex: usuário acessou a URL direto),
    # redireciona de volta para a página inicial.
    if not personagem:
        return redirect(url_for('home'))

    return render_template('exibir.html', personagem=personagem)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

