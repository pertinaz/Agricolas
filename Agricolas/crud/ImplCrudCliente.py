from Crud.crud import Crud
from Modelo.clientes.cliente import Cliente

class Cliente(Crud):
    def crear(self,**kwargs):
        return Cliente.Cliente(kwargs['nombre'],kwargs['cedula'])
    
    def borrar(self,**kwargs):
        return Cliente.Cliente()