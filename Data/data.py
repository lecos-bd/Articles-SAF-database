import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

def get_DOI(df):
    return df['DI'].unique()

def get_ano(df):
    return df['PY'].unique()

def get_journal(df):
    return df['JO'].unique()

def get_title(df):
    return df['TI'].unique()

def get_abstract(df):
    return df['AB'].unique()

def get_keywords(df):
    return df['DE'].unique()

def get_citations(df):
    return df['TC'].unique()

def get_references(df):
    return df['CR'].unique()

def get_authors(df):
    return df['AU'].unique()

def get_affiliations(df):
    return df['AF'].unique()

def get_bd(df):
    return df['BD'].unique()

def get_source(df):
    return df['SO'].unique()

def get_escopo(df):
    return df['COMBINACAO_EIXOS']

if __name__ == "__main__":
    df = load_data("Todos os Artigos.xlsx")