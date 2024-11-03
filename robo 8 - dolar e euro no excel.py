# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:18:11 2023

@author: Matheus Almeida
"""

import robo_6_euroedolar as eurodolar
import xlsxwriter
import os
import pyautogui as tempopausacomputador

tempopausacomputador.sleep(6)

dolar = eurodolar.valordolar
euro = eurodolar.valoreuro

import xlsxwriter
import os

tempopausacomputador.sleep(6)
nomecaminhoarquivo = 'C:\\Users\Matheus Almeida\Desktop\\teste.xlsx'

tempopausacomputador.sleep(6)
planilhacriada = xlsxwriter.Workbook(nomecaminhoarquivo)

tempopausacomputador.sleep(6)
planilha1 = planilhacriada.add_worksheet()

tempopausacomputador.sleep(6)
planilha1.write("A1","Dolar")
planilha1.write("B1","Euro")
planilha1.write("A2",dolar)
planilha1.write("B2",euro)





planilhacriada.close()


os.startfile(nomecaminhoarquivo)
