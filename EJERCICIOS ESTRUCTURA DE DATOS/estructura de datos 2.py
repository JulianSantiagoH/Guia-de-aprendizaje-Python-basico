n=int(input('ingrese hasta que numero llegar: '))

lista=list(range(1,n))

for i in range(len(lista)):
    lista[i]=lista[i]**3

print(lista)
