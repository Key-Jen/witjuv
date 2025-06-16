#from prettytable import PrettyTable

#table = PrettyTable()

#table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#table.add_rows(
#    [
#        ["Adelaide", 1295, 1158259, 600.5],
#        ["Brisbane", 5905, 1857594, 1146.4],
#        ["Darwin", 112, 120900, 1714.7],
#        ["Hobart", 1357, 205556, 619.5],
#        ["Sydney", 2058, 4336374, 1214.8],
#        ["Melbourne", 1566, 3806092, 646.9],
#        ["Perth", 5386, 1554769, 869.4],
#    ]
#)
#print(table)

animales = [
    ["Mamiferos",["Vaca lechera", "Hamster dorado", "Pony salvaje", "Chancho con chaleco"]],
    ["Reptiles",["Cobra kai","Balano","Dragon de comodo","Mamba negra"]],
    ["Aves",["Pato", "Pinguinos", "Canarios", "Gallina"]]
]


for i in range(len(animales)):
    for x in range(len(animales[i][1])):
        print(animales[i][1])


lista_comida = ["Lasaña", "Pollo Arvejado","Curanto","Sopaipilas pasadas"]
# 1.- Imprimir la cantidad de elementos de lista
# 2.- Imprimir la lista completa de comidas
# 3.- Imprimir todas las comidas una a una
# 4.- Preguntar al usuario que comida busca

for animal in animales:
    print(animal[0])
    for animalito in animal[1]:
        print(animalito)

