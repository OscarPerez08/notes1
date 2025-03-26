
usuarios = {}  # Diccionario para almacenar usuarios y contraseñas
roles = {}     # Diccionario para asignar roles (profesor o estudiante)
cursos = {}    # Diccionario para asociar usuarios con sus cursos
notas = {}     # Diccionario para asociar cursos con las notas

# Menú principal
def menu_inicio():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("¡Adiós!")
            break
        else:
            print("Por favor, selecciona una opción válida.")
#us001
# Registrar un nuevo usuario
def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    rol = input("Rol (profesor/estudiante): ").lower()

    if usuario in usuarios:
        print("El usuario ya existe.")
    else:
        if rol in ["profesor", "estudiante"]:
            usuarios[usuario] = contraseña
            roles[usuario] = rol
            cursos[usuario] = []  # Inicializamos una lista de cursos vacía para el usuario
            print(f"Usuario '{usuario}' registrado exitosamente como {rol}.")
        else:
            print("Rol no válido. El usuario no se ha registrado.")

#us002
# Iniciar sesión
def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if usuarios.get(usuario) == contraseña:
        print(f"Bienvenido, {usuario}!")
        menu_usuario(usuario)
    else:
        print("Usuario o contraseña incorrectos.")

# Menú del usuario según su rol
def menu_usuario(usuario):
    while True:
        print("\n--- Menú del Usuario ---")
        if roles[usuario] == "profesor":
            print("1. Crear Curso")
            print("2. Registrar Nota")
            print("3. Ver Cursos")
            print("4. Salir")
        elif roles[usuario] == "estudiante":
            print("1. Ver Cursos")
            print("2. Consultar Nota")
            print("3. Salir")

        opcion = input("Elige una opción: ")

        if roles[usuario] == "profesor":
            if opcion == "1":
                crear_curso(usuario)
            elif opcion == "2":
                registrar_nota(usuario)
            elif opcion == "3":
                ver_cursos(usuario)
            elif opcion == "4":
                print(f"Adiós, {usuario}.")
                break
            else:
                print("Por favor, selecciona una opción válida.")
        elif roles[usuario] == "estudiante":
            if opcion == "1":
                ver_cursos(usuario)
            elif opcion == "2":
                consultar_nota(usuario)
            elif opcion == "3":
                print(f"Adiós, {usuario}.")
                break
            else:
                print("Por favor, selecciona una opción válida.")