# Pida al usuario que ingrese su sueldo y 
# defina el monto de impuesto de segunta categoria que debe pagar a servicio de impuestos internos 

def definir_impuesto(sueldo):
    sueldo_int = int(sueldo)
    impuesto = 0

    if sueldo_int >=  8075200:
        impuesto = ((sueldo_int * 27.48)/100)
    elif sueldo_int >= 6056460 and sueldo_int > 8075200:
        impuesto = ((sueldo_int * 15.57)/100)
    elif sueldo_int >= 4710500 and sueldo_int > 6056460:
        impuesto = ((sueldo_int * 10.64)/100)
    elif sueldo_int >= 3364700 and sueldo_int > 4710500:
        impuesto = ((sueldo_int * 7.09)/100)
    elif sueldo_int >= 2018820 and sueldo_int > 3364700:
        impuesto = ((sueldo_int * 4.52)/100)
    elif sueldo_int >= 908469 and sueldo_int > 2018820:
        impuesto = ((sueldo_int * 2.20)/100)
    else:
        impuesto = 0
    print(f"El impuesto de segunda categoria a pagar con el sueldo de {sueldo_int} es: ${impuesto}")
    


sueldo_ingresado = input("Ingrese su sueldo: ")

definir_impuesto(sueldo_ingresado)