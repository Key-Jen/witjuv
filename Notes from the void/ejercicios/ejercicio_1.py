# Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable
# luego le pido al usuario que ingrese la contraseña y el sistema debe indicar por pantalla
# si la contraseña ingresada es correcta

def validacion_contraseña(contraseña_usuario):
    contraseña = "todos_juntos"
    if contraseña_usuario == contraseña:
        print("Contraseña correcta.")
    else:
        print("Contraseña Incorrecta.")

contraseña_ingresada = input("Ingrese su contraseña: ")
validacion_contraseña(contraseña_ingresada)