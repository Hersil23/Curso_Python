#El manejo de excepciones se refiere a la forma en que Python maneja los errores que pueden ocurrir durante la ejecución de un programa.


#Python tiene la estructura try-except para manejar excepciones.


def divide_numbers(num1, num2):
  return num1 / num2

#la siguiente variable rompe el programa, porque no se puede dividir por cero
#result = divide_numbers(10, 0)

#print("Finalizado el programa")


def safe_divide_numbers(num1, num2):
  try:
    val = num1 / num2
    return val
  #el siguiente bloque de codigo se ejecuta si ocurre un error de division por cero
  except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
    return None
  #el siguiente bloque de codigo se ejecuta si ocurre un error de tipo
  except TypeError:
    print("Error: Los valores deben ser números.")
    return None
  finally:
    print("Intento de división finalizado.")
    
  
#result = safe_divide_numbers(10, 1)

#result2 = safe_divide_numbers(10, 0)

#result3 = safe_divide_numbers(10, "a")

#print(f"El resultado es: {result}")

#print(f"El resultado es: {result2}")

#print(f"El resultado es: {result3}")

#Ejemplo de manejo de excepciones fuera de funcion

try:
  number = int("123")
# Si el texto no se puede convertir a un número entero, se lanzará una excepción ValueError
except ValueError:
  print("Error: No se puede convertir el texto a un número entero.")

# Si no ocurre ninguna excepción, se ejecutará el bloque else
else:
  print("Conversión exitosa.")
#Opcional, por si quieres que pase algo ocurra o no ocurra un error  
finally:
  print("Intento de conversión finalizado.")
  
#Ejemplo de manejo de excepciones sobre indices, para preparar nuestra app para errores de indice
try:
  list = ["primer elemento", "segundo elemento", "tercer elemento"]
  element = list[2]
except IndexError:
  print("Error: El elemento no existe en la lista.")
else:
  print(f"El elemento del indice pedido es: {element}")
  
  
#Existen varias excepciones mas como:

#KeyError: si se intenta acceder a una clave no existente en un diccionario
#FileNotFoundError: si se intenta abrir un archivo que no existe