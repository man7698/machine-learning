# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:37:51 2023

@author: Matheus Almeida
"""


from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera
 
navegadorFormulario = opcoesSelenium.Chrome()
navegadorFormulario.get("https://pt.surveymonkey.com/r/Y9Y6FFR")
 
#Aguardar para o computador processar as informações
tempoEspera.sleep(3)
 
#Preenche Nome
navegadorFormulario.find_element_by_name("683928983").send_keys("Nicole Ferreira")
 
#Preenche Email
navegadorFormulario.find_element_by_name("683932318").send_keys("nicole.ferreira@gmail.com")
 
#Preenche Telefone
navegadorFormulario.find_element_by_name("683930688").send_keys("(11) 11111 - 1111")
 
#Preenche Sobre
navegadorFormulario.find_element_by_name("683932969").send_keys("Sei automatizar processos e planilhas com Python")
 
 
#Preenche Radio Button Feminino
navegadorFormulario.find_element_by_id("683931881_4497366119_label").click()
 
#Aguardar para o computador processar as informações
tempoEspera.sleep(6)
 
#Clica para enviar as informações
navegadorFormulario.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button').click()
