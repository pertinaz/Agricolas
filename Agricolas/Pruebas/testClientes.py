import unittest
from Modelo.clientes.cliente import Cliente

class TestClientes(unittest.TestCase):
    def testCliente(self):
        cliente = Cliente("Juan",12345)
        self.assertEqual(Cliente.nombreCliente,"Juan")

if __name__ == '__main__':
    unittest.main()