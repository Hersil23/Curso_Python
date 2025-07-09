 # try:
 #   document = open("Tareas/history.txt", "r")
  #  print(document.read())
  #  document.close()
 # except Exception as e:
  #  print(e)
    

#crear un archivo

try:
    document = open("Tareas/python.txt", "w")
    document.write("Hola, este estoy aprendiendo Python.")
    document.close()

    document = open("Tareas/python.txt", "r")
    print(document.read())    
    document.close()
except Exception as e:
    print(e)