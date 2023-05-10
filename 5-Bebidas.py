class Bebida:
    def __init__(self, nombre, creacion, ingredientes):
        self.__nombre = nombre
        self.__creacion = creacion
        self.__ingredientes = ingredientes
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_creacion(self):
        return self.__creacion
    
    def set_creacion(self, creacion):
        self.__creacion = creacion
    
    def get_ingredientes(self):
        return self.__ingredientes
    
    def set_ingredientes(self, ingredientes):
        self.__ingredientes = ingredientes
    
    def presentarse(self):
        print(f"Hola, soy una bebida llamada {self.__nombre} creada en {self.__creacion}. Mis ingredientes son {self.__ingredientes}. ¡Disfrútame!")

# Crear un objeto de la clase Bebida
mi_bebida = Bebida("Margarita", "México", ["tequila", "jugo de limón", "jarabe de agave"])

# Llamar al método presentarse del objeto mi_bebida
mi_bebida.presentarse()

# Cambiar el nombre de la bebida usando el método set_nombre y luego llamar al método presentarse nuevamente
mi_bebida.set_nombre("Piña colada")
mi_bebida.presentarse()
