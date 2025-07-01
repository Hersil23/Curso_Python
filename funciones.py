#Es un bloque aislado de codigo reutilizable


#Estructura palabra reservada def + nombre de mi funcion + parentesis () + dos puntos ":" dentro lo que sea que quiera
#ejecutar

#Defino mi funcion (Declarar)
def saludar():
  print("Hola desde mi funcion")
  
#usar mi funcion (Invocar)
saludar()

#Esto es una variable Global, existe en todo el programa
valOne = 10

def sum():
  #Esto es una variable local, solo existe dentro de la funcion
  valTwo = 3
  print(f"La suma de {valOne} y {valTwo} es: {valOne + valTwo}")
  
sum()

print(valOne)