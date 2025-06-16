from cryptography.fernet import Fernet

#generar clave
clave = Fernet.generate_key()
fernet = Fernet(clave)

#texto llano o plano
palabra = input("Ingrese texto a cifrar: ")

#cifrar
cifrado = fernet.encrypt(palabra.encode())
print("El cifrado queda asi: ", cifrado)

#descifrar
descifrado = fernet.decrypt(cifrado)
print("Descifrado: ", descifrado )
