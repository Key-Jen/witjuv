import hashlib

def hash_md5(texto):
    #convertir el texto a byte
    texto_bytes = texto.encode()
    #creamos el hash (objeto)
    hashmd5 = hashlib.md5(texto_bytes)
    return hashmd5.hexdigest()

#pp
frase = input("ingrese una frase: ")
elhash = hash_md5( frase )
print("La huella digital es: ", elhash)

