#forma iterativa

def get_int():
    while True:
        try:
            num = int(input("ITERATIVA: Ingresa un número entero: "))
            return num
        except ValueError:
            print("ITERATIVA: El valor ingresado no es un número entero válido. Inténtalo de nuevo.")
#forma recursiva
def get_int2():
    try:
        num = int(input("RECURSIVA: Ingresa un número entero: "))
        return num
    except ValueError:
        print("RECURSIVA: El valor ingresado no es un número entero válido. Inténtalo de nuevo.")
        return get_int2()
    
get_int()
get_int2()