import sys
import os
from flask import Flask, render_template, request

# Ajuste para importar de pastas diferentes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Data import data
import plot  # plot.py está na mesma pasta (App)

# Indicamos ao Flask onde está a pasta Templates e os arquivos estáticos
app = Flask(__name__, template_folder="../Templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultados = []
    grafico_html = ""
    
    if request.method == 'POST':
        termo = request.form.get('busca')
        # Busca os dados usando o módulo na pasta Data
        resultados = data.consultar_artigos(termo)
        
        # Opcional: Gerar gráfico
        # import pandas as pd
        # grafico_html = plot.gerar_grafico_ano(pd.DataFrame(resultados))

    return render_template('index.html', artigos=resultados, grafico=grafico_html)

if __name__ == '__main__':
    app.run(debug=True)