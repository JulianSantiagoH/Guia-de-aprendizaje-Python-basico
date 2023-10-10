menor_50 = 0
entre_50_70 = 0
entre_70_80 = 0
mayor_80 = 0

# Leer las calificaciones de los 10 estudiantes
for i in range(1, 11):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación del estudiante {i}: "))
            if 0 <= calificacion <= 100:
                break
            else:
                print("La calificación debe estar entre 0 y 100. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Ingrese una calificación numérica.")

    if calificacion < 50:
        menor_50 += 1
    elif 50 <= calificacion < 70:
        entre_50_70 += 1
    elif 70 <= calificacion < 80:
        entre_70_80 += 1
    else:
        mayor_80 += 1

# Imprimir resultados
print(f"Cantidad de estudiantes con calificación menor a 50: {menor_50}")
print(f"Cantidad de estudiantes con calificación entre 50 y 70: {entre_50_70}")
print(f"Cantidad de estudiantes con calificación entre 70 y 80: {entre_70_80}")
print(f"Cantidad de estudiantes con calificación mayor o igual a 80: {mayor_80}")
