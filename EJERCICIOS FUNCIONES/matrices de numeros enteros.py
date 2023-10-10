import random

# Función para generar una matriz 10x10 de números enteros aleatorios
def generar_matriz_de_enteros():
    matriz = []
    for _ in range(10):
        fila = []
        for _ in range(10):
            numero = random.randint(1, 100)  
            fila.append(numero)
        matriz.append(fila)
    return matriz


matriz1 = generar_matriz_de_enteros()
matriz2 = generar_matriz_de_enteros()
matriz3 = generar_matriz_de_enteros()


print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

print("\nMatriz 3:")
for fila in matriz3:
    print(fila)



    

# Función para leer los valores de una matriz
def leer_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()  

print("Matriz 1:")
leer_matriz(matriz1)

print("\nMatriz 2:")
leer_matriz(matriz2)

print("\nMatriz 3:")
leer_matriz(matriz3)



# Función para sumar tres matrices
def sumar_matrices(matriz1, matriz2, matriz3):
    resultado = []  
    for i in range(len(matriz1)):
        fila_resultado = [] 
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j] + matriz3[i][j]
            fila_resultado.append(suma)
            resultado.append(fila_resultado)  
    return resultado



matriz_suma = sumar_matrices(matriz1, matriz2, matriz3)


print("Matriz Suma:")
leer_matriz(matriz_suma)
