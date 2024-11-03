# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:47:20 2023

@author: Matheus Almeida
Robo 1
"""
import pyautogui as posicaomouse

posicaomouse.sleep(2)


posicaomouse.moveTo(x=20, y=750)
posicaomouse.click(x=20, y=750)

posicaomouse.sleep(2)

print(posicaomouse.position())
posicaomouse.click(x=186, y=507)