#Ejercicio 7

num = int(input("Ingrese un número entero positivo: "))
sumatoria = 0


for i in range (0 , num):
    sumatoria += i

print(f"La suma de los números comprendidos entre 0 y {num} es {sumatoria}.")