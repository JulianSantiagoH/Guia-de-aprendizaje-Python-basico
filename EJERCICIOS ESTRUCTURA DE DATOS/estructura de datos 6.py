lista=[54,64,3,65,8,17,56,34,33,2]

def cadenas(lista):
    cadena=','.join(map(str,lista))
    return cadena


print('1.Contenido de la lista')

for i in lista:
    print(i)

print('2. cadena con los elementos de la lista')

print(cadenas(lista))

print('')
print('=============================================================')
print('')

print('3.orden de mayor a menor')

lista.sort(reverse=True)

print(lista)

print('')
print('=============================================================')
print('')

print('4. buscar un elemento que el usuario pida')

print('')
print('=============================================================')
print('')

a=int(input('ingrese el numero para saber si esta en la lista: '))

if a in lista:
    print(f'{a} se encuentra en la lista')
else:
    print(f'{a} no se encuentra en la lista')

print('')
print('=============================================================')
print('')

print('5.mostrar su tamaño o longitud')

longitud=len(lista)

print(longitud)


print('')
print('=============================================================')
print('')

print('6.buscar el elemento mayor')

maximo=max(lista)

print(maximo)

print('')
print('=============================================================')
print('')

print('7. buscar el elemento menor')

minimo=min(lista)
print(minimo)


