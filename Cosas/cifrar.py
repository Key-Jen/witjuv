import bcrypt

palabra = input("Ingrese palabra o frase: ")
contrasena = palabra.encode("utf-8")
print("contrasena:", contrasena)
salero = bcrypt.gensalt()
hash_contrasena = bcrypt.hashpw(contrasena, salero) 
print(hash_contrasena)

otravez = input("Ingresela de vuelta: ")
otra_vez_b= otravez.encode("utf-8") #contraseña en formato byte
print("Coincide: ", bcrypt.checkpw(otra_vez_b, hash_contrasena))

#contra = otravez.encode("utf-8")
#print("contrasena 2:", contra)
#hash_contra = bcrypt.hashpw(contra,salero) 
#print(hash_contra)
