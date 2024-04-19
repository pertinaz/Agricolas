import unittest
from Modelo.pedidos.factura import Factura

class TestFacturas(unittest.TestCase):
    def testFacturas(self):
        facturas = Factura("Juan","Fertilizantes","03/03/2024",1300.0)
        self.assertEqual(Factura.valorTotalCompra,1300.0)

if __name__ == '__main__':
    unittest.main()