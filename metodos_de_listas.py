#Un metodo es una funcion asociada a un objeto (Dicho objeto puede ser una variable, una lista, un diccionario, un objeto, una clase, etc.)

#Metodos de Listas

names = ["Javier","Paula","Herasi", "Alejandro", "Cris", "Norland"]

#len() devuelve la longitud de mi lista

print(f"la longitud de mi lista es: {len(names)}")


#append() nos permite agregar un elemento al final de la lista

names.append(input("Ingrese un nombre: "))

print(names)

#extend(): nos permite agregar varios elementos al final de la lista

names.extend(["manuel","Andrea","Juan"])

print(names)

#insert (posicion, elemento): nos permite agregar un elemento en una posicion especifica de la lista

names.insert(2, "Andres")
print(names)

#remove(elemento): nos permite eliminar un elemento de la lista

names.remove("Andres")

print(names)    

#index(elemento): nos permite obtener el indice de un elemento en la lista

print(names.index("Juan"))  

#count(elemento): nos permite contar cuantas veces se repite un elemento en la lista

cellphones = ["Samsung", "Xiaomi", "Apple", "Huawei", "Samsung"]
print(cellphones.count("Samsung"))

#sort(): nos permite ordenar la lista de forma ascendente

cellphones.sort()
print(cellphones)

#reverse(): nos permite invertir el orden de la lista
cellphones.reverse()
print(cellphones)

#pop(indice): nos permite eliminar un elemento de la lista en una posicion especifica y devuelve el elemento eliminado
removed_item = cellphones.pop(2)
print(removed_item)