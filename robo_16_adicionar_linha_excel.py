# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:27:40 2023

@author: Matheus Almeida
"""


from openpyxl import load_workbook
import os

caminho_nome_arquivo = "C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\\DeletarLinhaColuna.xlsx"

arquivo = load_workbook(filename=caminho_nome_arquivo)

planilha_selecionada = arquivo['Professor']

dadostabela = [
    ['Nome','Idade'],
    ['Berenice',28],
    ['Caio',32],
    ['Nicole',34],
    ['Leonardo',19],
    ['Amanda',25]
]
    
for i in dadostabela:
    planilha_selecionada.append(i)
        
    
    

arquivo.save(filename=caminho_nome_arquivo)

os.startfile(caminho_nome_arquivo)