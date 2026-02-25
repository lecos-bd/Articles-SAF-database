import pandas as pd
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(DATA_DIR, 'Todos os Artigos.xlsx')

def carregar_dataframe():
    if not os.path.exists(EXCEL_PATH):
        return None
    return pd.read_excel(EXCEL_PATH)

def obter_valores_unicos():
    """Retorna valores únicos apenas para as colunas de filtro solicitadas."""
    df = carregar_dataframe()
    if df is None: return {}

    colunas_filtro = ['COMBINACAO_EIXOS', 'PY']
    valores_unicos = {}
    
    for col in colunas_filtro:
        if col in df.columns:
            valores = df[col].dropna().unique().tolist()
            valores.sort()
            valores_unicos[col] = valores
        else:
            valores_unicos[col] = []
    return valores_unicos

def consultar_artigos_filtrados(filtros):
    df = carregar_dataframe()
    if df is None: return []

    # Aplicação dos filtros dinâmicos
    for coluna, valor in filtros.items():
        if valor:
            df = df[df[coluna].astype(str) == str(valor)]

    # 1. Lista de colunas para remover (ajuste os nomes se houver variação no Excel)
    colunas_para_remover = ['EIXO_AMBIENTAL', 'EIXO_ECONOMICO', 'EIXO_SOCIAL', 'N_EIXOS']
    df = df.drop(columns=[c for c in colunas_para_remover if c in df.columns])

    # 2. Reorganizar para que TI e DI sejam os primeiros
    cols = list(df.columns)
    if 'TI' in cols: cols.insert(0, cols.pop(cols.index('TI')))
    if 'DI' in cols: cols.insert(1, cols.pop(cols.index('DI')))
    
    df = df[cols]

    return df.to_dict(orient='records')