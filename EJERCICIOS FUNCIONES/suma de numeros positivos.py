def sumatoria_digitos(numero):
    suma = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma
def main():
    numeros = []  
    cantidad_menor_10 = 0
    mayor_sumatoria = 0
    numero_mayor_sumatoria = None
    while True:
        entrada = input("Ingrese un número positivo o si quiere salir oprima (q):  ")
        
        if entrada.lower() == 'q':
            break
        
        try:
            numero = int(entrada)
            if numero > 0:
                numeros.append(numero)
                suma_digitos = sumatoria_digitos(numero)
                if suma_digitos < 10:
                    cantidad_menor_10 += 1
                if suma_digitos > mayor_sumatoria:
                    mayor_sumatoria = suma_digitos
                    numero_mayor_sumatoria = numero
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
    
    if numeros:
        print(f"Número con la mayor sumatoria de dígitos: ",numero_mayor_sumatoria)
    else:
        print("No se ingresaron números.")
    
    print(f"Cantidad de dígitos menor que 10: ",cantidad_menor_10)

if __name__ == "__main__":
    main()
