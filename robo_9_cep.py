# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:39:26 2023

@author: Matheus Almeida
"""


from selenium import webdriver as opcoesselenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoespera

from selenium.webdriver.common.by import By

navegador = opcoesselenium.Chrome()
navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

navegador.find_element(By.NAME,"endereco").send_keys("05892387")

navegador.find_element(By.NAME,"btn_pesquisar").click()
tempoespera.sleep(3)

rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
print(rua)


bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
print(bairro)

cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
print(cidade)


cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
print(cep)




