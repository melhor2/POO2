class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def get_especie(self):
        return self.__especie
    
    def set_especie(self, especie):
        self.__especie = especie
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.__nombre}, tengo {self.__edad} años y soy un {self.__especie}.")
        
    def emitir_sonido(self):
        pass
    

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "perro")
        self.__raza = raza
        
    def get_raza(self):
        return self.__raza
    
    def set_raza(self, raza):
        self.__raza = raza
    
    def emitir_sonido(self):
        print("¡Guau guau!")
    
    
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad, "gato")
        self.__color = color
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def emitir_sonido(self):
        print("¡Miau miau!")
        

# Creamos un objeto de tipo Perro
mi_perro = Perro("Kratos", 5, "Labrador americano")
mi_perro.presentarse() 
mi_perro.set_raza("labradors Retriever")
print(mi_perro.get_raza()) 
mi_perro.emitir_sonido() # ¡Guau guau!


# Creamos un objeto de tipo Gato
mi_gato = Gato("Hector", 3, "Negro")
mi_gato.presentarse() 
mi_gato.set_color("Blanco")
print(mi_gato.get_color()) # Blanco
mi_gato.emitir_sonido() # ¡Miau miau!
