import json
def openBD():
    with open("./UsersBD.json", "r") as archivo:
        data = json.load(archivo)
        return data



class User:
  
  def __init__ (self, userName, password, amount):
    self.userName = userName
    self.password = password
    self.amount = amount
    
  def getUserName(self):
    return self.userName
  
  def getPassword(self):
    return self.password
  
  def getAmount(self): 
    return self.amount
  
  def saveChanges(self):
    ## guarda en el json
    with open("./UsersBD.json", "r") as archivo:
        data = json.load(archivo)
    
    # Buscamos al usuario
    for user in data["dataUsers"]:
        if user["userName"] == self.userName:
            user["amount"] = self.amount
            break
    
    with open("./UsersBD.json", "w") as archivo:
        json.dump(data, archivo)
  	
    
  @classmethod
  def searchUser(cls, username, password):
    #  = openBD()
    with open("./UsersBD.json", "r") as archivo:
        dataUsers = json.load(archivo)
    
    retorno = None
    for userItem in dataUsers["dataUsers"]:
        if userItem["userName"] == username and userItem["pass"] == password:  # Verificar la contraseña
            retorno = User(username, password, userItem["amount"])
    return retorno
        
