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
class CuentaCorriente(Cuenta):   
    def __init__(self, numero, fecha_apertura, saldo, numero_chequera):
        super().__init__(numero, fecha_apertura, saldo)
        self.numero_chequera = numero_chequera

    def get_numero_chequera(self):
        return self.numero_chequera

    def set_numero_chequera(self, numero_chequera):
        self.numero_chequera = numero_chequera

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de chequera: {self.numero_chequera}")
cuenta = Cuenta(numero="123456789", fecha_apertura="2023-09-29", saldo=1000)
cuenta.mostrar_informacion()
def menu1():
    print("_________________________________________")
    print("1. cuenta comun")
    print("2.cuenta corriente")
    e=int(input("==> "))
    return e
def menu():
    print("_________________________________________")
    print("1. agregar a la cuenta?")
    print("2. desea retirar?")
    print("3. cerrar el programa")
    a=int(input("==> " ))
    print("_________________________________________")
    return a
def menu2():
     print("_________________________________________")
     print("1. cosignar a cuenta corriente")
     print("2. retirar de cuenta corriente")
     print("3. cambiar numero de cheque")
     print(" 4.para volver al inicio")
     o=int(input("==> "))
     return o
x=0
while x==0:
    e=menu1()
    if e==1:
         a=menu()
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
    if e==2:
        cuenta_corriente = CuentaCorriente(numero="123456789", fecha_apertura="2023-09-29", saldo=1000, numero_chequera="7890")
        cuenta_corriente.mostrar_informacion()
        z=0
        while z==0:
            
            o=menu2()
            if o==1:
                b=int(input("digite la cantidad a consignar ==> "))
                cuenta_corriente.Consignar(b)  
                cuenta_corriente.mostrar_informacion()
            if o==2:
                 b=int(input("digite la cantidad a retirar ==> "))
                 cuenta_corriente.Retiro(b)  
                 cuenta_corriente.mostrar_informacion()
            if o==3:
                b=int(input("digite el numero de 4 digitos que quiera que sea su nuevo numero de cheque ==> "))
                cuenta_corriente.set_numero_chequera(b)
                print("Nuevo número de chequera:",cuenta_corriente.get_numero_chequera())
            if o==4:
                z=1
print("el programa finalizo")
