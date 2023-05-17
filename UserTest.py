import unittest
from User import User  # Importa la clase User desde el archivo User.py

class UserTest(unittest.TestCase):

    def test_getUserName(self):
        user = User("john_doe", "password123", 100)
        self.assertEqual(user.getUserName(), "john_doe")

    def test_getPassword(self):
        user = User("john_doe", "password123", 100)
        self.assertEqual(user.getPassword(), "password123")

    def test_getUserAmount(self):
        user = User("john_doe", "password123", 100)
        self.assertEqual(user.getAmount(), 100)
        
    # def test_searchUser_existingUser(self):
    #     # Simulamos un escenario donde existe el usuario en el diccionario
    #     data = {
    #         "john_doe": {
    #             "pass": "password123",
    #             "monto": 100
    #         }
    #     }
    #     user = User.searchUser("john_doe", "password123")
    #     self.assertIsNotNone(user)
    #     self.assertEqual(user.getUserName(), "john_doe")
    #     self.assertEqual(user.getPassword(), "password123")
    #     self.assertEqual(user.amount, 100)

    # def test_searchUser_nonExistingUser(self):
    #     # Simulamos un escenario donde el usuario no existe en el diccionario
    #     data = {}  # Diccionario vacío
    #     user = User.searchUser("jane_smith", "password456")
    #     self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
