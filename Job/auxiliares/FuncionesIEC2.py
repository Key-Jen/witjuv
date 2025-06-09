from auxiliares.FuncionesIEC import *

def fn_guardar_inventario(lnom,lpre,lsto):
    with open ("inventario.txt", "w", encoding = "utf-8") as inventario:
        largo = len(lnom)
        for i in range(largo):
            inventario.write(lnom[i]+"\n")
            inventario.write(str(lpre[i])+"\n")
            inventario.write(str(lsto[i])+"\n")
        print("Inventario guardado en inventario.txt")

def fn_cargar_inventario(lnom,lpre,lsto):
    try:
        with open ("inventario.txt", "w", encoding = "utf-8") as inventario:
            lineas = inventario.readlines()
            largo = len (lineas)
            for i in range(0, largo,3):
                nom = lineas[i].strip()
                pre = float(lineas[i+1].strip())
                sto = int(lineas[i+2].strip())
                lnom.append( nom )
                lpre.append( pre )
                lsto.append( sto )
                print("Inventario cargado exitosamente :3")
    except FileNotFoundError:
        print("No se encontro el inventario, usando por defecto")
        lnom = ["Plumon","Borrador","Pizarra"]
        lpre = [1200.0, 3500.0, 13500.0]
        lsto = [20,8,10]
    except Exception as err:
        print("Error al cargar inventario:", err)