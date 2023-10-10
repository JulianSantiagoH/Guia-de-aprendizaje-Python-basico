saldo = 100000  # Inicialmente, se asume un saldo de $100,000

# Función para mostrar el estado financiero
def mostrar_estado_financiero(saldo):
    if saldo <= 0:
        print("\033[91m¡Estás sin dinero!")
    elif saldo < 50000:
        print("Tienes poco efectivo, estás a punto de alcanzar el tope mínimo.")
    elif saldo >= 1000000:
        print("Tienes un buen estatus financiero.")
    else:
        print("Tu saldo es suficiente.")

# Función para agregar dinero a la billetera virtual
def agregar_dinero(saldo, cantidad):
    saldo += cantidad
    return saldo

# Mostrar el estado financiero inicial
mostrar_estado_financiero(saldo)

while True:
    print("\n¿Qué acción deseas realizar?")
    print("1. Mostrar estado financiero")
    print("2. Agregar dinero")
    print("3. Salir")
    
    opcion = input("Ingresa el número de la opción que deseas: ")
    
    if opcion == "1":
        mostrar_estado_financiero(saldo)
    elif opcion == "2":
        try:
            cantidad = float(input("Ingresa la cantidad que deseas agregar: "))
            if cantidad < 0:
                print("No puedes agregar una cantidad negativa.")
            else:
                saldo = agregar_dinero(saldo, cantidad)
                print(f"Se han agregado ${cantidad} a tu billetera.")
        except ValueError:
            print("Ingresa una cantidad válida.")
    elif opcion == "3":
        print("Gracias por usar la billetera virtual. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Ingresa un número válido (1, 2 o 3).")
