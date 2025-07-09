 # try:
 #   document = open("Tareas/history.txt", "r")
  #  print(document.read())
  #  document.close()
 # except Exception as e:
  #  print(e)
    

#crear un archivo


#	try:
#		document = open("Tareas/python.txt", "w")
#		document.write("Hola, este estoy aprendiendo Python.")
#		document.close()

#		document = open("Tareas/python.txt", "r")
#		print(document.read())    
#		document.close()
#	except Exception as e:
#		print(e)

	#from os import system as cmd
	#import time as tm

	#tm.sleep(3)
	#cmd("cls")

#crear un archivo y escribir en el

try:
    document= open ("./Tareas/Nuevo_Archivo2.txt", "w")
    content = input("Escribe el contenido del archivo: ")
    document.write(content)
    document.close()
except Exception as e:
    print("Error al crear o leer el archivo:", e)
