# Operadores aritmeticos permiten realizar operaciones entre variables
numero_1 = 3
numero_2 = 7
numero_3 = 9

nombre = "Constanza"
apellido = "Paillal"

# Operador suma
Suma = numero_1 + numero_2
print(Suma)
contatenacion = nombre + " " + apellido
print(contatenacion)

# Operador resta
resta = numero_1 - numero_2
print(resta)

# Operador multiplicacion
multiplicacion = numero_1 * numero_2
print(multiplicacion)
multiplicar_texto = nombre * numero_1
print(multiplicar_texto)
exponente = numero_1 ** numero_2
print(exponente)

# Operador division
division = numero_3 / numero_1
print(division)
print(type(division))

division_baja = numero_3 // numero_2
print(division_baja)
print(type(division_baja))

# Mostrar con x cantidad de decimales
print(f"{numero_3 / numero_2: .4f}")

# Operador resto
op_resto = numero_3 % numero_2
print(op_resto)