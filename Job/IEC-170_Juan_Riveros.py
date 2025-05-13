#Sistema de gestion de inventario para una tienda
#Autor: Jota
#Historial
import Version.version
 
def fn_get_num_valido(mensaje):
    """
    funcion para validar el ingreso de un valor numérico.
    No termina hasta que el valor ingresado es válido
    """
    validos = ["0","1","2","3","4","5","6","7","8","9","-","."]
    malopos = False
    repite = True
    num = 0
    while repite:
        num = input( mensaje )
        l = len( num ) #obtener el largo
        malochar = False
        malog = False
        contg = 0
        contp = 0
        for i in range( l ):
            if not num[i] in validos:
                malochar = True
            if num[i] == "-":
                contg = contg+1
            if num[i] == ".":
                contp = contp+1
        malopos = contg == 1 and  num[0] != "-"
        malog = contg > 1
        malop = contp > 1
        if malochar or malog or malopos or malop:
            repite = True
            print("La entrada no es válida")
        else:
            repite = False
    numero = float(num)
    return(numero)
    #fn_get_valida_num

def fn_mostrar_producto(prod, precio, stock):
    """
    `uso`: muestra un producto del inventario;
    `entrada`: nombre, precio y cantidad del producto;
    `retorna`: nada;
    """
    print(f"Producto: {prod}") 
    print("Precio: %5.2f" % precio) 
    print(f"Stock: {stock}")
    print("=====================================")  
    #mostrar_producto()

def fn_buscar(lista, nombre):
    esta = False
    i = 0
    l = len (nombre)
    while i < l and not esta:
        if lista[i].upper() == nombre.upper():
            esta = True
        else:
            i = i + 1
    if esta:  #si lo encuentra "esta" vale True
        return i    #retornamos la posicion donde lo halló
    else:
        return -1    #retornamos -1 si no lo encuentra
    #buscar()
# Vi la primera funcion y como se construyo desde 0...
# Deberia entender las otras 2 pero no me pregunti wn preguntale a la mari y a la abril


#PROGRAMA PRINCIPAL (PP)

#listas para administrar los productos
try:            #TRY???!?!?
    print(f"*** Menú {Version.version.version}")
    lnombre = ["Plumon", "Borrador","Pizarra"]
    lprecio = [1200, 3500, 10500]
    lstock = [20,8,3]


    salir = False
    while not salir:
        print(" *** Menú *** ")
        print("[1] Agrega producto")
        print("[2] Listar producto")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("Opcion: ")

        #******* agrega producto
        if (op == "1"):
            nom = input("Nombre del producto: ")        #Entiendo la logica de las funciones pero just in case wtf is this
            lnombre.append(nom)
            precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: "))
            lprecio.append(precio)
            canti = fn_get_num_valido("Cantidad del Producto: ") #int(input("Cantidad del producto: "))
            lstock.append(int(canti))
            print(f"Se ha agregado {nom}, con el precio {precio} y el stock {canti}")

        #******* Listar
        if (op == "2"):
            largo = len (lnombre)
            for i in range(largo):
                fn_mostrar_producto(lnombre[i],lprecio[i],lstock[i])

        #******* Buscar por nombre
        if (op == "3"):
            nom = input("Nombre del producto a buscar: ")
            pos = fn_buscar (lnombre, nom)
            if pos == -1:
                print(f"El Producto {nom} no esta en el inventario")
            else:
                fn_mostrar_producto(lnombre[pos],lprecio[pos],lstock[pos])

        #******* Eliminar producto por nombre   
        if (op == "4"):
            nom = input("Nombre del producto a Eliminar :evil_imp: : ")
            pos = fn_buscar(lnombre, nom)
            if pos != -1: #Indica que el producto si está
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Estai seguro waton? [si/no]")
                if resp.upper() == "SI":
                    del lnombre[pos]
                    del lprecio[pos]
                    del lstock[pos]
                    print(f"Producto {nom} eliminado :pensive_sob:.")
                else: 
                    print("Te salvaste waton...")
            else:
                print(f"El producto {nom} no existe dumbass!!! :P")
                    
        #******* Modificar cantidad
        if (op == "5"):
            nom = input("Nombre del producto a modificar :blush: : ")
            pos = fn_buscar(lnombre, nom)
            if pos == -1: #Indica que el producto NO está
                print(f"El producto {nom} no existe dumbass!!! :P")
            else:
                fn_mostrar_producto(lnombre[pos], lprecio[pos], lstock[pos])
                resp = input("Estai seguro waton? [si/no]")
                if resp.upper() == "SI":
                    cant = fn_get_num_valido("Ingrese nueva cantidad: ")
                    lstock[pos] = int(cant)
                    print(f"Cantidad del producto {nom} modificada :thumb_up:.")
                else: 
                    print("Te salvaste waton...")

        #******* Salir
        if (op == "6"):
            salir = True
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")