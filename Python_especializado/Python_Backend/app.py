import requests

#obtener los datos de un pokemon

url = "https://pokeapi.co/api/v2/pokemon/pikachu"  # URL de la API de Pokémon para Pikachu

#creemos nuestra respuesta

response = requests.get(url)

#verifiquemos que la respuesta sea exitosa

if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Altura: {data['height']}")
else:
    print("Error al obtener los datos del pokemon")