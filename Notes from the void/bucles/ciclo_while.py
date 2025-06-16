# El ciclo while que signifa mientras, nos permite ejecutar una serie de 
# acciones mientras una condicion logica sea VERDADERA

contador_str = input("Ingrese un numero entero menor a 50: ")
contador_int = int(contador_str)

while contador_int < 50:
    contador_int = contador_int + 1
    print(f"Su contador es: {contador_int}")

print(f"Ciclo terminado, Usted ingreso el número: {contador_str}")