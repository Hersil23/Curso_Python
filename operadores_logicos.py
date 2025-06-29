#Los operadores lógicos son utilizados para combinar expresiones booleanas.


numberOne = 10
numberTwo = 5

TengoDinero = False
QuieroSalir = False

# and: Devuelve True si ambas expresiones son verdaderas.

print(TengoDinero and QuieroSalir)  # False, porque QuieroSalir es False

QuieroSalir = True
TengoConQuien =False

# or: Devuelve True si al menos una de las expresiones es verdadera.

print(QuieroSalir or TengoConQuien)  # True, porque QuieroSalir es True

#Condiciones anidadas
print((QuieroSalir or TengoConQuien) and TengoDinero) # False, porque TengoDinero es False

# not: Devuelve True si la expresión es falsa, y False si la expresión es verdadera.

operacion1 = True
operacion2 = False

print(not operacion2)