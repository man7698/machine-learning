# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:45:24 2023

@author: Matheus Almeida
"""
import pyautogui as posicaoabrirarquivos

posicaoabrirarquivos.hotkey('win', 'r')

posicaoabrirarquivos.sleep(2)

posicaoabrirarquivos.typewrite('notepad')

posicaoabrirarquivos.sleep(2)

posicaoabrirarquivos.press('enter')

posicaoabrirarquivos.sleep(2)

posicaoabrirarquivos.typewrite('abrimos notepad')

fecharjanela = posicaoabrirarquivos.getActiveWindow()

fecharjanela.close()

posicaoabrirarquivos.sleep(2)

posicaoabrirarquivos.press('tab')

posicaoabrirarquivos.sleep(2)

posicaoabrirarquivos.press('enter')



