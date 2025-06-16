# escribir un programa que pida la usuarios que escriba un numero entero e indique si el numero es impar o par

def par_impar(numero):
    if numero % 2 == 0:
        print(f"Su numero {numero} es par.")
    else:
        print(f"Su numero {numero} es impar.")


numero_ingresado = int(input("ingrese un numero entero: "))
par_impar(numero_ingresado)