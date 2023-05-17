# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:46:29 2023

@author: LAB02 
"""

from Cajero import Cajero
from User import User


cajero = Cajero()
# cajero.login()
if(not cajero.login()):
    print("No login")
    exit()

cajero.showMenu()