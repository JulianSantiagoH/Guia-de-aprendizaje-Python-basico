
def maximo(x, y):
    if x > y:
        return x
    else:
        return y

def minimo(x, y):
    if x < y:
        return x
    else:
        return y

x = int(input("Ingresa un número: "))
y = int(input("Ingresa otro número: "))


resultado = maximo(x - 3, minimo(x + 2, y - 5))


print("El resultado es:", resultado)
