from Crud.ImplCrudProductos import productoControl
from Modelo.productos.productoControl import ControlPlagas

class ControlFertilizante(productoControl):
    def crear(self,**kwargs):
        return ControlPlagas(kwargs['fechaUltimaAplicacion'])
    
    def borrar(self,**kwargs):
        raise NotImplementedError
    
    def buscar(self,**kwargs):
        raise NotImplementedError