from Cajero import Cajero
from User import User

cajero = Cajero()
if(not cajero.login()):
    print("No login")
    exit()

cajero.showMenu()