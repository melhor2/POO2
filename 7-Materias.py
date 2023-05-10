class Materia:
    def __init__(self, nombre, creacion):
        self._nombre = nombre
        self._creacion = creacion

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_creacion(self):
        return self._creacion

    def set_creacion(self, nueva_creacion):
        self._creacion = nueva_creacion

    def saludar(self):
        print(f"Hola, soy la materia {self._nombre}!")

    def presentarse(self):
        print(f"Soy la materia {self._nombre}, creada en el año {self._creacion}.")

# Crear objetos de la clase Materia
materia1 = Materia("Matemáticas", 1995)
materia2 = Materia("Historia", 2001)

# Llamar a los métodos definidos
materia1.saludar()
materia2.presentarse()

# Cambiar el nombre de una materia utilizando el setter correspondiente
materia1.set_nombre("Álgebra")
print(materia1.get_nombre()) # Imprime "Álgebra"
