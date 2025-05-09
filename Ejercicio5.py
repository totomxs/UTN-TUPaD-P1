#Ejercicio5

import random  #Función que permite generar números aleatorios

numadiv = random.randint(0 , 9)

intentos = 0   #Se inicializa el contador.

while True:
    num = int(input("Adivine el número en cuestión (0 - 9): "))
    intentos += 1
    if num == numadiv:
        print("¡Adivinaste, felicitaciones")
        break            #Corta el bucle en caso de adivinar el número.
    else:
        print ("Seguí participando.")

print(f"Necesitaste {intentos} para ganar el juego.")        