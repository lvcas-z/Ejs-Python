import random


# 1)Contador descendente: 
'''Escribe un programa que solicite al usuario un número entero positivo y luego 
imprima en pantalla todos los números desde ese número hasta 1 en orden descendente.
'''
num_descendente = int(input("Ingrese un numero"))

while num_descendente > 1:
    num_descendente-=1
    print(num_descendente)    


# 2)Suma de números
''' Escribe un programa que solicite al usuario una serie de números enteros 
y calcule la suma de todos ellos. El programa debe dejar de solicitar números 
cuando el usuario ingrese un número negativo.
'''
num_suma = int(input("Ingrese un numero"))
suma = 0
while num_suma >=1 :
    suma+=num_suma
    print(suma)


# 3)Adivinar el número
'''Escribe un programa en el que el usuario debe adivinar un número generado aleatoriamente.
El programa debe solicitar al usuario que ingrese un número y luego proporcionar pistas(mayor o menor) 
hasta que el usuario adivine el número correcto
'''

num_adivinar = int(input("Ingrese un numero entre el 0 y el 10"))
num_random = random.randint(0,10)
# print(f"Soy el numero random : {num_random}") 
while num_adivinar is not num_random :
    if(num_adivinar>num_random):
        print("El numero a adivinar es menor")
        num_adivinar = int(input("Ingrese otro numero "))
    else:
        print("El numero a adivinar es mayor ")
        num_adivinar = int(input("Ingrese otro numero "))
print("Felicitaciones acertaste")

# 4)Tabla de multiplicar
'''Escribe un programa que solicite al usuario un número entero
y luego imprima la tabla de multiplicar de ese número, desde 1 hasta 10.
'''
num_tabla = int(input("Ingrese el numero de la tabla: "))
contador=0

while contador < 11:
    print(f"{num_tabla} * {contador} = {num_tabla*contador}")
    contador+=1