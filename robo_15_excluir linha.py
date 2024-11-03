# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:49:11 2023

@author: Matheus Almeida
"""


from openpyxl import load_workbook
import os

caminho_nome_arquivo = "C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\\DeletarLinhaColuna.xlsx"

arquivo = load_workbook(filename=caminho_nome_arquivo)

planilha_selecionada = arquivo['Professor']

planilha_selecionada.delete_rows(3)
planilha_selecionada.delete_rows(4)

arquivo.save(filename=caminho_nome_arquivo)

os.startfile(caminho_nome_arquivo)