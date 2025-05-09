#Ejercicio3

num1 = int(input("Ingrese un número aleatorio: "))
num2 = int(input("Ingrese otro número distinto y mayor al anterior: "))

sumatoria = 0
inicio = num1 + 1
final = num2 #no hace falta restarle uno porq la función range no incluye al valor final

if num2 > num1:
        for i in range(inicio,final):
            sumatoria = sumatoria + i   #hace que la sumatoria, inicializada en 0, se aplique para los valores dentro del rango
        print(f"La sumatoria entre de los números comprendidos entre {num1} y {num2} es: {sumatoria} ")
elif num2 == num1:
    print("Los números ingresados son iguales. Corrija eso por favor.")                
else:
    print(f"El {num2} es menor que {num1}. Por favor corrija eso.")