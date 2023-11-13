class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property               #Se le agrega el decorador para indicar al programa que es un getter y usar la funcion como propiedad
    def nombre (self):
        return self.__nombre
    
    @nombre.setter          
    def nombre (self, new_nombre):
        self.__nombre = new_nombre
        
        
nahuel = Persona ("Lucas", 21)

nombre = nahuel.nombre  #Llamado a la funcion como propiedad
print (nombre)


nahuel.nombre = "Algo"
nombre = nahuel.nombre
print(nombre)
