# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:27:21 2023

@author: Matheus Almeida
"""

from openpyxl import load_workbook

import os


from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera
from selenium.webdriver.common.by import By

nomecaminhoarquivo = "C:\\Users\Matheus Almeida\Desktop\Robos Python\Planilhas\dados_formulario.xlsx"
planilha_aberta = load_workbook(filename=nomecaminhoarquivo)

sheet_selecionada = planilha_aberta['Plan1']

for i in range (2,len(sheet_selecionada['A']) + 1):
    
    nome = sheet_selecionada['A%s'% i].value
    email = sheet_selecionada['B%s'% i].value
    telefone = sheet_selecionada['C%s' % i].value
    sexo = sheet_selecionada['D%s'% i].value
    sobre = sheet_selecionada['E%s'% i].value

    navegadorFormulario = opcoesSelenium.Chrome()
    navegadorFormulario.get("https://pt.surveymonkey.com/r/Y9Y6FFR")
 
    #Aguardar para o computador processar as informações
    tempoEspera.sleep(3)
 
    #Preenche Nome
    navegadorFormulario.find_element(By.NAME, "683928983").send_keys(nome)
 
    #Preenche Email
    navegadorFormulario.find_element(By.NAME, "683932318").send_keys(email)
 
    #Preenche Telefone
    navegadorFormulario.find_element(By.NAME, "683930688").send_keys(telefone)
 
    #Preenche Sobre
    navegadorFormulario.find_element(By.NAME, "683932969").send_keys(sobre)
 

    if sexo == "Masculino":

        #Preenche Radio Button Feminino
        navegadorFormulario.find_element(By.ID,"683931881_4497366118_label").click()
 
    else:
        navegadorFormulario.find_element(By.ID,"683931881_4497366119_label").click()
    
    #Aguardar para o computador processar as informações
    tempoEspera.sleep(3)
 
    #Clica para enviar as informações
    navegadorFormulario.find_element(By.XPATH,'//*[@id="patas"]/main/article/section/form/div[2]/button').click()
    
    print(nome)
    print(email)
    print(telefone)
    print(sexo)
    print(sobre)


