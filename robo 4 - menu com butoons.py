# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:17:12 2023

@author: Matheus Almeida
"""

import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique no botão desejado',buttons = ['Excel','Word','Notepad'])


if opcao == "Excel":
    escolha_opcao.hotkey('win', 'r')
    
    escolha_opcao.sleep(0.3)
    
    escolha_opcao.typewrite('Excel')
    
    escolha_opcao.press('enter')
    
elif opcao == "Word":

    print("Escolheu Word")
    escolha_opcao.hotkey('win', 'r')
    
    escolha_opcao.sleep(0.3)
    
    escolha_opcao.typewrite('winWord')
    
    escolha_opcao.press('enter')
    
elif opcao == "Notepad":
    print("Escolheu Notepad")
    escolha_opcao.hotkey('win', 'r')
    
    escolha_opcao.sleep(0.3)
    
    escolha_opcao.typewrite('Notepad')
    
    escolha_opcao.press('enter')
    
    
    