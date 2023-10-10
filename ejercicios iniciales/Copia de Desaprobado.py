Nombre = input ("Ingresa nombre del aprendiz: ")

print("Hola ",Nombre)

NombreCompetencia = input ("Ingresa el Nombre de su Competencia: ")

print("tu competencia es ",NombreCompetencia)

NotaDefinitiva = float (input ("Ingresa la nota definitiva: "))

print("la nota definitiva del aprendiz es ",NotaDefinitiva)

NumeroHoras = int (input("Ingresar el numero de horas del aprendiz en la competencia: "))

print("la cantidad de horas del aprendiz ",Nombre," de la competencia ",NombreCompetencia, " es de ",NumeroHoras)

Porcentaje = int (30)

Nfallas = int (input( "Ingrese el numero de fallas del aprendiz: "))

result = Porcentaje * NumeroHoras / 100

if Nfallas > result:
    print("el estudiante desaprobo")

else:
    print ("el estudiante aprobo")
