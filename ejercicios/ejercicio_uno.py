class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar (self):
        print (f"El estudiante {self.nombre} esta estudiando")
    
nombre = input("Como se llama el estudiante?:    ")
edad = input ("Que edad tiene el estudiante?:   ")
grado = input ("A que grado va el estudiante?:  ")

estudiante = Estudiante(nombre, edad, grado)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()