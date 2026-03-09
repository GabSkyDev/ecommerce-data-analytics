#!/usr/bin/env python3
"""
Pipeline de Dados - E-commerce Analytics

Este script executa toda a pipeline de dados:
1. Carrega os dados brutos
2. Aplica limpeza e transformação
3. Executa análises de negócio
4. Salva resultados em CSVs para Power BI

Uso:
    python src/pipeline.py
"""

import sys
import os
import pandas as pd

# Adiciona o diretório raiz ao path para importar módulos locais
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_cleaning import data_cleaning
from src.analysis import save_analysis

def main():
    """Função principal da pipeline."""
    print("Iniciando pipeline de dados e-commerce...")

    # Define diretório base (raiz do projeto)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Caminhos dos arquivos usando paths absolutos para evitar erros de cwd
    data_path = os.path.join(base_dir, "data", "data.csv")
    reports_dir = os.path.join(base_dir, "reports")

    try:
        # 1. Carrega dados brutos
        print("Carregando dados brutos...")
        df_raw = pd.read_csv(data_path)
        print(f"Dados carregados: {len(df_raw)} linhas")

        # 2. Aplica limpeza e transformação
        print("Aplicando limpeza e transformação...")
        df_clean = data_cleaning(df_raw)
        print(f"Dados limpos: {len(df_clean)} linhas")
        print(f"Colunas: {list(df_clean.columns)}")

        # Salva dados limpos para referência futura
        cleaned_data_path = os.path.join(base_dir, "data", "cleaned_data.csv")
        df_clean.to_csv(cleaned_data_path, index=False)
        print(f"Dados limpos salvos em: {cleaned_data_path}")

        # 3. Executa análises e salva CSVs
        print("Executando análises de negócio...")
        save_analysis(df_clean, reports_dir)

        print("\nPipeline concluída com sucesso!")
        print(f"Dados prontos para Power BI em: {reports_dir}/")

    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado - {e}")
        print("Verifique se o arquivo data.csv existe em ../data/")
        sys.exit(1)
    except Exception as e:
        print(f"Erro na pipeline: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()