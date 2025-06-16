#import getpass
import pwinput

usuario = input("usuario: ")
clave = pwinput.pwinput(prompt="clave: ",mask="_")

if usuario == "admin" and clave == "123456":
    print("Correcto!.")
else:
    print("Acceso denegado :P.")

print(f"las credenciales son {usuario} y {clave}")











#                                             Para integridad de los datos y contraseña
#                                                               |
# Funciones de Hash    ---------------------> siempre tienen el mismo largo (MD5, SHA 256)          HASH
#                                             IRREVERSIBLE
#                                             
# Funciones de Cifrado ---------------------> Largo variable                                 
#                                             Reversible (si tiene la clave)                        Cypher Text
#                                             AES, DES, Fernet                                      Texto Cifrado
#                                                     |
#                                             Seguridad (Privacidad en la WEB)
#                                             Para mantener incognito un Mensaje/Archivo
