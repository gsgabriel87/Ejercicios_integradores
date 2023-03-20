def contar_palabras(texto):

    palabras = texto.split()
    contar_palabra = {}
    for palabra in palabras:
        if palabra not in contar_palabra:
            contar_palabra[palabra] = 1
        else:
            contar_palabra[palabra] += 1
    return contar_palabra

def mas_frecuente_palabra(contar_palabra):

    frecuencia = 0
    mas_frecuente = None
    for palabra in contar_palabra:
        if contar_palabra[palabra] > frecuencia:
            frecuencia = contar_palabra[palabra]
            mas_frecuente = palabra
    return (mas_frecuente, frecuencia)

cadena=input("Ingrese una cadena de caracteres.\n")

contar_palabra = contar_palabras(cadena)
print(contar_palabra)
mas_frecuente = mas_frecuente_palabra(contar_palabra)
print(mas_frecuente)
