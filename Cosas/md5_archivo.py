import hashlib


def calcular_md5_archivo(archi):
    hash_md5 = hashlib.md5()
    with open(ruta, "rb") as file:
        bloque = file.read(4096)
        while bloque != b"":        #la b es de byte
            hash_md5.update( bloque )
            bloque = file.read(4096)
    return hash_md5.hexdigest()


#pp
ruta = r"T:\Solicitudes instalacion Informatica 2025\Apache Hadoop\hadoop-3.4.1-src.tar.gz" #Archivos de prueba, el del escritorio se borra, thanks inacap.
ruta2 = r"C:\Users\informatica\Desktop\hadoop-3.4.1-src.tar.gz"
print(calcular_md5_archivo(ruta))
print(calcular_md5_archivo(ruta2))