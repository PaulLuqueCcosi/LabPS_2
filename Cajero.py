from User import User
import MENSAJES
class Cajero:   
  
    def __init__(self):
        self.user = None
        self.isLogin = False
        self.maxNnumberAttemps = 3
        self.maximoMontoDeposito = 3000
        self.maximoMontoRetiro = 3000
        self.topeDeposito = False

    def inputAmount (self, operation):
        amount = None
        try:
            amount = float(input(f'Ingrese el monto a {operation}: '))
            if(amount <= 0):
                print(MENSAJES.ERROR_MONTO_NEGATIVO)
                amount = None
        except ValueError:
            print(MENSAJES.ERROR_VALOR_NO_NUMERICO)

        return amount

        
    def login(self):
        numAttemp = 1
        while(numAttemp <= self.maxNnumberAttemps):
            userName = input("Username: ")
            password = input("Password: ")

            user = User.searchUser(userName, password)
                
            # ERROR
            if(user == None):
                print(MENSAJES.ERROR_USUARIO_PASSWORD_NO_ENCONTRADO)
                print(f"Le quedan {self.maxNnumberAttemps - numAttemp} intentos") 
                numAttemp += 1
            else:
                # susario correcto
                self.user = user
                self.isLogin = True
                break
                
        if(self.user):
            print(f"BIENVENIDO {self.user.userName}")
            return True
        else:
            print(MENSAJES.ERROR_NUMERO_INTENTOS_LOGIN)
            return False

    def depositar(self, monto):
        
        if(monto > self.maximoMontoDeposito):
            print(MENSAJES.ERROR_TOPE_DEPOSITO)
            return 
        
        if(self.user.depositoPermitido - monto >= 0):
            # deposito
            self.user.amount += monto
            self.user.depositoPermitido -= monto
            self.user.saveChanges()
        else:
            print(MENSAJES.ERROR_TOPE_DEPOSITO_DIA)
            return 
            
    
    def retirar(self, monto):
        # si el no excedemos el limite de retiro del cajero
    
        if(self.maximoMontoRetiro < monto):
            print(MENSAJES.ERROR_TOPE_RETIRO_CAJERO)
            return


        
        # el monto no es posible de retirar
        if(self.user.amount < monto):
            # podemos usar throws para salzar una exception
            print(MENSAJES.ERROR_SALDO_INSUFICIENTE)
            return
        
        # retirando 
        print("Retirando el monto")
        self.user.amount -= monto
        self.user.saveChanges()
        print(f"Su cuenta actual es de {self.user.amount}")

    def ver(self):        
        print(f"Su saldo es: " , self.user.amount)

    def salir(self):
        print("SALIR")
        
    def showMenu(self):
        options = {
            "1" : "Depositar",
            "2" : "Reritar",
            "3" : "Ver Saldo",
            "4" : "Salir",
        }
                
        inputStr = None
        mount = None
        
        while True:
            print("MENU: ")
            for number, opcion in options.items():
                print(f"{number}. {opcion}")

            # while(True):
            inputStr = input("Ingrese su opcion: ")
            
            if (not (inputStr in options.keys())):
                print(MENSAJES.ERROR_OPCION_NO_VALIDA)
                continue
                
            if(inputStr == "1"):
                mount = self.inputAmount(options[inputStr])
                if(mount == None):
                    continue
                self.depositar(mount)
            elif(inputStr == "2"):
                mount = self.inputAmount(options[inputStr])
                if(mount == None):
                    continue
                self.retirar(mount)
            elif(inputStr == "3"):
                self.ver()
            else:
                break
        print ("================================")

