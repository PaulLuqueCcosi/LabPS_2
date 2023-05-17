import unittest
from unittest.mock import patch
from Cajero import Cajero
from User import User

class CajeroTest(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero()

    def test_inputAmount_validInput(self):
        with patch('builtins.input', return_value='100'):
            result = self.cajero.inputAmount("depositar")
            self.assertEqual(result, 100)

    def test_inputAmount_invalidInput(self):
        with patch('builtins.input', return_value='abc'):
            result = self.cajero.inputAmount("retirar")
            self.assertIsNone(result)

    @patch('builtins.input', side_effect=['john_doe', 'password123'])
    def test_login_successful(self, mock_input):
        user = User("john_doe", "password123", 100)
        User.searchUser = unittest.mock.MagicMock(return_value=user)

        self.assertTrue(self.cajero.login())
        self.assertEqual(self.cajero.user, user)
        self.assertTrue(self.cajero.isLogin)

    @patch('builtins.input', side_effect=['jane_smith', 'password456'])
    def test_login_unsuccessful(self, mock_input):
        User.searchUser = unittest.mock.MagicMock(return_value=None)

        self.assertFalse(self.cajero.login())
        self.assertIsNone(self.cajero.user)
        self.assertFalse(self.cajero.isLogin)

    def test_depositar(self):
        user = User("john_doe", "password123", 100)
        self.cajero.user = user

        self.cajero.depositar(50)
        self.assertEqual(user.amount, 150)

    def test_retiro_sufficientFunds(self):
        user = User("john_doe", "password123", 100)
        self.cajero.user = user

        with patch('builtins.print') as mock_print:
            self.cajero.retiro(50)
            mock_print.assert_called_with("Su cuenta actual es de 50")

    def test_retiro_insufficientFunds(self):
        user = User("john_doe", "password123", 100)
        self.cajero.user = user

        with patch('builtins.print') as mock_print:
            self.cajero.retiro(150)
            mock_print.assert_called_with("NO SE TIENE ESE DINERO EN AL CUENTA")

    def test_ver(self):
        user = User("john_doe", "password123", 100)
        self.cajero.user = user

        with patch('builtins.print') as mock_print:
            self.cajero.ver()
            mock_print.assert_called_with("Su saldo es: 100")

    def test_salir(self):
        with patch('builtins.print') as mock_print:
            self.cajero.salir()
            mock_print.assert_called_with("SALIR")

    @patch('builtins.input', side_effect=['2', '50'])
    def test_showMenu_retirar(self, mock_input):
        user = User("john_doe", "password123", 100)
        self.cajero.user = user
        self.cajero.retirar = unittest.mock.MagicMock()

        self.cajero.showMenu()
        self.cajero.retirar.assert_called_with(50)

if __name__ == '__main__':
    unittest.main()
