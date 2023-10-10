Dolar = float (3950.50)

Euro = float (4343.60)

Le = float (5028.74)

Pm = float (232.85)

Vpd = 0

Pc = int(input("ingrese la cantidad de dinero para convertir: "))

Rd = Pc/Dolar
Re = Pc/Euro
Rle = Pc/Le
Rpm = Pc/Pm

a = round(Rd, 2)
b = round(Re, 2)
c = round(Rle, 2)
d = round(Rpm, 2)

print("la cantidad de dinero que usted ingreso fue de: " ,Pc, " Pesos Colombianos")

print("la cantidad de Pesos Colombianos que ingresaste equivale a: " , a , " Dolares")

print("la cantidad de Pesos Colombianos que ingresaste equivale a: " , b , " Euros")
        
print("la cantidad de Pesos Colombianos que ingresaste equivale a: " , c , " Libras Esterlinas")
        
print("la cantidad de Pesos Colombianos que ingresaste equivale a: " , d , " Pesos Mexicanos")
        

        

