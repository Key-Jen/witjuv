archivo = open("archivo.txt", "r", encoding = "utf-8")
lineas = archivo.readlines()
numlin = len ( lineas)
for i in range(0,numlin):
    lin = lineas[i]
    print(i+1,"\t",lin)