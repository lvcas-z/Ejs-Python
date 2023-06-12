import math

# 1) Cálculo del área de un círculo:
'''Escribe un programa que solicite al usuario el radio de un círculo y calcule el área utilizando la fórmula:
área = pi * radio^2. Imprime el resultado del cálculo.
'''

radio = int(input("Ingrese el radio de del circulo"))
area = math.pi * radio**2
circunferencia = 2 * math.pi * radio

print(f"El area del circulo es :  {area} ")
print(f"La circunferencia del circulo es :  {circunferencia} ")


# 2) Promedio de 3 notas
'''Consiste en escribir un programa en Python que solicite al usuario ingresar tres notas y calcule el promedio de las mismas. 
El programa debe imprimir el resultado del promedio.
'''

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("El promedio de las tres notas es:", promedio)

# 3) Conversión de grados Celsius a Fahrenheit:
'''Escribe un programa que solicite al usuario una temperatura en grados Celsius y la convierta a grados Fahrenheit 
utilizando la fórmula: F = (C * 9/5) + 32. Imprime el resultado de la conversión.
'''

celsius = float(input("Ingrese una temperatura en grados Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# 4) Calculadora de área y perímetro de un rectángulo:
'''Escribe un programa que solicite al usuario ingresar la longitud y el ancho de un rectángulo y 
calcule el área y el perímetro utilizando las fórmulas: área = longitud * ancho 
y perímetro = 2 * (longitud + ancho). Imprime los resultados del área y el perímetro.
'''

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

area = longitud * ancho
perimetro = 2 * (longitud + ancho)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")