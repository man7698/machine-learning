# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:29:51 2023

@author: Matheus Almeida
"""


import xlsxwriter as opcoesdoxlswriter

import os

nomecaminhoarquivo = 'C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\pintafundoefonte.xlsx'

workbook = opcoesdoxlswriter.Workbook(nomecaminhoarquivo)

sheetpadrao = workbook.add_worksheet("Dados")

corfundo = workbook.add_format({'fg_color':'yellow'})
corfonte = workbook.add_format()
corfonte.set_font_color('blue')




sheetpadrao.write("A1","Nome",corfundo)
sheetpadrao.write("B1","Idade",corfundo)
sheetpadrao.write("A2","Amanda")
sheetpadrao.write("B2",21)
sheetpadrao.write("A3","Alan")
sheetpadrao.write("B3",28)

workbook.close()

os.startfile(nomecaminhoarquivo)
