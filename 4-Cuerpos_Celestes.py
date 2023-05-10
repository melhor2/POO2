class CuerposCelestes:
    def __init__(self, nombre, tipo, edad):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def presentarse(self):
        print(f"Hola, soy un {self.__tipo} llamado {self.__nombre}.")

    def calcular_edad(self):
        velocidad_luz = 299792458 # m/s
        edad_años_luz = self.__edad * velocidad_luz * 31557600 # 1 año luz = 31557600 segundos
        return f"Mi edad es de aproximadamente {round(edad_años_luz, 2)} años luz."


# Crear objetos de la clase CuerposCelestes
sol = CuerposCelestes("Sol", "estrella", 4600000000)
print(sol.get_nombre())
print(sol.get_tipo())
print(sol.calcular_edad())
sol.presentarse()

tierra = CuerposCelestes("Tierra", "planeta", 4500000000)
print(tierra.get_nombre())
print(tierra.get_tipo())
print(tierra.calcular_edad())
tierra.presentarse()

galaxia = CuerposCelestes("Vía Láctea", "galaxia", 13800000000)
print(galaxia.get_nombre())
print(galaxia.get_tipo())
print(galaxia.calcular_edad())
galaxia.presentarse()
