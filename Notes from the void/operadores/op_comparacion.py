numero_1 = 5
nuemro_2 = 4

# Operador equivalente
equivalente = numero_1 == 5
print(equivalente)

contraseña_guardada = "pepito_paga_doble"
ingreso_contraseña = input("Ingrese su contraseña")
acceso = ingreso_contraseña == contraseña_guardada

if acceso == True:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Operador distinto de 
op_distinto = numero_1 != nuemro_2
print(f"Operador distinto que: {op_distinto}")

# Operador mayor que
op_mayor_que = numero_1 > nuemro_2
print(f"Operador mayor que: {op_mayor_que}")

# Operador mayor o igual que
op_mayor_igual_que = numero_1 >= nuemro_2
print(f"Operador mayor o igual que: {op_mayor_igual_que}")

# Operador menor que
op_menor_que = numero_1 < nuemro_2
print(f"Operador menor que: {op_menor_que}")

# Operador menor o igual que 
op_menor_igual_que = numero_1 <= nuemro_2
print(f"Operador menor o igual que: {op_menor_igual_que}")
