from User import User

class Cajero:   
  
    def __init__(self):
        self.user = None
        self.isLogin = False
        self.maxNnumberAttemps = 3

    def inputAmount (self, operation):
        amount = None
        try:
            amount = float(input(f'Ingrese el monto a {operation}: '))
            if(amount <= 0):
                print("ERROR: ingrese el monto positivo")
                amount = None
        except ValueError:
            print('Error. Ingresa valores numericos.')

        return amount

        
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
            print(f"Bienvenido {self.user.userName}")
            return True
        else:
            print("ERROR: A excedido los intentos, no podra realizar operaciones.")
            return False

    def depositar(self, monto):
        # deposito
        self.user.amount += monto
        self.user.saveChanges()
    
    def retirar(self, monto):
        # el monto no es posible de retirar
        if(self.user.amount < monto):
            # podemos usar throws para salzar una exception
            print("ERROR: SALDO INSUFICIENTE EN LA CUENTA")
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

            while(True):
                inputStr = input("Ingrese su opcion: ")
                
                if (not (inputStr in options.keys())):
                    print(f"ERROR: '{inputStr}' no es una opcion valida")
                    continue
                
                # correcto 
                break
                
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

