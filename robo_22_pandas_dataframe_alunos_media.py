import pandas as opcoespandas
import numpy as opcoesnumpy



df_notasaluno = opcoespandas.DataFrame(
    {
     "Nome":["Ana","Pedro","João"],
     "Nota1":[9,7,10],
     "Nota2":[6,9,8],
     "Nota3":[7,5,10],
     "Nota4":[10,10,6]
     
     }
    )

#Adiciona nova coluna
df_notasaluno["Media"] = (df_notasaluno["Nota1"] + df_notasaluno["Nota2"] + df_notasaluno["Nota3"] +
 df_notasaluno["Nota4"])/4

#Excluir coluna
#df_notasaluno = df_notasaluno.drop(columns=[5])

display(df_notasaluno)