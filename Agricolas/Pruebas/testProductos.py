import unittest
from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes,Antibiotico

class TestProductos(unittest.TestCase):
    def testProductoControl(self):
        producto = ProductoControl("123ABC","Fertilizante X","Cada 30 dias",50.0)
        self.assertEqual(producto.nombreProducto,"Fertilizante X")

    def testAntibiotico(self):
        antibiotico = Antibiotico("Antibiotico Y",500,"Bovinos",100.0)
        self.assertEqual(antibiotico.dosis,500)

if __name__=='__main__':
    unittest.main()