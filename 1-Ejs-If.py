# 1) Edad mínima para votar:
'''Escribe un programa que solicite al usuario su edad y determine si es elegible para votar en las elecciones. 
Si la edad es igual o mayor a 18, el programa deberá imprimir "Eres elegible para votar". 
De lo contrario, deberá imprimir "No eres elegible para votar".
'''
edad_minima = int(input("Ingrese su edad : "))

if(edad_minima>=18):
    print("Eres elegible para votar")
else:
    print("No eres elegible para votar")

    
# 2) Clasificación de notas:
'''Escribe un programa que solicite al usuario una calificación numérica (entre 0 y 100)
y lo clasifique en una categoría según los siguientes rangos:
90-100: "Excelente"
80-89: "Bueno"
70-79: "Regular"
60-69: "Suficiente"
Por debajo de 60: "Reprobado"
El programa debe imprimir la clasificación correspondiente según la calificación ingresada.
'''

calificacion_numerica = int(input("Ingrese su calificacion : "))

if(calificacion_numerica>=90):
    print("Excelente")
elif(calificacion_numerica>=80):
    print("Bueno")
elif(calificacion_numerica>=70):
    print("Regular")
elif(calificacion_numerica>=60):
    print("Suficiente")
else:
    print("Reprobado")

# 3)Comparación de números:
'''Escribe un programa que solicite al usuario dos números y determine cuál de ellos es mayor. 
El programa debe imprimir el número mayor o un mensaje indicando que ambos números son iguales si son iguales.
'''

num_1 = int(input("Ingrese el primer numero : "))
num_2 = int(input("Ingrese el segundo numero : "))

if(num_1>num_2):
    print(f"El primer numero es el mayor :  {num_1}")
elif(num_2>num_1):
    print(f"El segundo numero es el mayor : {num_2}")
else:
    print("Ambos numeros son iguales")

# 4) Categorización de números:
'''Escribe un programa que solicite al usuario un número y lo clasifique en una de las siguientes categorías:
Si el número es negativo: "Negativo"
Si el número es cero: "Cero"
Si el número es positivo: "Positivo"
El programa debe imprimir la categoría correspondiente según el número ingresado.
'''

num_clasificar = int(input("Ingrese un numero para saber su clasificacion : "))

if(num_clasificar>0):
    print("El numero es positivo")
elif(num_clasificar<0):
    print(f"El numero es negativo ")
else:
    print("El numero es cero")

#5 Dia de la semana
'''Escribe un programa que solicite al usuario un número del 1 al 7 representando un día de la semana. 
El programa debe imprimir el nombre del día correspondiente, por ejemplo, si el usuario ingresa 1, 
el programa debe imprimir "Lunes", y así sucesivamente.
'''
dia = int(input("Ingrese un dia de la semana : "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Número inválido. Ingrese un número del 1 al 7.")
