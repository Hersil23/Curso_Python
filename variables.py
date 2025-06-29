#Un comentario de linea es uno que solo abarca una linea

"""
Esto es un comentario 
de varias 
lineas
"""

#Variables

""" Es una forma de almacenar un valor en memoria. """

name = "Delvis"

#Tipos de datos

#Enteros (numeros enteros)

age = 23

#Flotantes (numeros decimales)

height = 1.75

#Enteros negativos (numeros enteros negativos)

vision = -2

#Flotantes negativo (numeros decimales)

temp = -1.75

#Textos (cadenas de caracteres "Strings")

lastName = "Tengo 23 años"

#Booleanos (Verdadero o falso)

isStudent = True

isEmployed = False

#Listas (colecciones de elementos)

fruits = ["apple", "banana", "cherry","orange"]

numbers = [1, 2, 3, 4, 5]

students = ["Jesus", "Cris", "Jean"]

components =["CPU", "RAM", "GPU",["SSD", "HDD"]]

#Tuplas (colecciones inmutables de elementos)

fruits = ("apple", "banana", "cherry")

numbers = (1, 2, 3, 4, 5)

#Diccionarios (colecciones de pares clave-valor)

student = {
  "name": "",
  "age": 0,
  "isStudent": True
}

name1, lastName, age = "Hola mundo", "Sanabria", 23

#Salida de datos

#print nos sirve para la salida de datos por consola
print(name1)

#Entrada datos

#input() nos permite pedirle datos al usuario por consola, es decir permite la entrada
#de datos a mi aplicacion

name2 = input("Ingrese su nombre: ")
print("Hola " + name2)

#¿Que pasa si yo quiero que el usuario ingrese un numero?

age2 = int(input("Ingrese su edad: "))
#str es una funcion que convierte un numero a texto
print("Tu edad es: " + str(age2))