totalp = 0
totalh = 0
totalm = 0
sumah= 0
sumam = 0
edadminima = None

# Pedir datos de los invitados
while True:
    edad = int(input("Ingrese la edad de la persona (ingrese 0 para finalizar): "))
    
    if edad == 0:
        break  # Salir del bucle si se ingresa 0
    
    if edad < 18:
        print("Lo siento, los menores de edad no pueden asistir a la fiesta.")
        continue  # Continuar con la siguiente iteración
    
    sexo = input("Ingrese el sexo de la persona (H para hombre, M para mujer): ").upper()
    
    if sexo == 'H':
        totalh += 1
        sumah += edad
    elif sexo == 'M':
        totalm += 1
        sumam += edad
    else:
        print("Sexo no válido. Use 'H' para hombre o 'M' para mujer.")
        continue  # Continuar con la siguiente iteración
    
    # Actualizar la edad mínima
    if edadminima is None or edad < edadminima:
        edadminima = edad
    
    totalp += 1

# Calcular promedio de edades por sexo
promedioh = sumah / totalh if total_hombres > 0 else 0
promediom = sumam / totalm if totalm > 0 else 0

# Mostrar resultados
print('Total de personas que asistieron: ',totalp)
print('Total de hombres: ',totalh)
print('Total de mujeres: ',totalm)
print('Promedio de edad de hombres: ',promedioh)
print('Promedio de edad de mujeres: ',promediom)
print('Edad mínima que asistió: ',edadminima)


#cambio normal