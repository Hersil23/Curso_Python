#Los bucles son estructuras de control que permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición. En Python, existen dos tipos principales de bucles: `for` y `while`.

#for (para cada elemento en una secuencia)

fruits = ["Manzana", "banana", "naranja", "kiwi"]

for fruit in fruits:
  print(fruit)
  
  
#Recorrer un rango de numeros

for i in range(0,5):
  print(f"Numero: {i}")
  
myList = ["Python", "Java", "C++", "JavaScript", "PHP"]

for language in myList:
  if language == "JavaScript":
    print("JavaScript encontrado, saliendo del bucle.")
    break  # Sale del bucle si encuentra "JavaScript"
  print(f"Lenguaje de programacion: {language}")
  
#Usando continue para saltar un elemento especifico

for language in myList:
  if language == "Java":
    print("Saltando Java.")
    continue  # Salta el resto del bucle para este elemento
  print(f"Lenguaje de programacion: {language}")

#Bucle while (mientras se cumpla una condicion)

count = 0

while count < 5:
  print(f"Contador: {count}")
  count += 1
  

choise = input("Para iniciar escriba iniciar: ") #INICIAR choise = "INICIAR"


while choise.lower() == "iniciar":
  numberOne = int(input("Ingrese un numero: "))
  numberTwo = int(input("Ingrese otro numero: "))
  print(f"La suma de {numberOne} y {numberTwo} es: {numberOne + numberTwo}")
  choise = input("Para continuar escriba 'continuar' o cualquier otra tecla para salir: ") #No
  if choise.lower() == "continuar":
    choise = "iniciar"  # Reinicia el bucle si el usuario escribe "continuar"
#Al terminar el bucle, se imprime un mensaje de despedida.
print("Gracias por usar la calculadora. ¡Hasta luego!")


#Enunciado de ejercicios

# Ejercicio 1: Contador Selectivo
# Enunciado:  
# Escribe un programa que pida al usuario un número entero positivo "n". Luego, imprime todos los números del 1 al "n" que cumplan al menos una de estas condiciones:
# 1. El número es múltiplo de 3.
# 2. El número es mayor que 10 y menor que 20.
# 3. El número es igual a 25 o 50.  
# Si el número no cumple ninguna condición, no se imprime.

n = int(input("Ingrese un número entero positivo: "))
print("Números que cumplen las condiciones:")
for i in range(1, n + 1):
    if (i % 3 == 0) or (10 < i < 20) or (i == 25 or i == 50):
        print(i)


# Ejercicio 2:
#Enunciado: 
# Crea un programa que simule la validación de una contraseña:
# 1. Define una contraseña secreta (ej: "python123").
# 2. Pide al usuario que ingrese una contraseña.
# 3. El programa debe:
#    - Permitir hasta 3 intentos.
#    - Si la contraseña es correcta, muestra "¡Acceso concedido!" y terminar el programa.
#    - Si es incorrecta, muestra "Contraseña incorrecta. Intentos restantes: X" y permitir un  siguiente intento.
#    - Si se agotan los intentos, muestra "¡Cuenta bloqueada!".

password = "python123"
attents = 3


while attents > 0:
  input = input("Ingrese la contraseña: ")
  if input == password:
    print("¡Acceso concedido!")
    break
  else:
    attents -= 1
    print(f"Contraseña incorrecta. Intentos restantes: {attents}")

if attents == 0:
  print("¡Cuenta bloqueada!")