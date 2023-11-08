class Persona:  #CLASE PADRE
    def __init__ (self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar (self):
        print ("Hola")
    
class Artista:
    def __init__ (self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilida (self):
        print(f"Mi habilidad es: {self.habilidad}")


class Empleado (Persona):   #CLASE HIJO
    def __init__ (self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)        #Se detalla lo que se quiere heredar de la clase padre
        self.trabajo = trabajo
        self.salario = salario

class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad,salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)        #CUANDO SE HEREDA DE MAS DE UNA CLASE SE DETALLA QUE SE HEREDA DE CADA UNA
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

roberto = Empleado("Roberto", 43, "argentino","Cantar", "Progranador", 10000)


herencia = issubclass (EmpleadoArtista, Persona)    #NOS INDICA SI UNA CLASE HEREDA DE OTRA
print(herencia)

instancia = isinstance (roberto, Persona)   #NOS INDICA SI ES UNA INSTANCIA (OBJETO) DE UNA CLASE
print (instancia)


roberto.hablar()       #Tambien se heredan los metodos