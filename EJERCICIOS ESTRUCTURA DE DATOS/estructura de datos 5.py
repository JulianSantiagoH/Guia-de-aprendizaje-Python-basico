cadena = input("Ingrese una cadena de texto: ")

palabras = cadena.split()

palabras_sin_repetir = []


for palabra in palabras:
    if palabra.upper() not in palabras_sin_repetir:
        palabras_sin_repetir.append(palabra.upper())


print("Palabras en mayúscula sin repetir en el orden original:")
for palabra in palabras:
    if palabra.upper() in palabras_sin_repetir:
        print(palabra.upper())
        palabras_sin_repetir.remove(palabra.upper())
