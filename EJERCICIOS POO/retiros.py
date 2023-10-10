class Cuenta:
    def __init__(self, numero, fecha_apertura, saldo):
        self.numero = numero
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo

    def get_numero(self):
        return self.numero

    def set_numero(self, numero):
        self.numero = numero

    def get_fecha_apertura(self):
        return self.fecha_apertura

    def set_fecha_apertura(self, fecha_apertura):
        self.fecha_apertura = fecha_apertura

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def Retiro(self, valor):
        if valor > self.saldo:
            print("No se puede realizar el retiro. Saldo insuficiente.")
        else:
            self.saldo -= valor

    def Consignar(self, valor):
        self.saldo += valor

    def mostrar_informacion(self):
        print(f"Número de cuenta: {self.numero}")
        print(f"Fecha de apertura: {self.fecha_apertura}")
        print(f"Saldo actual: {self.saldo}")
cuenta = Cuenta(numero="123456789", fecha_apertura="2023-09-29", saldo=1000)
cuenta.mostrar_informacion()
x=0
while x==0:
    print("_________________________________________")
    print("1. agregar a la cuenta?")
    print("2. desea retirar?")
    print("3. cerrar el programa")
    a=int(input("==> " ))
    print("_________________________________________")
    if a==1:
          b=int(input("digite la cantidad a consignar ==> "))
          cuenta.Consignar(b)
          cuenta.mostrar_informacion()
    if a==2:    
        b=int(input("digite la cantidad a retirar ==> "))
        cuenta.Retiro(b) 
        cuenta.mostrar_informacion()
    if a==3:
        x=1
print("el programa finalizo")
