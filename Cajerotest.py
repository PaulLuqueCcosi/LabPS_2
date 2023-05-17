import unittest
from unittest.mock import patch
from User import User
from Cajero import Cajero
import MENSAJES

class TestCajero(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero()

    def test_inputAmount_valid_amount(self):
        with patch('builtins.input', return_value='100'):
            amount = self.cajero.inputAmount("depositar")
            self.assertEqual(amount, 100)
            

    def test_inputAmount_negative_amount(self):
        with patch('builtins.input', return_value='-100'):
            with patch('builtins.print') as mocked_print:
                amount = self.cajero.inputAmount("depositar")
                self.assertIsNone(amount)
                mocked_print.assert_called_with(MENSAJES.ERROR_MONTO_NEGATIVO)

    def test_inputAmount_non_numeric_input(self):
        with patch('builtins.input', return_value='abc'):
            with patch('builtins.print') as mocked_print:
                amount = self.cajero.inputAmount("depositar")
                self.assertIsNone(amount)
                mocked_print.assert_called_with(MENSAJES.ERROR_VALOR_NO_NUMERICO)
                
    def test_inputAmount___input(self):
        with patch('builtins.input', return_value=''):
            with patch('builtins.print') as mocked_print:
                amount = self.cajero.inputAmount("depositar")
                self.assertIsNone(amount)
                mocked_print.assert_called_with(MENSAJES.ERROR_VALOR_NO_NUMERICO)


    def test_depositar_below_maximum_deposit(self):
        self.cajero.user = User("username", "password", 1000)
        self.cajero.user.depositoPermitido = 1000
        self.cajero.maximoMontoDeposito = 5000
        self.cajero.depositar(1000)
        self.assertEqual(self.cajero.user.amount, 2000) ## monto de la cuenta despues del deposito
        self.assertEqual(self.cajero.user.depositoPermitido, 0)

    def test_depositar_above_maximum_deposit(self):
        self.cajero.user = User("username", "password", 1000)
        self.cajero.user.depositoPermitido = 1000
        self.cajero.maximoMontoDeposito = 500
        with patch('builtins.print') as mocked_print:
            self.cajero.depositar(1000)
            mocked_print.assert_called_with(MENSAJES.ERROR_TOPE_DEPOSITO)

    def test_depositar_above_daily_limit(self):
        self.cajero.user = User("username", "password", 1000)
        self.cajero.user.depositoPermitido = 500
        self.cajero.maximoMontoDeposito = 1000
        with patch('builtins.print') as mocked_print:
            self.cajero.depositar(1000)
            mocked_print.assert_called_with(MENSAJES.ERROR_TOPE_DEPOSITO_DIA)

    def test_depositar_valid(self):
        self.cajero.user = User("username", "password", 100)
        self.cajero.user.depositoPermitido = 500
        self.cajero.maximoMontoDeposito = 1000
        
        self.cajero.depositar(400)
        
        self.assertEqual(self.cajero.user.amount, 500)
        self.assertEqual(self.cajero.user.depositoPermitido, 100)
        
    
    def test_retirar_valid(self):
        self.cajero.user = User("username", "password", 100)
        self.cajero.retirar(50)        
        self.assertEqual(self.cajero.user.amount, 50)
        
        self.cajero.user = User("username", "password", 100)
        self.cajero.retirar(50.5)        
        self.assertEqual(self.cajero.user.amount, 49.5)
    

 
    def test_retirar_invalid(self):
        self.cajero.user = User("username", "password", 100)
        
        with patch('builtins.print') as mocked_print:
            self.cajero.retirar(150)    
            mocked_print.assert_called_with(MENSAJES.ERROR_SALDO_INSUFICIENTE)
            self.assertEqual(self.cajero.user.amount, 100)

     
    def test_retirar_invalid_maxTope(self):
        self.cajero.user = User("username", "password", 1000)
        self.cajero.maximoMontoRetiro = 500
        with patch('builtins.print') as mocked_print:
            self.cajero.retirar(600)    
            mocked_print.assert_called_with(MENSAJES.ERROR_TOPE_RETIRO_CAJERO)
            self.assertEqual(self.cajero.user.amount, 1000)    

if __name__ == '__main__':
    unittest.main()
