import os
import sys
from flask import Flask, render_template, request

# Configuração de caminhos (mantendo sua estrutura)
APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(APP_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR)

from Data import data

@app.route('/', methods=['GET', 'POST'])
def index():
    opcoes_filtros = data.obter_valores_unicos()
    resultados = None # Iniciamos como None para diferenciar "página limpa" de "nenhum resultado"
    erro_validacao = False

    if request.method == 'POST':
        # Captura os filtros ignorando campos vazios
        filtros_selecionados = {col: request.form.get(col) for col in opcoes_filtros.keys() if request.form.get(col)}
        
        # Validação: Pelo menos um filtro deve estar preenchido
        if filtros_selecionados:
            resultados = data.consultar_artigos_filtrados(filtros_selecionados)
        else:
            erro_validacao = True # Ativa o aviso de que é necessário selecionar algo
            
    return render_template('index.html', filtros=opcoes_filtros, artigos=resultados, erro=erro_validacao)


if __name__ == '__main__':
    app.run(debug=True)