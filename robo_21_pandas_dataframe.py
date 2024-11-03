import pandas as opcoespandas
import numpy as opcoesnumpy

df_datas = opcoespandas.date_range("20221201",periods=31)

print(df_datas)



df_datas_meses = opcoespandas.date_range("20221231",periods=12,freq="M")
print(df_datas_meses)



df_numerosaleatorios = opcoespandas.DataFrame(opcoesnumpy.random.rand(5,1))
print(df_numerosaleatorios)



df_notasalunos = opcoespandas.DataFrame(
    {
     
     "Nome": ["Ana","Pedro","João"],
     "Media":[9,7,10]
      
     }
    ) 
print(df_notasalunos)



