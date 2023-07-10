# 1) Agregar elementos a un conjunto
'''Escribe un programa que solicite al usuario ingresar una serie de números separados por espacios.
Luego, crea un conjunto con esos números y muestra el conjunto resultante.
'''

# num_separados = input("Ingrese una serie de numeros separados por espacios : ")
# separados = set(num_separados.split())
# print(separados)


# 2) Eliminar un elemento de un conjunto
'''Escribe un programa que cree un conjunto con algunos nombres de colores predefinidos.
Luego, solicita al usuario que ingrese un nombre de color y elimina ese color del conjunto.
Finalmente, muestra el conjunto resultante.
'''

# colores = {"rojo","verde","azul"}
# color_eliminar = input("Ingrese un color a eliminar: ")
# colores.remove(color_eliminar)
# print(colores)

# 3) Eliminar un elemento aleatorio de un conjunto
'''Escribe un programa que cree un conjunto con algunos números.
Luego, elimina y muestra un número aleatorio del conjunto.
'''

import random
num = {1, 2, 3, 4, 5}
num_eliminar = random.choice(list(num))
num.remove(num_eliminar)
print(num)

# 4) Vaciar un conjunto
'''Escribe un programa que cree un conjunto con algunos elementos.
Luego, vacía el conjunto y muestra el conjunto resultante (que estará vacío).
'''

conjunto = {1, 2, 3, 4, 5}
conjunto.clear()
print(conjunto)


# 5) Verificar si un conjunto es un subconjunto de otro
'''Escribe un programa que cree dos conjuntos, uno con los números del 1 al 5 y otro con los números del 1 al 10.
Luego, verifica si el primer conjunto es un subconjunto del segundo conjunto e imprime el resultado.
'''

conjunto1 = {1,2,3,4,5,6}
conjunto2 = {1,2,3,4,5,6,7,8,9,10}
es_subconjunto = conjunto1.issubset(conjunto2)
print(es_subconjunto)