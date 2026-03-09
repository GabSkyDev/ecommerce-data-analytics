import sys
import os

sys.path.append(os.path.abspath(".."))

from src.data_cleaning import data_cleaning
import pandas as pd
import numpy as np

def top_10_products(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Nome_Produto')['Faturamento'].sum().sort_values(ascending=False).head(10)

def faturamento_mensal(df: pd.DataFrame) -> pd.Series:
    # Cria coluna mês se não existir
    if 'Mes' not in df.columns:
        df = df.copy()
        df['Mes'] = df['Data_Pedido'].dt.to_period('M')

    return df.groupby('Mes')['Faturamento'].sum()

def faturamento_por_estado(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Estado')['Faturamento'].sum().sort_values(ascending=False)

def faturamento_por_categoria(df: pd.DataFrame) -> pd.Series:
    return df.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

def save_analysis(df: pd.DataFrame, output_dir: str = "../reports") -> None:
    # Cria diretório se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Executa análises
    top_produtos = top_10_products(df)
    fat_mensal = faturamento_mensal(df)
    fat_estado = faturamento_por_estado(df)
    fat_categoria = faturamento_por_categoria(df)

    # Salva CSVs
    top_produtos.to_csv(f"{output_dir}/top_10_produtos.csv", header=['Faturamento'])
    fat_mensal.to_csv(f"{output_dir}/faturamento_mensal.csv", header=['Faturamento'])
    fat_estado.to_csv(f"{output_dir}/faturamento_por_estado.csv", header=['Faturamento'])
    fat_categoria.to_csv(f"{output_dir}/faturamento_por_categoria.csv", header=['Faturamento'])

    print(f"Análises salvas em {output_dir}/")
    print("Arquivos gerados:")
    print("   - top_10_produtos.csv")
    print("   - faturamento_mensal.csv")
    print("   - faturamento_por_estado.csv")
    print("   - faturamento_por_categoria.csv")

