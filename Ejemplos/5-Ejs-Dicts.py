# 1) Información de contactos
'''Escribe un programa que solicite al usuario ingresar el nombre y número de teléfono de varias personas.
Luego, crea un diccionario donde las claves sean los nombres y los valores sean los números de teléfono.
Finalmente, muestra el diccionario resultante.
'''

# contactos={}


# while True :
#     nombre = input("Ingrese un nombre o 'SALIR' para terminar : ")
#     if(nombre=='SALIR'):
#         print("Saliste de la agenda")
#         break
#     num_telefono = input(f"Ingrese el numero de telefono de {nombre.capitalize()} ")
#     contactos[nombre]=num_telefono
#     break
# print(contactos)



# 2) Contar palabras en un texto
'''Escribe un programa que solicite al usuario ingresar un texto.
Luego, cuenta la cantidad de veces que aparece cada palabra en el texto y almacena esta información en un diccionario.
Finalmente, muestra el diccionario resultante.
'''

# texto = input("Ingrese un texto")
# palabras = texto.split()
# contador_palabras = {}
# for palabra in palabras:
#     if palabra in contador_palabras:
#         contador_palabras[palabra] += 1
#     else:
#         contador_palabras[palabra] = 1

# print(contador_palabras)



# 3) Información de productos
'''Escribe un programa que solicite al usuario ingresar información de varios productos, como nombre, precio y cantidad.
Luego, crea un diccionario para cada producto donde las claves sean el nombre, el precio y la cantidad, y los valores sean los valores ingresados.
Finalmente, muestra una lista con los diccionarios de los productos.
'''
productos = []
while True:
    nombre_producto = input("Ingrese el nombre del producto o 'SALIR' para finalizar el ingreso de productos ")
    if(nombre_producto=='SALIR'):
        print("Saliste de la aplicacion")
        break
    
    precio_producto = float(input(f"Ingrese el precio del producto "))
    cantidad_producto = int(input(f"Ingrese la cantidad del producto "))
    producto = {"nombre_producto": nombre_producto,"precio_producto": precio_producto,"cantidad_producto": cantidad_producto}
    productos.append(producto)

print(productos)

# 4) Calificaciones de estudiantes
'''Escribe un programa que solicite al usuario ingresar el nombre y la calificación de varios estudiantes.
Luego, crea un diccionario donde las claves sean los nombres de los estudiantes y los valores sean las calificaciones.
Finalmente, muestra el promedio de las calificaciones de todos los estudiantes.
'''

# estudiantes = {}
# while True :
#     nombre_estudiante = input("Ingrese el nombre del estudiante o 'SALIR' para finalizar ")
#     if(nombre_estudiante=='SALIR'):
#         print("Saliste de la aplicacion")
#         break
#     nota_estudiante  = float(input("Ingrese la calificacion"))
    
#     estudiantes[nombre_estudiante]=nota_estudiante
    
# promedio_estudiantes = sum(estudiantes.values()) / len(estudiantes)

# print(f"Estudiantes : {estudiantes}")
# print(f"Promedio total estudiantes : {promedio_estudiantes}")
