# 📊 E-commerce Data Analytics
Transformando dados de vendas brutos em insights acionáveis para decisões estratégicas de negócio.

## 📌 Visão Geral
Este projeto tem como objetivo analisar os dados de vendas de uma loja de e-commerce para gerar insights valiosos para as decisões de estoque, marketing, crescimento e planejamento estratégico.
O repositório contém:
- Notebooks com análises exploratórias e geração de insights;
- Scripts Python para limpeza, transformação e análise;
- Pipeline de processamento dos dados;
- Data sets brutos de exemplo.

## 🛠️ Tecnologias Utilizadas
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

## 🗂️ Estrutura do repositório
```text
ecommerce-data-analytics/
│
├── data/                      # Dados brutos e intermediários
├── notebooks/                 # Notebooks de análise exploratória e geração de insights
│   ├── 01_data_analysis.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_business_insights.ipynb
├── src/                      # Scripts de análise e pipeline
│   ├── analysis.py          # Funções de análise
│   ├── data_cleaning.py      # Limpeza e preparo dos dados
│   └── pipeline.py           # Função/coordenador de fluxo de dados
├── requirements.txt          # Dependências do projeto
└── .gitignore
```

## 🧾 Instalação e Uso
### 1. Clone o repositório:
```bash
git clone https://github.com/GabSkyDev/ecommerce-data-analytics.git
cd ecommerce-data-analytics
```

### 2. Crie e ative um ambiente Python:
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

### 3. Instale dependências:
```bash
pip install -r requirements.txt
```
### 4. Execute os notebooks ou scripts conforme necessidade.

## 🎯 Definição do Problema de Negócio
### 1.1 O Problema
Uma loja de e-commerce está crescendo rapidamente, gerando um volume grande de dados de vendas que, em seu estado bruto, não entrega conhecimento pronto para uso. Aspectos críticos que impactam o negócio:
- Gestão de estoque ineficiente: dificuldade em identificar produtos que vendem bem vs produtos que ficam parados.
- Marketing com baixo retorno: campanhas genéricas por falta de segmentação por categorias e regiões.
- Perda de oportunidades sazonais: sem visão clara de tendências ao longo do tempo.
- Expansão sem direção: falta de insights para identificar mercados mais promissores.
- Essas lacunas fazem com que as decisões estratégicas sejam baseadas em intuição, ao invés de dados concretos.

### 1.2 Objetivos do Projeto
Este projeto de análise de dados foi concebido para responder perguntas de negócio essenciais:
- O que vender? – Identificar produtos de maior sucesso.
- Onde focar? – Quais categorias e regiões geram mais receita.
- Quando agir? – Tendências de vendas ao longo do tempo.
- Para onde expandir? – Onde nosso público tem maior presença.

### 1.3 Solução Proposta
Consolidar, limpar e analisar os dados históricos de vendas usando Python e bibliotecas como Pandas, NumPy e Matplotlib, gerando um relatório visual com insights claros para equipes de gestão, marketing e operações.

### 1.4 Resultados Esperados
Ao final do projeto espera-se:
- Otimização de estoque: reduzir custos e evitar falta de itens.
- Marketing mais eficaz: campanhas baseadas em categorias e regiões lucrativas.
- Planejamento estratégico: planejamento baseado em padrões de sazonalidade.
- Cultura orientada a dados: substituindo decisões por intuição por análises concretas.

## 💡 Soluções
| Arquivo / Notebook                     | Função / Descrição                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| `notebooks/01_data_analysis.ipynb`     | Análise exploratória dos dados, gráficos de distribuição, tendências temporais.      |
| `notebooks/02_data_cleaning.ipynb`     | Limpeza e preparação dos dados, tratamento de valores faltantes, padronização.       |
| `notebooks/03_business_insights.ipynb` | Análises aplicadas para gerar insights, ranking de produtos, sazonalidade e regiões. |
| `src/data_cleaning.py`                 | Funções reutilizáveis de limpeza e transformação dos dados brutos.                   |
| `src/analysis.py`                      | Funções de análise específicas, como segmentação por categoria ou região.            |
| `src/pipeline.py`                      | Coordenação do fluxo de dados: execução sequencial de limpeza e análises.            |
| `data/`                                | Armazenamento de datasets brutos e intermediários.                                   |
