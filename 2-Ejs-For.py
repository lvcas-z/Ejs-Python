#1)Imprimir los números del 1 al 10
'''Escribe un programa que utilice un bucle for para imprimir los números del 1 al 10 
en una línea separados por espacios.
'''

numeros = ""
for i in range(1,11):
    numeros += " "+str(i)

print(numeros)


#2)Suma de los elementos de una lista:
'''Dada una lista de números, escribe un programa que utilice un bucle for para calcular 
la suma de todos los elementos de la lista e imprimir el resultado.
'''

lista_num = [1,2,3,4,5]
suma = 0 
for suma_num in lista_num :
    suma += suma_num
    
print("La suma de los numeros es : ", suma)


#3)Contar las vocales en una cadena:
'''Dada una cadena de texto, escribe un programa que utilice un bucle for para contar el número de vocales
(a, e, i, o, u) presentes en la cadena e imprimir el resultado.
'''
cadena = "Murcielago"
contador=0
for letra in cadena : 
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        contador+=1

print(contador)


#4)Tabla de multiplicar:
'''Escribe un programa que solicite al usuario ingresar un número y utilice un bucle for para imprimir 
la tabla de multiplicar de ese número del 1 al 10.
'''

numero_tabla = int(input("Ingrese el numero de la tabla: "))
for i in range(1,10):
    print(f"{numero_tabla}*{i} = {numero_tabla * i}")
    