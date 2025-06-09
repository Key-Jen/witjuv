#with open("archivo.txt", "w") as archivo:
    #archivo.write("Esta es la primera linea del archivo\n")
    #archivo.write("Esta es la segunda\n")

    
   # archivo = open("archivoi.txt", "w", encoding = "utf-8")
   #input("revisa el contenido del archivo:")
    #archivo.write("otro contenido\n")
    #nput("entre medio:")
    #archivo.write("mas sin sentido\n")
    #input("revisa de nuevo:")
    #archivo.close()
    #input("revisa de nuevo:")

    #archivo = open("archivo.txt", "a", encoding = "utf-8")
    #archivo.write("otro mas contenido\n")
    #archivo.write("otro mas sin sentido\n")
    #archivo.close() 

    #archivo = open("archivo.txt", "r", encoding = "utf-8")
    #contenido = archivo.read()
    #print("Contenido del archivo: \n",contenido )

archivo = open("Cosas/archivo.txt", "r", encoding = "utf-8")
lineas = archivo.readlines()
numlin = len ( lineas)
for i in range(0,numlin):
    lin = lineas[i]
    print(i+1,"\t",lin)
        