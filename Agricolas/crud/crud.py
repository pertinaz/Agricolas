import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directiorio actual:",os.getcwd())
from datetime import datetime
now = datetime.now()
from abc import ABC,abstractmethod

from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes, Antibiotico
from Modelo.clientes.cliente import Cliente
from Modelo.pedidos.factura import Factura

buscarCedula = Cliente.buscarCedula
mostrarFactura = Factura.mostrarFactura

guardarCliente = Cliente.registrarCliente
cliente = Cliente

guardarFactura = Factura.registrarFactura
factura = Factura

guardarProductoControl = ProductoControl.registrarProducto
productoPlagas = ControlPlagas
productoFertilizante = ControlFertilizantes

guardarAntibiotico = Antibiotico.registrarAntibiotico
antibiotico = Antibiotico


class Crud(ABC):
    @abstractmethod
    def crear(self,**kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def borrar(self,**kwargs):
        raise NotImplementedError
    
    @abstractmethod
    def buscar(self,**kwargs):
        raise NotImplementedError
