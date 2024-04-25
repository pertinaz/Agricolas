class Cliente:
    def __init__(self,nombreCliente,cedulaCliente):
        self.nombreCliente = nombreCliente
        self.cedulaCliente = cedulaCliente
        self.__clientes = [] # Crear un metodo de clase (base de datos) para guardar los clientes 

    @property
    def clientes(self):
        return self.__clientes
    
    @clientes.setter
    def clientes(self,cliente):
        self.__clientes.append(cliente)
    
    def registrarCliente(self,cliente):
        self.__clientes = cliente
    
    def buscarCedula(self,cedulaCliente):
        for cedula in self.__clientes.cedulaCliente:
            if cedulaCliente == cedula:
                return (f"DATOS DEL CLIENTE: \n{self.__clientes}")
            else: 
                raise ValueError(f"No existe tal cliente con cedula: {cedulaCliente}")
