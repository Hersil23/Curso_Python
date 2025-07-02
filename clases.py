#La POO (Programacion Orientada a Objetos) es un paradigma de programacion que nos permite crear objetos que contienen tanto datos como metodos para manipular esos datos.

#Clase es una plantilla o molde que define las caracteristicas y comportamientos de un objeto.


class Person:
  #Esto no cambia, son atributos estaticos
  # name = "Delvis"
  # age = 23
  # country = "Venezuela"
  
  def __init__(self, name, age, country):
    #Atributos dinamicos de clase
    self.name = name
    self.age = age
    self.country = country
    
  #Podemos tener metodos dentro de una clase, estos son funciones que pertenecen a la clase
    
  def greet(self):
    print(f"Hola, desde mi clase, mi nombre es {self.name}, tengo {self.age} años y soy de {self.country}")
  
  def goodbye(self):
    print(f"Adios, hasta la proxima amiguitos")
    
#Instaciar una clase es crear un objeto a partir de la clase, esto se hace llamando a la clase como si fuera una funcion.

personOne = Person("Delvis", 23, "Venezuela")

personTWo = Person("Herasi", 47, "Venezuela")

#Acceder a los atributos de la clase
    
print(f"Mi nombre es {personOne.name}, tengo {personOne.age} años y soy de {personOne.country}")
#Lllamemos a nuestra segunda persona
print(f"Mi nombre es {personTWo.name}, tengo {personTWo.age} años y soy de {personTWo.country}")
    
#Llamar a los metodos de la clase

personOne.greet()

personTWo.goodbye()

#Acceder a los atributos  con el atributo especial __dict__

print(f"Los atributos de personOne son: {personOne.__dict__}")


#Extencion de clases, podemos crear una clase que herede de otra clase, esto se llama herencia.


#Si yo creo ua clase student, esta heredara todos los atributos, su manejo, y todos los metodos de la clase Person

class Student(Person):
  
  def __init__(self, name, age, country,career):
    #Llamamos al constructor de la clase padre
    super().__init__(name, age, country)
    #Atributo adicional de la clase Student
    self.career = career
    
    #Metodo propio de la clase Student
    
  def study(self):
    print(f"Estoy estudiando {self.career}")


studentOne = Student("Alejandro", 34, "Venezuela", "Admin. Financiera")

print(f"Mi nombre es {studentOne.name}, tengo {studentOne.age} años, soy de {studentOne.country} y estudio {studentOne.career}")

studentOne.greet()

studentOne.goodbye()

studentOne.study()

#Crear la clase professor que herede de la clase Person y tenga su propia variable llamada, class, y su metodo
#darClass
class Professor(Person):
	
	def __init__(self, name, age, country, className):
		#Llamamos al constructor de la clase padre
		super().__init__(name, age, country)
		#Atributo adicional de la clase Professor
		self.className = className
		
	#Metodo propio de la clase Professor
	def giveClass(self):
		print(f"Estoy dando la clase de {self.className}")

professorOne = Professor("Romulo", 53, "Colombia", "Fisica")

print(f"Mi nombre es {professorOne.name}, tengo {professorOne.age} años, soy de {professorOne.country} y doy la clase de {professorOne.className}")

professorOne.giveClass()