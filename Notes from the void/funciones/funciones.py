from operaciones import op_suma, op_resta, op_division, op_multiplicacion

respuesta = "SI"
while True:
    if respuesta.upper() == "SI":
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        operacion = input("Ingrese la operacion a realizar: ")
        
        if operacion == "+":
            resultado = op_suma(numero1,numero2)

        elif operacion == "-":
            resultado = op_resta(numero1,numero2)

        elif operacion == "*":
            resultado = op_multiplicacion(numero1,numero2)

        elif operacion == "/":
            resultado = op_division(numero1,numero2)
        print(resultado)
#        operar(numero1,numero2,operacion)
#        respuesta = input("¿Desea realizar otra operacion? Responda SI o NO: ")
    else:
        break

