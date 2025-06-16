import math
# Funciones con numeros

numeros = [4,6,2,9,25]

print(f"el numero mayor es: {max(numeros)}")
print(f" El numero menor es: {min(numeros)}")

numero = 12.3456
print()
print(f"Redondear un decimal {numero} = {round(numero)}")
print(f"Redondear un decimal {numero} = {round(numero,2)}")
print(f"Truncar un decimal {numero} = {math.trunc(numero)}")
print(f"Aproximar al entero superior el numero {numero} = {math.ceil(numero)}")
print(f"Valor absoluto de -45: {math.fabs(-45)}")
print(f"Raiz cuadrada de 25 = {math.sqrt(9)}")
print(f"Sumatoria de 4+6+2+9+25 = {math.fsum(numeros)}")
