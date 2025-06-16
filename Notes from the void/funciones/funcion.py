# Definición de funciones
# Ejercicio 1
def saludar(nombre):
    print(f"Hola admirable {nombre}")

# Llamar a una funcion
print()
nombre = input("Ingrese su nombre: ")
saludar(nombre)

# Ejercicio 2
def sumar(a,b):
    resultado = a + b
    print(resultado)

print()
sumar(5,7)

# Ejercicio 3
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

print()
sumar(a,b)


# Ejercicio 4
def operar(num1,num2,op):
    resultado = 0
    if op == "+":
        resultado = num1 + num2
    elif op == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("No se puede dividir por 0")
            return
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    else:
        print("Operacion incorrecta...")
    print(f"{num1} {op} {num2} = {resultado}")