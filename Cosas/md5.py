import hashlib

#def hash_md5(texto):
#    #convertir el texto a byte
#    texto_bytes = 
#    #creamos el hash (objeto)
#    hashmd5 = hashlib.md5(texto_bytes)
#    return hashmd5.hexdigest()

#pp
print(hashlib.md5("123456".encode()).hexdigest() )


import bcrypt
print(bcrypt.hashpw("123456".encode(), bcrypt.gensalt()))