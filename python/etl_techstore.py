import pandas as pd
import os

def main():

      ## Tratamento de arquivo
      document_entrance = os.path.join('data', 'vendas_techstore.csv')
      document_processed = os.path.join('data', 'vendas_techstore_processed.csv')
      df = pd.read_csv(document_entrance)
      df_processed = df.copy()

      ## Verificação e tratamento de valores nulos
      print(df.isnull().sum())

      df_processed['cliente'] = df_processed['cliente'].fillna("Não informado")
      df_processed['cidade'] = df_processed['cidade'].fillna("Não informado")
      df_processed['preco_unitario'] = df_processed.groupby('produto')['preco_unitario'].transform(lambda x: x.fillna(x.median()))
      df_processed['forma_pagamento'] = df_processed['forma_pagamento'].fillna("Não informado")

      #Conversão de data
      df_processed['data_venda'] = (
            df_processed['data_venda']
            .str.replace('.', '-', regex=False)
            .str.replace('/', '-', regex=False)
      )
      df_processed['data_venda'] = pd.to_datetime(df_processed['data_venda'], errors='coerce')
      df_processed = df_processed.dropna(subset=['data_venda'])

      print(df_processed['data_venda'].isna().sum())

      #Criação coluna valor_total, colunas auxiliares ano e mês

      df_processed['valor_total'] = df_processed['quantidade'] * df_processed['preco_unitario']
      df_processed['ano'] = df_processed['data_venda'].dt.year
      df_processed['mes'] = df_processed['data_venda'].dt.month
      meses_pt = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro'
      }
      df_processed['mes'] = df_processed['mes'].map(meses_pt)

      



      df_processed.to_csv(document_processed,
                          index=False,
                          encoding='utf-8-sig')

if __name__ == "__main__":
      main()