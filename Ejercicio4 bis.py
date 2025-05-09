sumatoria = 0  
numero = 0  

while True:  # Usamos un bucle infinito 
    entrada = input("Indique un número entero (ingrese 0 para cortar): ")
    
    if entrada == "0":
        break  # Salir del bucle (aunque no se recomienda usar break)
    
    try:
        numero = int(entrada) 
        sumatoria += numero  # Acumulamos el número
    except ValueError:
        print("Debe ingresar un número entero válido")

print(f"La sumatoria de los números ingresados es {sumatoria}.")