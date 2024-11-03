# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:32:08 2023

@author: Matheus Almeida
"""


import xlsxwriter
import os

nomecaminhoarquivo = 'C:\\Users\Matheus Almeida\Desktop\\teste.xlsx'

planilhacriada = xlsxwriter.Workbook(nomecaminhoarquivo)

planilha1 = planilhacriada.add_worksheet()

planilha1.write("A1","Nome")
planilha1.write("B1","Idade")
planilha1.write("A2","Amanda")
planilha1.write("B2",28)
planilha1.write("A3","Roberto")
planilha1.write("B3",25)



planilhacriada.close()


os.startfile(nomecaminhoarquivo)

