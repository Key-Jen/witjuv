import math

pi = math.pi

# radio = float(input("Ingrese el radio: "))
# print()

def area_circunferencia(radio):
    area = pi * radio ** 2
    return area

def raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada

def ejecutar_codigo():
    print()
    radio = float(input("Ingrese el radio de la circunferencia: "))
    print()
    respuesta_1 = area_circunferencia(radio)

    numero = float(input("Ingrese un numero para calcular su raiz: "))
    print()
    respuesta_2 = raiz_cuadrada(numero)
    print(f"el area de la circunferencia de radio {radio} es: {respuesta_1}")
    print()
    print(f"la raiz cuadrada de {numero} es: {respuesta_2}")
    print()


ejecutar_codigo()



# area = pi * radio**2
# print(f"El area de la circunferencia con radio {radio} es: {area}")

# numero = float(input("Ingrese un numero: ""))

# raiz_cuadrada = math.sqrt(numero)

