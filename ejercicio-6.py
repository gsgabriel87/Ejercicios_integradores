class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        self.dni = dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return ("es mayor de edad")
        else:
            return ("es menor de edad")

        
persona1 = Persona("Pepe", 24, 23165989)

print(persona1.get_nombre())   
print(persona1.es_mayor_de_edad())   
persona1.mostrar()  