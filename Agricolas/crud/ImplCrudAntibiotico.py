from Crud.ImplCrudProductos import productoControl
from Modelo.productos.productoControl import ControlPlagas

class Antibiotico(productoControl):
    def crear(self,**kwargs):
        return ControlPlagas(kwargs['nombreProducto'],kwargs['dosis'],kwargs['tipoAnimal'],kwargs['precio'],kwargs['inventario'])
    
    def borrar(self,**kwargs):
        raise NotImplementedError
    
    def buscar(self,**kwargs):
        raise NotImplementedError