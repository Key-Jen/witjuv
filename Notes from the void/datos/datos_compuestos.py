# Datos compuestos son COLECCIONES de elementos o datos que pueden pertencer a una variable

#LISTAS, coleccion ORDENADA de elementos
lista = ["Constanza Paillal", 21, True]
print(lista)
print(type(lista))
print(lista[0])
lista[0]= "Constanza Paillal"
print(lista)

# DICCIONARIO, colecciones ORDENADA de pares de elementos mutables
diccionario = {
    "nombre":"Constanza Paillal",
    "edad": 21,
    "es estudiante": True
}
print(diccionario)
print(type(diccionario))
print(diccionario["nombre"])
diccionario["nombre"]="Constanza Paillal"
print(diccionario)

#CONJUNTO, coleccion desordenada de elementos
conjunto = {"Constanza Paillal", 21, True}
print(conjunto)
print(type(conjunto))
conjunto.add(78)
print(conjunto)
conjunto.pop()
print(conjunto)

# TUPLAS, colecciones inmutable de elementos
tupla = ("Constanza Paillal", 21, True)
print(tupla)
print(type(tupla))

print(tupla[0])