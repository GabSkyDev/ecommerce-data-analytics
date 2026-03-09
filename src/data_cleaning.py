import pandas as pd

def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Correção no tipo na coluna 'Data_Pedido' para datetime para análise temporal
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'])

    # Criação de coluna de 'Faturamento' ('Preco_Unitario' x 'Quantidade')
    df['Faturamento'] = df['Preco_Unitario'] * df['Quantidade']

    # Criação de coluna 'Tipo_Entrega' para indicar velocidade de entrega com base no Estado
    df['Tipo_Entrega'] = df['Estado'].apply(lambda status: 'Rápida' if status in ['SP', 'RJ', 'MG'] else 'Normal')

    return df