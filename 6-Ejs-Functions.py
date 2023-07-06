# 1) Calculadora de suma y resta:
'''Escribe una función llamada calculadora que tome dos números y una cadena que indique la operación a realizar ("suma" o "resta").
La función debe realizar la operación correspondiente y devolver el resultado.
'''

def calculadora():
    tipo_calculo = input("Ingrese 'SUMAR' o 'RESTAR' para definir la operacion correspondiente")
    a = float(input("Ingrese el primer numero"))
    b = float(input("Ingrese el segundo numero"))
    if(tipo_calculo == 'SUMAR'):
        print(f"La suma entre {a} + {b} es = {a+b}")
    elif(tipo_calculo == 'RESTAR'):
        print(f"La resta entre {a} - {b} es = {a-b}")
    else:
        print("Ingresaste un valor erroneo")

# calculadora()

# 2)Contador de palabras:
'''Escribe una función llamada contar_palabras que tome una cadena de texto como entrada y cuente cuántas palabras hay en ella.
La función debe devolver el número de palabras.
'''

def contador_palabras() :
    texto = input("Ingrese un texto... ")
    palabras = texto.split()
    cantidad_palabras = 0
    for palabra in palabras :
        cantidad_palabras +=1
    print(f"La cantidad de palabras son : {cantidad_palabras}")
    

# contador_palabras()

# 3)Conversión de temperatura:
'''Escribe una función llamada convertir_temperatura que tome una temperatura en grados Celsius y la convierta a grados Fahrenheit.
La fórmula de conversión es: Fahrenheit = Celsius * 9/5 + 32. La función debe devolver la temperatura en grados Fahrenheit.
'''

def convertir_temperatura_fahrenheit ():
    celsius = float(input("Ingrese la temperatura a convertir"))
    fahrenheit = celsius * 9/5 + 32
    print(f"La temperatura {celsius} en grados fahrenheit es : {fahrenheit}")

convertir_temperatura_fahrenheit()
