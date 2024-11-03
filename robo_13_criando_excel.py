# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:14:28 2023

@author: Matheus Almeida
"""


import xlsxwriter as opcoesdoxlswriter

import os

nomecaminhoarquivo = 'C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\primeiroexemplo.xlsx'

workbook = opcoesdoxlswriter.Workbook(nomecaminhoarquivo)

sheetpadrao = workbook.add_worksheet()

sheetpadrao.write("A1","Nome")
sheetpadrao.write("B1","Idade")
sheetpadrao.write("A2","Amanda")
sheetpadrao.write("B2",21)
sheetpadrao.write("A3","Alan")
sheetpadrao.write("B3",28)

workbook.close()

os.startfile(nomecaminhoarquivo)


