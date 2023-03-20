import datetime

# Clase Persona
class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError('El nombre no puede estar vacío')
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError('La edad debe ser un entero positivo')
        self._edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        if not isinstance(dni, str) or len(dni) != 8:
            raise ValueError('El DNI debe ser una cadena de 8 caracteres')
        self._dni = dni

# Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            print("Error: No puede ingresar una cantidad negativa.")
        else:
            self.__cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.nombre}\nCantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            print("Error: No se puede ingresar una cantidad negativa.")
        else:
            self.__cantidad += cantidad

    def retirar(self, cantidad):

            self.__cantidad -= cantidad

# Clase CuentaJoven que hereda de Cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
       # hoy = datetime.date.today()
        return self.titular.edad >= 18 and self.titular.edad < 25

    def retirar(self, cantidad):
        if not self.es_titular_valido():
            print("Error: El titular no cumple con los requisitos de edad.")
        else:
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.bonificacion}%")

persona1 = Persona("Juan", 24, "23165989")
persona2 = Persona("Juana", 14, "43165989")
cuenta = CuentaJoven(persona1,150,5)
cuenta2 = CuentaJoven(persona2,150,0)
cuenta.mostrar()
cuenta.retirar(200)
cuenta.mostrar()

cuenta2.mostrar()
cuenta2.retirar(200)
cuenta2.mostrar()