import json

class User:
  
  def __init__ (self, userName, password, amount):
    self.userName = userName
    self.password = password
    self.amount = amount
    self.depositoPermitido = 3000
    
  def getUserName(self):
    return self.userName
  
  def getPassword(self):
    return self.password
  
  def getAmount(self): 
    return self.amount
  
  def saveChanges(self, fileName = "UsersBD.json"):
    ## guarda en el json
    with open(fileName, "r") as archivo:
        data = json.load(archivo)
        archivo.close()
    
    # Buscamos al usuario
    for user in data["dataUsers"]:
        if user["userName"] == self.userName:
            user["amount"] = self.amount
            break
    
    with open(fileName, "w") as archivo:
        json.dump(data, archivo)
        archivo.close()
    
  @classmethod
  def searchUser(cls, username, password, fileName = "UsersBD.json"):
    with open(fileName, "r") as archivo:
        dataUsers = json.load(archivo)
    
    retorno = None
    for userItem in dataUsers["dataUsers"]:
        if userItem["userName"] == username and userItem["pass"] == password:  # Verificar la contraseña
            retorno = User(username, password, userItem["amount"])
    
    archivo.close()
    return retorno
        
