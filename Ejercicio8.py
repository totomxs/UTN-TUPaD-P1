#Ejercicio8

contPARES = 0
contIMPARES = 0
contPOSITIVOS = 0
contNEGATIVOS = 0

cantidadNUM = 100  #Cambiar el valor de esta variable para chequear el código.


for i in range (cantidadNUM):
    num = int(input("Ingrese un número entero: "))
    if num == 0:
        continue  #ignora el valor 0 ya que éste no está dentro de ninguna de las 4 categorías.    
    if num % 2 == 0:
        contPARES += 1
    else:
        contIMPARES += 1
    if num > 0:
        contPOSITIVOS += 1
    elif num < 0:
        contNEGATIVOS += 1
   

print(f"La cantidad de números pares es {contPARES};")
print(f"La cantidad de números impares es {contIMPARES};")
print(f"La cantidad de números positivos es {contPOSITIVOS};")
print(f"La cantidad de números negativos es {contNEGATIVOS}.")