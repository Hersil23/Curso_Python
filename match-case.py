#Match nos sirve para evaluar una variable y ejecutar un bloque de código dependiendo del valor de esa variable.

print("Ingrese un numero del 1 al 5")
number = input("Numero: ")

match number:
  case "1":
    print("El numero es 1")
  case "2":
    print("El numero es 2")
  case "3":
    print("El numero es 3")
  case "4":
    print("El numero es 4")
  case "5":
    print("El numero es 5")
  case _:
    print("El numero no esta entre 1 y 5")
    
# El guion bajo (_) se usa como un comodín para capturar cualquier valor que no coincida con los casos anteriores.  

print("Seleccion de Idioma:")

language = input("Ingrese el idioma (es, en, fr): ")

match language:
 case "es":
  print("Seleccionaste Español")
 case "en":
    print("You selected English")
 case "fr":
    print("Vous avez sélectionné le français")
 case _:
    print("No se ha seleccionado ningun idioma")