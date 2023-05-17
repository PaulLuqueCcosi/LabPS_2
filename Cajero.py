from User import User

class Cajero:   
  
    def __init__(self):
        self.user = None
        self.isLogin = False
        self.maxNnumberAttemps = 3

    def inputAmount (self, operation):
        try:
            amount = float(input(f'Ingrese el monto a {operation}'))
            return amount
        except ValueError:
            print('Error. Ingresa valores numericos.')
        
    def login(self):
        numAttemp = 1
        while(numAttemp <= self.maxNnumberAttemps):
            userName = input("Username: ")
            password = input("Password: ")

            user = User.searchUser(userName, password)
                
            # ERROR
            if(user == None):
                print("ERROR: Usuario o contrasena incorrecto")
                print(f"Le quedan {self.maxNnumberAttemps - numAttemp}") 
                numAttemp += 1
            else:
                # susario correcto
                self.user = user
                self.isLogin = True
                break
                
        if(self.user):
            print(f"Bienvenido {self.userName}")
            return True
        else:
            print("ERROR: A excedido los intentos, no podra realizar operaciones.")
            return False

    def depositar(self, monto):
        # verificamos si ya se inicio sesion
        # if(not self.isLogin):
        #     print("ERROR: NO LOGEADO")
        #     return
        
        # deposito
        self.user.amount += monto
        self.user.saveChange()
    
    def retiro(self, monto):
        # verificamos si ya se inicio sesion
        # if(not self.isLogin):
        #     print("NO LOGEADO")
        #     return
        
        # el monto no es posible de retirar
        if(self.user.amount < monto):
            # podemos usar throws para salzar una exception
            print("NO SE TIENE ESE DINERO EN AL CUENTA")
            return
        
        # Retiro
        print(f"Su monto actual es de {self.user.amount}")
        print(f"Retiro {monto}")
        
        # retirando 
        self.user.amount -= monto
        self.user.saveChanges()
        print(f"Su cuenta actual es de {self.user.amount}")

    def ver(self):
        # verificamos si ya se inicio sesion
        # if(not self.isLogin):
        #     print("NO LOGEADO")
        #     return
        
        print(f"Su saldo es: " , self.monto)

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
        
        
        for number, opcion in options.items():
            print(f"{number}. {opcion}")
        
        while(True):
            inputStr = input("Ingrese su opcion: ")
            
            if (not (inputStr in options.keys())):
                print(f"ERROR: '{inputStr}' no es una opcion valida")
                continue
            
            # correcto 
            mount = self.inputAmount(options[inputStr])
            break
            
        if(inputStr == "1"):
            self.depositar(mount)
        elif(inputStr == "2"):
            self.retirar(mount)
        elif(inputStr == "3"):
            self.ver()
        else:
            self.salir()
        
