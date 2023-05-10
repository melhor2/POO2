class Personas:
    def __init__(self, name, surname, occupation, age, gender):
        self.name = name
        self.surname = surname
        self.occupation = occupation
        self.age = age
        self.gender = gender
    
    def get_Present(self):
        print("Buenos dias, Me presento")
        print(f"\nFull name: {self.name} {self.surname} \nOccupation o or profession : {self.occupation} \nHow old are you : {self.age} \nWhat generated are you : {self.gender}")

    def setName(self, name):
        self.name = name
        
    def setSurname(self, surname):
        self.surname = surname
        
    def setOccupation(self, occupation):
        self.occupation = occupation
         
    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender
        
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
    
    def getOccupation(self):
        return self.occupation
    
    def getAge(self):
        return self.age
    
    def getGender(self):
        return self.gender
    
Personas1 = Personas('jeremy', 'Rodriguez', 'Estudiante', '19', 'Masculino')
Personas1.get_Present()

print("---------------------------------inheritance-----------------------------------")

class Profesional(Personas):
    
    def __init__(self, name, surname, occupation, age, gender):
        super().__init__(name, surname, occupation, age, gender)
        
personas2 = Profesional('Juan', 'Pérez', 'Ingeniero', '35', 'Masculino')
personas2.get_Present()
