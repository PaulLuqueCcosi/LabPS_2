from Cajero import Cajero
from User import User

cajero = Cajero()
if(cajero.login()):
    cajero.showMenu()