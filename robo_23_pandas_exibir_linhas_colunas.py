

import pandas as pd

#Caminho do arquivo
df_vendas = pd.read_excel("C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\\Vendas_Jan.xlsx")

#mostra dataframe
display(df_vendas)

#mostra quantidade de linhas no df
display(df_vendas.index)

#mostra quantidade de colunas no df
display(df_vendas.columns)


#mostra quantidade de linhas determinadas
display(df_vendas.head(6))

#mostra quantidade de ultimas linhas
display(df_vendas.tail(6))

#mostra coluna especifica
display(df_vendas["Vendedor"].head())



#localiza e limita a quantidade de linha
display(df_vendas.loc[1:5])


df_vendas_leonardo = df_vendas.loc[df_vendas["Vendedor"] == "Leonardo Almeida"]

display(df_vendas_leonardo)




