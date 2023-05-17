# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023

@author: LAB02 
"""

from Cajero import Cajero
from User import User
from DATA import data
# data = {
#   "Paquito": {
#     "pass": "1225",
#     "monto": 8952.51
#   },
#     "Yei": {
#     "pass": "5789",
#     "monto": 9152.50
#   },
#     "karitos": {
#     "pass": "7894",
#     "monto": 9999.50
#   },
#   }





cajero = Cajero()
# cajero.login()
if(not cajero.login()):
    print("No login")
    exit()

cajero.showMenu()