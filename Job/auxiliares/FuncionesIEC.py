from auxiliares.validacion_num import *
from auxiliares.FuncionesIEC2 import *

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

def fn_agregar_producto(lnombre, lprecio, lstock):
    nom = input("Nombre del producto: ")        #Entiendo la logica de las funciones pero just in case wtf is this
    lnombre.append(nom)
    precio = fn_get_num_valido("Precio del producto: ") #float(input("Precio del producto: "))
    lprecio.append(precio)
    stock = fn_get_num_valido("Cantidad del Producto: ") #int(input("Cantidad del producto: "))
    lstock.append(int(stock))
    print(f"Se ha agregado {nom}, con el precio {precio} y el stock {stock}")


def fn_listar(lnombre,lprecio,lstock):
    largo = len (lnombre)
    for i in range(largo):
        fn_mostrar_producto(lnombre[i],lprecio[i],lstock[i])


def fn_buscar(lnombre,lprecio,lstock):
    nom = input("Nombre del producto a buscar: ")
    pos = fn_buscar (lnombre, nom)
    if pos == -1:
        print(f"El Producto {nom} no esta en el inventario")
    else:
        fn_mostrar_producto(lnombre[pos],lprecio[pos],lstock[pos])

def fn_borrar(lnombre,lprecio,lstock):
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

def fn_modificar(lnombre,lprecio,lstock):
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
