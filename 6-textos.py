class Textos:
    def __init__(self, nombre, autor, fecha_creacion, contenido):
        self.__nombre = nombre
        self.__autor = autor
        self.__fecha_creacion = fecha_creacion
        self.__contenido = contenido
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_autor(self):
        return self.__autor
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_fecha_creacion(self):
        return self.__fecha_creacion
    
    def set_fecha_creacion(self, fecha_creacion):
        self.__fecha_creacion = fecha_creacion
    
    def get_contenido(self):
        return self.__contenido
    
    def set_contenido(self, contenido):
        self.__contenido = contenido
    
    def presentarse(self):
        print(f"Este es el texto {self.__nombre}, escrito por {self.__autor} en {self.__fecha_creacion}.")
    
    def contar_palabras(self):
        palabras = self.__contenido.split()
        return len(palabras)
texto1 = Textos("La Ilíada", "Homero", "siglo VIII a.C.", "Canta, oh diosa, la cólera del Pelida Aquiles...")
texto1.presentarse()
print(texto1.contar_palabras())
