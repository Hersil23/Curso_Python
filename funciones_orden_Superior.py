#Funciones de orden superior son funciones que pueden recibir otras funciones, y son creadas por el propio equipo de python

#Tambien tendremos las funciones generales que pueden ser usadas en cualquier parte de mi app, y fueron creadas por el equipo de python

#Funciones generales de Transformacion

#int() convierte un numero o cadena en un entero

print(int("10"))

#str() convierte un numero en una cadena

print(str(10))

#bool() convertir un numero o un string en un valor booleano

print(bool(0))

#dict() Crear un nuevo diccionario

print(dict(name="Delvis", age=23, country="Venezuela"))

#float() convierte un numero o una cadena en un valor de punto flotante

print(float(10))

#list() convierte un objeto iterable en una lista

print(list(("Delvis","Herasi","Norland","Cris","Javier")))

#tuple() convierte un objeto iterable en una tupla

print(tuple([1,2,3,4,5]))

#De busqueda

#max() devuelve el valor maximo de un objeto iterable

print(max([1,2,3,4,5]))

print(max(["Delvis","Herasi","Norland","Cris","Javier"]))

#min() devuelve el valor minimo de un objeto iterable

print(min([1,2,3,4,5]))

print(min(["Delvis","Herasi","Norland","Cris","Javier"]))

#sum() Devuelve la suma de los elementos de un iterable

print(sum([1,2,3,4,5]))

#round() redondea un numero al entero mas cercano

print(round(1.5))


#type() devuelve el tipo de un objeto

print(type(1))

print(type("Delvis"))

print(type([1,2,3,4,5]))

print(type({"name":"Delvis","age":23,"country":"Venezuela"}))

#range() devuelve una secuencia de numeros

print(list(range(5)))

print(list(range(1,5)))

print(list(range(1,10,2)))


#abs() devuelve el valor absoluto de un numero

print(abs(-10))

#all(list) Devuelve True si todos los elementos de la lista son verdaderos

print(all([True, True, True]))

print(all([True, False, True]))

print(all(["Delvis","Herasi","Norland","Cris",""]))

#any(list) Devuelve True si al menos un elemento de la lista es verdadero

print(any([True, True, True]))

print(any([True, False, True]))

print(any(["Delvis",""]))

#eval(str) Evalua una cadena de texto como una expresion de python

print(eval("2 + 2"))

#hex(): convertir un valor en una cadena hexadecimal

print(hex(10))


#Funciones de Orden Superior

#enumarate(): devuelve una tupla con el indice y el valor de un objeto iterable

myList = ["Delvis","Herasi","Norland","Cris","Javier"]

enumerar = enumerate(myList)

print(list(enumerar))


#sorted(): Devuelve una lista ordenada

print(sorted([2,4,47,7,35,3,7]))

print(sorted(["Delvis","Herasi","Norland","Cris","Javier"], reverse=True))


#map(function, iterable): Aplica un procedimiento previamente definido a cada uno de los elementos de una secuencia

myList = [1,2,3,4,5]

def multiply_by_2(x):
  return x * 2

print(list(map(multiply_by_2, myList)))

print(list(map(lambda x: x * 2, myList)))

#filter(function, iterable):Crea una lista con los elementos de otra lista, que cumplan cierta condicion

numbers = [12,235,3,4,5,34,56,678,95,10]

def is_even(x):
  return x % 2 == 0

even_numbers = list(filter(is_even, numbers))

print(even_numbers)

print(list(filter(lambda x: x % 2 == 0, numbers)))

