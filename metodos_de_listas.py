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
