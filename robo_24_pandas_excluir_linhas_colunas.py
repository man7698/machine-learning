
import pandas as pd


df_dados = pd.read_excel("C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\Deletar_Linhas_Colunas.xlsx")

#excluir linhas que tem pelo menos um valor em branco
df_dados.dropna()

#exclui coluna especifica
del df_dados["Produto"]

#excluir linha especifica
#axis - 1 - coluna , 0 - linha
df_dados.drop(2,axis = 0)



display(df_dados)