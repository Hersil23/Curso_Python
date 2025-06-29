#Un operador es un simbolo que realizara una operacion sobre uno o mas valores.

#Operadores de Asignacion son aquellos que asignan un valor a una variable.

# asignacion (=): Asigna el valor de la derecha a la variable de la izquierda.

numberOne = 10
numberTwo = 5

#En python se puede asignar multiples valores a la vez

numberOne, numberTwo = 15, 10

print(f"El valor de numberOne es {numberOne} y el valor de numberTwo es {numberTwo}")

#Operadores especiales de asignacion compuestos

# suma y asignacion (+=): Suma el valor de la derecha al valor de la variable de la izquierda y asigna el resultado a la variable de la izquierda.

myVal = 10
myVal += 5 

print(f"El valor de myVal es {myVal}")

# resta y asignacion (-=): Resta el valor de la derecha al valor de la variable de la izquierda y asigna el resultado a la variable de la izquierda.

myVal -= 3

print(f"El valor de myVal es {myVal}")

# multiplicacion y asignacion (*=): Multiplica el valor de la variable de la izquierda por el valor de la derecha y asigna el resultado a la variable de la izquierda.

myVal *= 2

print(f"El valor de myVal es {myVal}")

# division y asignacion (/=): Divide el valor de la variable de la izquierda por el valor de la derecha y asigna el resultado a la variable de la izquierda.

myVal /= 4

print(f"El valor de myVal es {myVal}")

# division entera y asignacion (//=): Divide el valor de la variable de la izquierda por el valor de la derecha y asigna el resultado entero a la variable de la izquierda.

myVal //= 2

print(f"El valor de myVal es {myVal}")

# modulo y asignacion (%=): Calcula el residuo de la division del valor de la variable de la izquierda por el valor de la derecha y asigna el resultado a la variable de la izquierda.

myVal %= 2

print(f"El valor de myVal es {myVal}")

# potencia y asignacion (**=): Eleva el valor de la variable de la izquierda al valor de la derecha y asigna el resultado a la variable de la izquierda.

myVal **= 3

print(f"El valor de myVal es {myVal}")