def contar_multiplos(vector, valor):
    cantidad_multiplos = 0
    for numero in vector:
        if numero % valor == 0:
            cantidad_multiplos += 1
    return cantidad_multiplos
vector = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x=0
while x==0:
    valor_dado = int(input("Ingrese un valor para encontrar múltiplos: "))
    cantidad = contar_multiplos(vector, valor_dado)
    print("La cantidad de números en el vector que son múltiplos de ",valor_dado, "es: " ,cantidad)
    print("desea reintentar? S/N ")
    f=input('')
    if f=='N' or f=='n':
        x=1
print('el proceso termino')
