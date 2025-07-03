#Un metodo es una funcion asociada a un objeto (Dicho objeto puede ser una variable, una lista, un diccionario, un objeto, una clase, etc.)

#Metodos de Strings

name = "Javier"

#len() devuelve la longitud de mi string

print(f"la longitud de mi string es: {len(name)}")

#count() devuelve la cantidad de veces que aparece una subcadena dentro de mi cadena (String)

text = "ok, chicos, esto es un texto, de muletillas ok"

print(f"la cantidad de 'ok' en mi string es: {text.count("ok")}")

#upper() convierte mi string en mayusculas

print(f"Mi string en mayusculas es: {name.upper()}")


#lower() convierte mi string en minusculas

print(f"Mi string en minusculas es: {name.lower()}")

nameOne = "cris"

#capitalize() convertir la primera letra de nuestro a mayusculas

print(f"Mi string con la primera letra en mayusculas es: {nameOne.capitalize()}")


#replace() reemplaza una subcadena por otra

user_status = "El usuario se encuentra online"

print(f"El usuario se encuentra {user_status}")

user_status = user_status.replace("online", "offline")

print(f"El usuario se encuentra {user_status}")

#split() divide mi string en una lista

my_super_awesome_text = "Hola mundo, estamos aqui felices, aprendiendo Python, en Lexpin"

my_words_list = my_super_awesome_text.split(", ")

print(my_words_list)


print("="*50)

#strip() permite eliminar un caracter en especifico de el inicio y el final de nuestro string

my_super_awesome_text = "------Hola mundo, estamos aqui felices, aprendiendo Python, en Lexpin----"

my_super_awesome_text = my_super_awesome_text.strip("-")

print(my_super_awesome_text)


#find() busca la posicion de una subcadena dentro de mi string

my_super_awesome_text = "Hola mundo, estamos aqui felices, aprendiendo Python, en Lexpin"

print(my_super_awesome_text.find("Python"))

#join() une los elementos de una lista (array) en un solo string, separados por un caracter

my_words_list = ["Hola", "mundo", "estamos", "aqui", "felices", "aprendiendo", "Python", "en", "Lexpin"]

my_super_awesome_text = " ".join(my_words_list)

print(my_super_awesome_text)


#starswith() devuelve True si el string empieza con la subcadena indicada

my_super_awesome_text = "Hola mundo, estamos aqui felices, aprendiendo Python, en Lexpin"

print(my_super_awesome_text.startswith("Hola"))


#endswith() devuelve True si el string termina con la subcadena indicada

my_super_awesome_text = "Hola mundo, estamos aqui felices, aprendiendo Python, en Lexpin"

print(my_super_awesome_text.endswith("Patata"))