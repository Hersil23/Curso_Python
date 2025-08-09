from bs4 import BeautifulSoup
import requests


#Vamos a leer un archivo local en modo solo lectura
with open("./Python-Backend/webScrapping/beautifulSoup/index.html", "r", encoding="utf-8") as html_file:
  """ Abro mi archivo y lo guardo en una variable """
  html = html_file.read()
  
soup = BeautifulSoup(html, "html.parser")

#Vamos a extraer los titulares
title = soup.find("h1")
""" title = soup.find("p", class_="text") """

#vamos a traernos todos los parrafos
paragraphs = soup.find_all("p")

#vamos a mostrar mi h1
print(title.text)


#vamos a mostrar todos los parrafos
for paragraph in paragraphs:
  print(paragraph.text)
  

url = "https://www.amazon.com/s?k=gaming"
second_url ="https://www.amazon.com/s?k=gaming&page=2"

#necesito configurar cabeceras
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36",
  "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.6,en;q=0.4"
}

#hacemos nuestra peticion 
""" response = requests.get(url, headers=headers) """
response = requests.get(second_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


#Buscamos todos los productos (Las clases pueden variar verifica)
products = soup.find_all("div", {"class": "s-card-container"})

""" print(products) """

print("\n")
print("Aqui comienza mi scrappin de productos")

for product in products:
  try:
    name = product.find("h2", {"class": "a-text-normal"}).text
    price = product.find("span", {"class": "a-offscreen"}).text
    
    print(f"Producto: {name} Precio: {price}")
  except:
    pass