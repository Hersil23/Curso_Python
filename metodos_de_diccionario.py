# un metodo es una funcion que pertenece a un objeto
# un diccionario es un objeto que contiene pares clave-valor

person = {
    "name": "Herasi",
    "age": 48,
    "city": "Eddinburgh",
    "hobbies": ["reading", "gaming", "coding"]
}

#get(value) nos permite obetener el valor de la clave que le pasamos como parametro
print(person.get("hobbies"))  # ["reading", "gaming", "coding"]

#setdefault(key, default) nos permite obtener el valor de la clave que le pasamos como parametro, si no existe, lo crea con el valor por defecto
print(person.setdefault("country", "Scotland"))  # "Scotland"

print(person)

#que es un json?# un json es un objeto que contiene pares clave-valor, es un formato de intercambio de datos
#para convertir un diccionario a json, usamos el metodo json.dumps()

import json

json_string = json.dumps(person)
print(json_string)

#para convertir un json a diccionario, usamos el metodo json.loads()
json_dict = json.loads(json_string)
print(json_dict)  # {'name': 'Herasi', 'age': 48, 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding'], 'country': 'Scotland'}

#para convertir un diccionario a json, usamos el metodo json.dump() y le pasamos un archivo
with open("person.json", "w") as file:
    json.dump(person, file)
#para convertir un json a diccionario, usamos el metodo json.load() y le pasamos un archivo
with open("person.json", "r") as file:      

		json_dict_from_file = json.load(file)
print(json_dict_from_file)  # {'name': 'Herasi', 'age': 48, 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding'], 'country': 'Scotland'}

#pop(key) nos permite eliminar la clave que le pasamos como parametro y nos devuelve su valor
removed_value = person.pop("age")
print(removed_value)  # 48
print(person)  # {'name': 'Herasi', 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding'], 'country': 'Scotland'}			

#popitem() nos permite eliminar el ultimo par clave-valor y nos devuelve una tupla con la clave y el valor
last_item = person.popitem()
print(last_item)  # ('country', 'Scotland')
print(person)  # {'name': 'Herasi', 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding']}

#copy() nos permite crear una copia del diccionario
person_copy = person.copy()	

personCopy = person.copy()
print(person_copy)  # {'name': 'Herasi', 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding']}
print(personCopy)  # {'name': 'Herasi', 'city': 'Eddinburgh', 'hobbies': ['reading', 'gaming', 'coding']}

#clear() nos permite eliminar todos los elementos del diccionario
person.clear()
print(person)  # {}

