#Sistema de gestion de inventario para una tienda
#Autor: Jota
#Historial
#09-06-25, Termine de depurar el programa, el 1 el 2 y el 6 funcionan de maravilla :'D
from version.version import version
from auxiliares.listas import lnombre, lprecio, lstock, fn_actualizar_lista
from auxiliares.validacion_num import fn_get_num_valido
from auxiliares.FuncionesIEC import *





#####################################PROGRAMA PRINCIPAL (PP)#######################################
###################################################################################################
#listas para administrar los productos
lnombre = []
lprecio = []
lstock = []
try:            #TRY???!?!?
   # print(f"*** Menú {version.version.version}")

    salir = False
    fn_cargar_inventario(lnombre,lprecio,lstock)
    while not salir:
        print(f" *** Menú {version} *** ")
        print("[1] Agrega producto")
        print("[2] Listar producto")
        print("[3] Buscar por nombre")
        print("[4] Eliminar producto")
        print("[5] Modificar cantidad")
        print("[6] Salir")
        op = input("Opcion: ")

        #******* agrega producto
        if (op == "1"):
          fn_agregar_producto(lnombre,lprecio,lstock)

        #******* Listar
        if (op == "2"):
            fn_listar(lnombre,lprecio,lstock)

        #******* Buscar por nombre
        if (op == "3"):
            fn_buscar(lnombre,lprecio,lstock)

        #******* Eliminar producto por nombre   
        if (op == "4"):
            fn_borrar(lnombre,lprecio,lstock)
                    
        #******* Modificar cantidad
        if (op == "5"):
            fn_modificar(lnombre,lprecio,lstock)


        #******* Salir
        if (op == "6"):
            salir = True
            fn_guardar_inventario(lnombre,lprecio,lstock)
            print("Hasta luego!")
except KeyboardInterrupt as error:
    print("\nUd. ha abandonado el programa por usar la combinacion Ctrl+C")