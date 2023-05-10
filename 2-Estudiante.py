class Estudiante_I():
    
    def __init__(self, nombre, apellido, edad, semestre):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.semestre = semestre
        
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años y voy en {self.semestre} semestre")


class Estudiante_M(Estudiante_I):
    
    def __init__(self, nombre, apellido, edad, semestre, costo):
        super().__init__(nombre, apellido, edad, semestre)
        self.costo = costo
        
    def Costop(self, Costo_M):
        if float(Costo_M) > 18000:
            self.costo = Costo_M
        
    def costot(self):
        return self.costo
    
    def presentarse2(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años y voy en {self.semestre} semestre, y el costo de mi matricula es {self.costo} usd")

estudiante1 = Estudiante_I("Jeremy", "Rodriguez", "18", "3er")
estudiante1.presentarse()

estudiante2 = Estudiante_M("Andrea", "Ronc", "22", "2do", "19.000")
estudiante2.presentarse2()
estudiante2.Costop('17.000')
estudiante2.Costop('20.000')

