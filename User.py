
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
    pass
  	
    
  @classmethod
  def searchUser(cls, username, password):
    # TODO: verificar si existe un usuario en el dicc
    # retuen, devuelve El user o None.
    for key, value in data.items():
      if key == username:
        return User(key,  value["pass"], value["monto"])
      else:
        return None
          
