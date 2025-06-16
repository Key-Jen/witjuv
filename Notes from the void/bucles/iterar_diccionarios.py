diccionario = {
    "nombre":"Constanza",
    "apellido":"Paillal",
    "edad":21,
    "estudiante":True
}

for clave in diccionario:
    print(f"La clave es: {clave}")

print()
for dato in diccionario.items():
    clave = dato[0]
    valor = dato[1]
    print(f"La clave es: {clave} y el valor es: {valor}")