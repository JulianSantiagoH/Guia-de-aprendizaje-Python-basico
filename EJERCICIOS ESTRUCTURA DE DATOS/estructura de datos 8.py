def menu ():
    print('*******************************************************')
    print('*****         Informacion Estudiantil             *****')
    print('*****                                             *****')
    print('***** 1.Ingresar Estudiantes                      *****')
    print('***** 2.Listar Estudiantes                        *****')
    print('***** 3.Modificar notas de un estudiante          *****')
    print('***** 4.Consultar nota definitiva de estudiante   *****')
    print('***** 5.Salir del Programa                        *****')
    print('*****                                             *****')
    print('*******************************************************')

estudiantes=[]

def ingresar():
    if len(estudiantes)>=5:
        print('ya ingreso los 5 estudiantes')
        return
    
    Codigo=int(input('Ingrese el Codigo del estudiante (como numero): '))
    Nombre=input('Ingrese el Nombre del estudiante: ')
    Nota1=float(input('Ingrese la primera nota: '))
    Nota2=float(input('Ingrese la Segunda nota: '))

    if Nota1 <0 and Nota1 >5 and Nota2 <0 and Nota2 >5:
            print('Las notas deben estar entre 0 y 5')
    else:
        estudiantes.append({'Codigo':Codigo,'Nombre':Nombre,'Nota1':Nota1,'Nota2':Nota2})
        print('notas ingresadas con exito')




def listar():
    if not estudiantes:
        print('No hay estudiantes registrados.')
    else:
        print('Lista de estudiantes: ')
        for estudiante in estudiantes:
            print(f" codigo: {estudiante['Codigo']}, Nombre: {estudiante['Nombre']}, Nota 1: {estudiante['Nota1']}, Nota 2: {estudiante['Nota2']}")


def modificar():
    Codigo=int(input('Ingrese el codigo del estudiante a modificar: '))

    for estudiante in estudiantes:
        
        if estudiante['Codigo']==Codigo:
            nnota1=float(input('ingrese la nueva nota 1'))
            nnota2=float(input('ingrese la nueva nota 2'))
            if nnota1 <0 and nnota1 >5 and nnota2 <0 and nnota2>5:
                print('Las notas deben estar entre 0 y 5')
               
            else:
                estudiante['Nota1']=nnota1
                estudiante['Nota2']=nnota2

def ndefinitiva():
    Codigo=int(input('ingrese el codigo del estudiante'))

    for estudiante in estudiantes:
        if estudiante['Codigo']==Codigo:
            definitiva=(estudiante['Nota1']+ estudiante['Nota2'])/2
            print(f"la nota definitiva del estudiante {estudiante['Nombre']} tiene como nota definitiva ",definitiva)

        
    
               


o=0

while o == 0:
    menu()
    a=int(input('Escoja la Opcion Deseada: '))

    if a==1:
        ingresar()

    if a==2:
        listar()

    if a==3:
        modificar()

    if a==4:
        ndefinitiva()



    if a == 5:
        o=1
        print('Programa Finalizado')
