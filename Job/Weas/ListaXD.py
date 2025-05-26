lista_estudiantes = [
    ['Armando casas',[['Biología',[4.5,5.6,6.7,7.0]],['Fisica',[4.5,5.6,6.7,7.0]],['Quimica',[4.5,5.6,6.7,7.0]]]],
    ['Aquiles Baeza',[['Biología',[5.6,6.5,5.0,5.9]],['Fisica',[5.6,6.5,5.0,5.9]],['Quimica',[5.6,6.5,5.0,5.9]]]],
    ['Delfin Quispe',[['Biología',[4.5,3.9,4.7,4.0]],['Fisica',[4.5,3.9,4.7,4.0]],['Quimica',[4.5,3.9,4.7,4.0]]]],
    ['Wendy Sulca',[['Biología',[4.5,5.0,4.8,5.1]],['Fisica',[4.5,5.0,4.8,5.1]],['Quimica',[4.5,5.0,4.8,5.1]]]],
    ['Dolores de Cabeza',[['Biología',[5.6,4.7,6.2,6.4]],['Fisica',[5.6,4.7,6.2,6.4]],['Quimica',[5.6,4.7,6.2,6.4]]]]
]

for estudiante in lista_estudiantes:
    print()
    print('------------------------------------------------------------------')
    print(f'Nombre: {estudiante[0]}')
    print()
    for asignatura in estudiante[1]:
        print()
        print(f'{asignatura[0]} : {asignatura[1]}')
        print()
        print()
        can_not = len(asignatura[1])
        suma = 0
        for notas in asignatura[1]:
            suma = suma + notas
        print(suma / can_not)
        suma = 0
            