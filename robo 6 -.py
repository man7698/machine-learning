# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:06:30 2023

@author: Matheus Almeida
"""


from selenium import webdriver as opcoes_selenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempopausacomputador
import pyautogui as teclasatalho

from selenium.webdriver.common.by import By

meunavegador = opcoes_selenium.Chrome()
meunavegador.get("https://www.google.com.br/")

tempopausacomputador.sleep(0.6)

meunavegador.find_element(By.NAME,"q").send_keys("Dolar Hoje")

tempopausacomputador.sleep(0.6)

meunavegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)

tempopausacomputador.sleep(0.6)

valordolar = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
tempopausacomputador.sleep(0.6)

print(valordolar)



##############################################

meunavegador.find_element(By.NAME,"q").send_keys("")

teclasatalho.press('tab')

teclasatalho.press('enter')


tempopausacomputador.sleep(0.6)

meunavegador.find_element(By.NAME,"q").send_keys("Euro Hoje")

tempopausacomputador.sleep(0.6)

meunavegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)

tempopausacomputador.sleep(0.6)

valoreuro = meunavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
tempopausacomputador.sleep(0.6)

print(valoreuro)


