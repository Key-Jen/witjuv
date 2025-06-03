def fn_valida_num():
    num = 0
    while num <= 0:
        try:
            num = int(input("Ingrese un nro: "))
            if num <= 0:
                print("Debe ser Positivo")
        except:
            print("Entrada no válida")
    return  num




##pp
resp = fn_valida_num()
print("El numero es: ", resp)