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


class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        if not isinstance(titular, Persona):
            raise ValueError('El titular debe ser una instancia de Persona')
        self._titular = titular

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        if cantidad < 0:
            raise ValueError('La cantidad debe ser un valor positivo')
        self._cantidad += cantidad

    def retirar(self, cantidad):
       # if cantidad < 0:
       #     raise ValueError('La cantidad debe ser un valor positivo')
       # if self._cantidad - cantidad < 0:
        #    raise ValueError('La cantidad a retirar es mayor que el saldo de la cuenta')
        self._cantidad -= cantidad

    def mostrar(self):
        print(f'Titular: {self.titular.nombre}\nSaldo: {self.cantidad}')


persona1 = Persona("Pepe", 24, "23165989")
cuenta = Cuenta(persona1,150)
cuenta.mostrar()
cuenta.ingresar(200)
cuenta.mostrar()
cuenta.retirar(400)
cuenta.mostrar()