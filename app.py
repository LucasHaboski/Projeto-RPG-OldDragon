# app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash

# Importa as classes principais do seu projeto.
from core.gerador_personagem import GeradorPersonagem
from models.personagem import Personagem
from models.atributos import Atributos

# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'key'

# Cria uma instância global do gerador
try:
    gerador = GeradorPersonagem()
except Exception as e:
    print(f"ERRO: Falha ao inicializar o GeradorPersonagem. Erro: {e}")
    gerador = None

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Rota principal. GET: mostra o formulário.
    POST: processa a criação inicial e redireciona para a distribuição ou para a ficha final.
    """
    if not gerador:
        return "<h1>Erro Crítico</h1><p>Não foi possível carregar as classes do gerador.</p>", 500

    if request.method == 'POST':
        # Salva os dados do formulário em uma variável de sessão temporária
        session['temp_character'] = {
            'nome': request.form.get('nome', 'Aventureiro(a)'),
            'estilo_key': request.form.get('estilo'),
            'raca_key': request.form.get('raca'),
            'classe_key': request.form.get('classe')
        }
        
        estilo_key = session['temp_character']['estilo_key']
        estilo_obj = gerador.estilos.get(estilo_key)

        if not estilo_obj:
            flash("Estilo de geração inválido.", "error")
            return redirect(url_for('home'))

        # Gera os valores dos atributos
        valores_gerados = estilo_obj.gerar_valores()
        session['valores_gerados'] = valores_gerados

        # Se o estilo for Clássico, cria o personagem diretamente
        if estilo_key == "1": # Supondo que '1' é a key para EstiloClassico
            atributos = Atributos()
            estilo_obj.aplicar_valores(atributos, valores_gerados)
            
            # Reúne tudo para criar o personagem final
            raca_obj = gerador.racas.get(session['temp_character']['raca_key'])
            classe_obj = gerador.classes.get(session['temp_character']['classe_key'])

            personagem_final = Personagem(
                nome=session['temp_character']['nome'],
                atributos=atributos,
                raca=raca_obj,
                classe=classe_obj
            )
            session['character'] = personagem_final.obter_resumo()
            # Limpa os dados temporários
            session.pop('temp_character', None)
            session.pop('valores_gerados', None)
            return redirect(url_for('exibir'))
        else:
            # Para Aventureiro e Heroico, redireciona para a página de distribuição
            return redirect(url_for('distribuir_atributos'))

    return render_template('index.html',
                           estilos=gerador.estilos,
                           racas=gerador.racas,
                           classes=gerador.classes)

@app.route('/distribuir-atributos', methods=['GET', 'POST'])
def distribuir_atributos():
    """
    Nova rota para permitir que o usuário distribua os atributos rolados.
    """
    # Se o usuário tentar acessar essa página sem dados, redireciona para o início
    if 'temp_character' not in session or 'valores_gerados' not in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        try:
            atributos = Atributos()
            valores_usados = []
            
            # Pega os valores do formulário e atribui
            for nome_attr in Atributos.NOMES_ATRIBUTOS:
                valor = int(request.form.get(nome_attr))
                atributos.definir_atributo(nome_attr, valor)
                valores_usados.append(valor)
            
            # Validação: verifica se o usuário usou os valores corretos
            if sorted(valores_usados) != sorted(session['valores_gerados']):
                # Se algo der errado (ex: usuário manipulou o HTML), retorna com erro
                flash("Houve um erro na distribuição dos atributos. Tente novamente.", "error")
                return redirect(url_for('distribuir_atributos'))

            # Monta o personagem final
            char_data = session['temp_character']
            raca_obj = gerador.racas.get(char_data['raca_key'])
            classe_obj = gerador.classes.get(char_data['classe_key'])

            personagem_final = Personagem(
                nome=char_data['nome'],
                atributos=atributos,
                raca=raca_obj,
                classe=classe_obj
            )
            session['character'] = personagem_final.obter_resumo()

            # Limpa os dados temporários da sessão
            session.pop('temp_character', None)
            session.pop('valores_gerados', None)

            return redirect(url_for('exibir'))
        except Exception as e:
            print(f"Erro ao finalizar personagem: {e}")
            flash("Ocorreu um erro inesperado ao finalizar o personagem.", "error")
            return redirect(url_for('home'))

    # Se a requisição for GET, apenas exibe a página de distribuição
    return render_template('distribuir.html',
                           valores_gerados=session['valores_gerados'],
                           atributos_nomes=Atributos.NOMES_ATRIBUTOS)

@app.route('/character-sheet')
def exibir():
    """
    Exibe a ficha do personagem que foi armazenada na sessão.
    """
    personagem = session.get('character', None)
    if not personagem:
        return redirect(url_for('home'))
    return render_template('exibir.html', personagem=personagem)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)