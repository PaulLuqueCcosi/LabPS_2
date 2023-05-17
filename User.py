import json
def openBD():
  with open('./UsersBD.json') as file:
    dataUsers = json.load(file)
    return dataUsers

dataUsers = openBD()
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
    ## guarda en el dicc
    dataUsers["userName"]['amount'] = self.amount
  	
    
  @classmethod
  def searchUser(cls, username, password):
    # TODO: verificar si existe un usuario en el dicc
    # retuen, devuelve El user o None.
    
    print(dataUsers["dataUsers"][1])
    if dataUsers["dataUsers"]["userName"] == username and dataUsers["dataUsers"]["userName"]["pass"] == password:  # Verificar la contraseña
        return User(dataUsers["userName"], dataUsers["userName"]["pass"])
    return None
        
