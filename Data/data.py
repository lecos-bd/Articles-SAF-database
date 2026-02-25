import pandas as pd
import os

# Caminho dinâmico para o Excel na raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, '..', 'artigos.xlsx')

def carregar_dados():
    return pd.read_excel(EXCEL_PATH)

def consultar_artigos(termo):
    df = carregar_dados()
    # Filtro simples por título
    resultado = df[df['titulo'].str.contains(termo, case=False, na=False)]
    return resultado.to_dict(orient='records')