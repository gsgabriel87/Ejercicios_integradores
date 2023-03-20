import string


def contar_palabras(cadena):

    cadena = cadena.lower()
    for p in string.punctuation:
        cadena = cadena.replace(p, '')


    palabras = cadena.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


cadena = "codo a codo"
frecuencias = contar_palabras(cadena)
print(frecuencias)


#{'codo': 2, 'a': 1}