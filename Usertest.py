import unittest
import json
from User import User

class TestUser(unittest.TestCase):

    def setUp(self):
        # Crea un archivo JSON de prueba
        self.test_data = {
            "dataUsers": [
                {
                    "userName": "Paquito",
                    "pass": "1225",
                    "amount": 8952.51
                },
                {
                    "userName": "Yei",
                    "pass": "5789",
                    "amount": 9152.50
                },
                {
                    "userName": "karitos",
                    "pass": "7894",
                    "amount": 9999.50
                }
            ]
        }
        with open("./UsersBD_TEST.json", "w") as archivo:
            json.dump(self.test_data, archivo)


    def test_getUserName(self):
        user = User("Paquito", "1225", 8952.51)
        self.assertEqual(user.getUserName(), "Paquito")

    def test_getPassword(self):
        user = User("Paquito", "1225", 8952.51)
        self.assertEqual(user.getPassword(), "1225")

    def test_getAmount(self):
        user = User("Paquito", "1225", 8952.51)
        self.assertEqual(user.getAmount(), 8952.51)

    def test_saveChanges(self):
        
        # Verificar Al inicio el monto original
        with open("UsersBD_TEST.json", "r") as archivo:
            data = json.load(archivo)
            amount = None
            for user_item in data["dataUsers"]:
                if user_item["userName"] == "Paquito":
                    amount = user_item["amount"]
                    break
            self.assertEqual(amount, 8952.51)
            
            
        user = User("Paquito", "1225", 1000)
        user.saveChanges(fileName="UsersBD_TEST.json")

        # Verificar que los cambios se hayan guardado en el archivo JSON
        with open("UsersBD_TEST.json", "r") as archivo:
            data = json.load(archivo)
            amount = None
            for user_item in data["dataUsers"]:
                if user_item["userName"] == "Paquito":
                    amount = user_item["amount"]
                    break
            self.assertEqual(amount, 1000)

    def test_searchUser(self):
        user = User.searchUser("Yei", "5789", fileName = "UsersBD_TEST.json")
        self.assertEqual(user.getUserName(), "Yei")
        self.assertEqual(user.getPassword(), "5789")
        self.assertEqual(user.getAmount(), 9152.50)

    def test_searchUser_nonexistent_user(self):
        # Preparar datos de prueba
        username = "testuser"
        password = "testpassword"
        
        # Ejecutar el método searchUser
        result = User.searchUser(username, password, fileName = "UsersBD_TEST.json")

        # Comprobar el resultado
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
