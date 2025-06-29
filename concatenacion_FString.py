#Concatenar

#Se refiere a unir dos o mas cadenas de texto por medio del operador +

textOne = "Hola "

textTwo = "Mundo"

# Usando el operador + para concatenar
print(textOne + textTwo)

#pintar una al lado de la otra
print(textOne, textTwo)

# Usando f-strings para concatenar 

name = "Jesus"
age = 23

#Con f-strings, podemos insertar variables directamente en cadenas de texto
print(f"Hola mi nombre {name} y tengo {age} años")

#Hacer comentarios de varias lineas

print(f"""Hola mi nombre es {name} y tengo {age} años
Estoy aprendiendo Python""")