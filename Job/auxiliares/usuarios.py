import bcrypt
import pwinput  
import pickle

def fn_hashear_clave(clave):
    clave_byte = clave.encode()
    clave_hash = bcrypt.hashpw(clave_byte, bcrypt.gensalt())
    return clave_hash

def fn_crear_usuario(users):
    print("Crear Usuario")
    cuenta = input("Ingrese nombre de usuario: ").strip()
    if cuenta in users:
        print("El nombre esta ocupado you dumb fck")
    else:
        clave = pwinput.pwinput("contraseña: ")
        clave2 = pwinput.pwinput("contraseña: ")
        if clave == clave2:
            users[cuenta] =fn_hashear_clave(clave)
            print("Usuario creado con exito")
        else:
            print("Las contraseñas no coinciden pendejo, no creare esa cuenta")

def fn_eliminar_usuario(users):
    print("Eliminar Usuario")
    cuenta = input("Ingrese el nombre de usuario: ").strip()
    if cuenta not in users:
        print("el usuario {} no existe tonto".format(cuenta))
    else:
        confirmation = input(f"Esta seguro de eliminar la cuenta {cuenta} ? [si/no] ").lower().strip()
        if confirmation == "si":
            del users[cuenta]
            print("Usuario {} eliminado".format(cuenta))
        else:
            print("El usuario {} no ha sido eliminado lol".format(cuenta))

def fn_cambiar_clave(users):
    print("Cambiar contraseña")
    cuenta = input("Cuenta?: ").strip()
    if cuenta in users:
        clave = pwinput.pwinput("Contraseña: ")
        clave2 = pwinput.pwinput("Repita contraseña: ")
        if clave == clave2:
            users[cuenta] = fn_hashear_clave(clave)
            print("Contraseña cambiada")
        else:
            print("las contraseñas son diferentes, no se realizaron cambios")
    else:
        print(f"Las cuenta {cuenta} no existe.")

def fn_guardar_usuarios(users):
    with open("usuarios.bin", "wb") as archivo:
        pickle.dump(users, archivo)
    print("Lista de usuarios actualizada")


def fn_cargar_usuarios():
    try:
        with open("usuarios.bin","rb") as archivo:
            return pickle.load(archivo)
    except FileNotFoundError:
        return {}

def fn_clave_valida(clave_plana, clave_guardada):
    bcrypt.checkpw(clave_plana.encode(), clave_guardada)

def fn_valida_usuario()
    users = fn_cargar_usuarios()
    if not users:
        return None
    
    cuenta = input("Usuario : ").strip()
    if cuenta not in users:
        print("La cuenta no existe, trata de usar alguna que si lo haga, genio.")
        return None
    
    clave = pwinput.pwinput("Contraseña por favor: ")
    if fn_clave_valida(clave,users[cuenta]):
        print(f"Bienvenid@ {cuenta}")
        return cuenta
    else:
        print("Contraseña incorrecta fucker")

#pp
usuarios = {}
usuarios = fn_cargar_usuarios()
salir = False
while not salir:
    print("***GESTION DE USUARIOS***")
    print("[1] Crear usuario")
    print("[2] Eliminar usuario")
    print("[3] Cambiar contraseña")
    print("[4] Lista usuarios")
    print("[5] Salir")
    op = input("Opcion: ")
    if op == "1":
        fn_crear_usuario(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "2":
        fn_eliminar_usuario(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "3":
        fn_cambiar_clave(usuarios)
        fn_guardar_usuarios(usuarios)

    if op == "4":
        print("Lista de Usuarios registrados: ", list(usuarios.keys()))


    if op == "5":
        fn_guardar_usuarios(usuarios)
        salir = True
print("Hasta la proximaaaaaaaaa")

    
    












