import operaciones

def Bienvenida():
    print()
    print("*** Super Calculadora Python")
    print("============================")
    print()

def menu():
    print()
    print("Selecciona su Operacion")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicacion")
    print("4: Division")
    print("0: Salir")
    print()

def ejecutar_calculadora():
    Bienvenida()
    while True:
        print()
        num_1 = float(input("Ingrese Numero 1: "))
        num_2 = float(input("Ingrese Numero 2: "))
        menu()
        opcion = input("Seleccione su opcion (0-4): ")

        resultado = 0
        operacion = ""

        if opcion == "1":
            resultado = operaciones.op_suma(num_1,num_2)
            operacion = "+"
        elif opcion == "2":
            resultado = operaciones.op_resta(num_1,num_2)
            operacion = "-"
        elif opcion == "3":
            resultado = operaciones.op_multiplicacion(num_1,num_2)
            operacion = "*"
        elif opcion == "4":
            resultado = operaciones.op_division(num_1,num_2)
            operacion = "/"
        elif opcion == "0":
            print("Saliendo del sistema... hacia otra galaxia...")
            break
        else:
            print("Opcion invalida... Vuelva a ingresar...")
            return
        
        if resultado == None:
            print("Operacio NO permitida.. no se puede dividir por cero")
        else:
            print(f"{num_1} {operacion} {num_2} = {resultado}")

ejecutar_calculadora()