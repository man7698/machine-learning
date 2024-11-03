# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:36:04 2023

@author: Matheus Almeida
"""


import smtplib

try:
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)


    servidor_email.starttls()


    servidor_email.login('matheusalmeida7698@gmail.com','hfmbcfadoghaoyip')

    remetente = 'matheusalmeida7698@gmail.com'

    destinatarios = 'matheusalmeida7698@gmail.com'

    conteudo = 'Email de teste'

    servidor_email.sendmail(remetente, destinatarios, conteudo)

   
    
except Exception as e:
    print("Erro ao enviar email",e)

finally:
     servidor_email.quit()




