from math import gcd  

def funcion_mcm(x,y):
 
    mcm=int(x*y/gcd(x,y)) 
    print("El mínimo común múltiplo entre {} y {} es {}\n".format(x,y,mcm))  

x= int(input("ingrese un numero "))  
y= int(input("ingrese un numero "))   
funcion_mcm(x,y)

print("-------------otra manera------------")

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x= int(input("ingrese un numero "))  
y= int(input("ingrese un numero ")) 


result = lcm(x, y)
print(result)
