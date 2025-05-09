#Ejercicio2

numero = input("Introduzca un número entero: ")
digitos = len(numero.replace("-", ""))  #Para contar la cantidad de dígitos e ignorar un posible signo "-" si el número ingresado es negativo

print(f"El número {numero} tiene {digitos} dígitos.")

