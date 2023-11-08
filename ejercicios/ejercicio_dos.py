class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def datos (self):
        print(f"""ALUMNO: \n 
                NOMBRE: {self.nombre} \n
                EDAD:   {self.edad}""")
        
class Estudiante (Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def mostrar_grado (self):
        print (f"El grado del estudiante es: {self.grado}")
        
        
estudiante = Estudiante ("Nahuel","24", "sexto")

estudiante.datos()
estudiante.mostrar_grado()