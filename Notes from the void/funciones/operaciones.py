
def op_suma(num1,num2):
    return num1 + num2

def op_resta(num1,num2):
    return num1 - num2

def op_multiplicacion(num1,num2):
    return num1 * num2

def op_division(num1,num2):
    if num2 == 0:
        print("No se puede dividir por 0")
        return None
    else:
        return num1 / num2