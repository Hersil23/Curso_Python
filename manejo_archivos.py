#Manejo de archivos se refiere a metodos y tecnicas nativos de python para leer, escribir, modificar y eliminar archivos de nuestro sistema.

#Abriendo un archivo para lectura

#Se utiliza el metodo open() para abrir un archivo en modo de lectura.

#El primer argumento es el nombre del archivo, y el segundo argumento es el modo en que se abre el archivo.

#Hay varios modos disponibles para abrir un archivo:

# "r" (read): Abre el archivo para lectura. Si el archivo no existe, genera un error.

# "w" (write): Abre el archivo para escritura. Si el archivo no existe, lo crea.

# "a" (append): Abre el archivo para escritura, agregando contenido al final del archivo. Si el archivo no existe, lo crea.

# "x" (create): Abre el archivo para escritura, creando el archivo si no existe.

try:
  document = open("./Python-Basico/history.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)

#from os import system as cmd

#import time as tm

#tm.sleep(3)

#cmd("cls")

#Crear un archivo nuevo

try:
  document = open("./Python-Basico/relatos.txt", "w")
  content = input("Ingrese el contenido del archivo: ")
  document.write(content)
  document.close()
  
  document = open("./Python-Basico/relatos.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)
  
#Agregar contenido a un archivo existente

try:
  document = open("./Python-Basico/relatos.txt", "a")
  content = input("Ingrese el contenido extra del archivo: ")
  document.write(content)
  document.close()
  
  document = open("./Python-Basico/relatos.txt", "r")
  print(document.read())
  document.close()
except Exception as e:
  print(e)
  
#crear solo archivo

try:
  document = open("./Python-Basico/relatos.txt", "x")
  document.close()
  
except Exception as e:
  print(e)
  
#Eliminar un archivo

import os

try:
  os.remove("./Python-Basico/relatos.txt")
except Exception as e:
  print(e)
  
#Manipular archivos .csv()

#para usar necesitamos importar la libreria
import csv

#Los metodos son:

#csv.writer() para escribir en un archivo .csv
#csv.reader() para leer un archivo .csv
#csv.DictWriter() para escribir en un archivo .csv con diccionarios
#csv.DictReader() para leer un archivo .csv con diccionarios

contacts = [{"nombre": "Jean", "telefono": "1234567890"},
            {"nombre": "Norland", "telefono": "9876543210"},
            {"nombre": "Alejandro", "telefono": "5555555555"},
            {"nombre": "Herasi", "telefono": "1111111111"}]

with open("./Python-Basico/contacts.csv", "w", newline="") as file:
  writer = csv.DictWriter(file, fieldnames=["nombre", "telefono"])
  writer.writeheader()
  writer.writerows(contacts)

with open("./Python-Basico/contacts.csv", "r") as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row["nombre"], row["telefono"])
    
#Ejercicio: agregar un campo adicional "Email" usando "a"
