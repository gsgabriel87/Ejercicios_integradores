from math import gcd  

def mcd(x,y):
 
    print("El máximo común divisor entre {} y {} es: ".format(x,y))  
    print(gcd(x,y))

print ("----------------forma 1---------------")

x= int(input("ingrese un numero "))  
y= int(input("ingrese un numero "))   
mcd(x,y)

print ("----------------forma 2---------------")


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)

a= int(input("ingrese un numero "))  
b= int(input("ingrese un numero "))    
resultado = maximo_comun_divisor(a, b)
resultado_recursivo = maximo_comun_divisor_recursivo(a, b)
print(
    f"El Máximo común divisor de {a} y {b} es {resultado}. De manera recursiva, es {resultado_recursivo}")