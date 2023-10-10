lista=[]

for i in range(20):
    n=int(input('ingrese un numero: '))

    while n < 0:
        print('el numero debe ser positivo, intenta nuevamente')
        n=int(input('==>'))

    lista.append(n)

print(lista)
        
