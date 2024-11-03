# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:17:53 2023

@author: Matheus Almeida
"""

import robo_9_cep as cep
from openpyxl import load_workbook
import os


nome_arquivo_cep = "C:\\Users\Matheus Almeida\Desktop\\pesquisa_endereco2.xlsx"
planilhadadosendereco = load_workbook(nome_arquivo_cep)

sheet_selecionada = planilhadadosendereco["Dados"]

linha = len(sheet_selecionada['A']) + 1

colunaA = "A" + str(linha)
colunaB = "B" + str(linha)
colunaC = "C" + str(linha)
colunaD = "D" + str(linha)


sheet_selecionada[colunaA] = cep.rua
sheet_selecionada[colunaB] = cep.bairro
sheet_selecionada[colunaC] = cep.cidade
sheet_selecionada[colunaD] = cep.cep

planilhadadosendereco.save(filename=nome_arquivo_cep)

os.startfile(nome_arquivo_cep)



















