#que es una tupla? una tupla es un objeto inmutable que contiene una secuencia de elementos, se define con paréntesis
# para crear una tupla, usamos paréntesis y separamos los elementos por comas
mi_tupla = (1, 2, 3)

#metodos de tuplas

myTuple = ("Herasi", "Paula", "Javier", "Alejandro", "Jean", "Jorge", "Sergio", "Javier", "Javier", "Javier" )

# count(value) nos permite contar cuantas veces se repite un valor en la tupla
print(myTuple.count("Javier"))  # 4

# index(value) nos permite obtener el indice del primer elemento que coincide con el valor que le pasamos como parametro
print(myTuple.index("Javier"))  # 2

# index(value, start, end) nos permite obtener el indice del primer elemento que coincide con el valor que le pasamos como parametro,
# buscando desde el indice start hasta el indice end
print(myTuple.index("Javier", 2, 5))  # 2