import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directiorio actual:",os.getcwd())

from Crud.crud import Crud
from Modelo.productos.productoControl import ProductoControl,ControlPlagas, ControlFertilizantes, Antibiotico

class productoControl(Crud):
    def crear(self,**kwargs):
        return ProductoControl(kwargs['registroICA'],kwargs['nombreProducto'],kwargs['frecuenciaAplicacion'],kwargs['valorProducto'],kwargs['inventario'])
    
    def borrar(self,**kwargs):
        raise NotImplementedError
    
    def buscar(self,**kwargs):
        raise NotImplementedError
