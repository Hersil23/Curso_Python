'''
ejercicio 1
'''
'''
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion a realizar (+, -, *, /): ")

if operacion == '+':
  resultado = num1 + num2

elif operacion == '-':
  resultado = num1 - num2

elif operacion == '*':
  resultado = num1 * num2

elif operacion == '/':
	if num2 != 0:
		resultado = num1 / num2
	else:
		resultado = "Error: Division por cero"
else:
  resultado = "Operacion no valida"

print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
'''
'''
ejercicio 2: calcula el area de un circulo con un radio dado
'''
'''
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14159 * radio**2
print(f"El area del circulo de radio {radio} es: {area}")

'''
'''
ejercicio 3: concatena dos cadenas de texto
'''
'''
cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(f"La cadena concatenada es: {cadena_concatenada}")
'''
'''
Ejercicio 4: crear lista con diferentes elemento e imprimierla

'''
'''
lista1 = [1, "dos", 4.5, True, "cinco"]
print("La lista es:", lista1)

ejercicio 5(7):  calcula el promedio de una lista de numeros


lista_numeros = [10, 20, 30, 40, 50]
promedio = sum(lista_numeros) / len(lista_numeros)
print(f"El promedio de la lista es: {promedio}")

print(len(lista_numeros))

ejercicio 6(10): imprime una cadena de texto inversa

""" 
cadena = "Herasi"
cadena_inversa = cadena[::-1]
print(f"La cadena inversa de {cadena} es: {cadena_inversa}")

ejercicio 7(13): reemplaza un caracter de una cadena de texto
'''
'''
cadena = "Herasi"
cadena_modificada = cadena.replace("H", "J")
print(f"La cadena modificada es: {cadena_modificada}")

ejercicio 9(16): imrime una lista de numeros de menor a mayor

'''
'''
lista_numeros = [10,2,4,7,5,0,3]
lista_numeros.sort()
print(f"La lista de numeros de menor a mayor es: {lista_numeros}")

ejercicio 10(19): imprime  cuenta las ocurrenias de un caracter en especifico en una cadena de texto

'''
'''
cadena = "HerasiPalabras"
caracter = "a"
ocurrencias = cadena.count(caracter)
print(f"El caracter '{caracter}' aparece {ocurrencias} veces en la cadena.")

'''
'''
numero = int(input("Ingrese un numero: "))

if numero >0:
  print(f"El numero {numero} es positivo.")
elif numero < 0:
  print(f"El numero {numero} es negativo.")
else:
  print("El numero es cero.")

ejercicio 41 imprime los numeros del 10 al 1 en orden descendente

'''
'''
for i in range(10, 0, -1):
  print(i)
'''

import random
numero_secreto = random.randint(1, 20)
intentos = 0

while True:
  intento = int(input("Adivina el numero secreto entre 1 y 20: "))
  intentos = intentos + 1 
  if intento == numero_secreto:
    print(f"Felicidades! Adivinaste el numero secreto {numero_secreto} en {intentos} intentos.")
    break
  elif intento < numero_secreto:
    print("El numero secreto es mayor.")
  else:
    print("El numero secreto es menor.")
  
