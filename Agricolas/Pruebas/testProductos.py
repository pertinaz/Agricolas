import unittest
from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes,Antibiotico

class TestProductos(unittest.TestCase):
    def testProductoControl(self):
        producto = ProductoControl("123ABC","control de plagas X","Cada 30 dias",50.0,45)
        self.assertEqual(producto.nombreProducto,"control de plagas X")

    def TestControlPlagas(self):
        producto = ControlPlagas("123CBA","Plaga X","15 dias",75.4,3,15)
        self.assertEqual(producto.registroICA,"123CBA")
    
    def TestControlFertilizantes(self):
        producto = ControlFertilizantes("098ABC","Fertilizante tomate","30 dias",55.7,5,"2024-03-23")
        self.assertEqual(producto.valorProducto,55.7)

    def testAntibiotico(self):
        antibiotico = Antibiotico("Antibiotico Y",500,"Bovinos",134.5,47)
        self.assertEqual(antibiotico.dosis,500)

if __name__=='__main__':
    unittest.main()
