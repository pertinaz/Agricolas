from Crud.ImplCrudProductos import productoControl
from Modelo.productos.productoControl import ControlPlagas

class ControlPlagas(productoControl):
    def crear(self,**kwargs):
        return ControlPlagas(kwargs['periodoCarencia'])
    
    def borrar(self,**kwargs):
        raise NotImplementedError
    
    def buscar(self,**kwargs):
        raise NotImplementedError
