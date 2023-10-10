class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

def agregar_usuario(usuarios, id, nombre, email):
    usuario = Usuario(id, nombre, email)
    usuarios.append(usuario)
    print(f"Usuario {nombre} agregado correctamente.")

def listar_usuarios(usuarios):
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")

def actualizar_usuario(usuarios, id, nuevo_nombre, nuevo_email):
    for usuario in usuarios:
        if usuario.id == id:
            usuario.nombre = nuevo_nombre
            usuario.email = nuevo_email
            print(f"Usuario con ID {id} actualizado correctamente.")
            return
    print(f"No se encontró un usuario con ID {id}.")

usuarios = []

while True:
    print("\nOpciones:")
    print("1. Agregar usuario")
    print("2. Listar usuarios")
    print("3. Actualizar usuario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = int(input("Ingrese ID del usuario: "))
        nombre = input("Ingrese nombre del usuario: ")
        email = input("Ingrese email del usuario: ")
        agregar_usuario(usuarios, id, nombre, email)
    if opcion == "2":
        listar_usuarios(usuarios)
    if opcion == "3":
        id = int(input("Ingrese ID del usuario a actualizar: "))
        nuevo_nombre = input("Ingrese nuevo nombre: ")
        nuevo_email = input("Ingrese nuevo email: ")
        actualizar_usuario(usuarios, id, nuevo_nombre, nuevo_email)
    if opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
