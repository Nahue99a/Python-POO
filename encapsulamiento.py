class MiClase:
    def __init__(self):     
        self._atributo_privado = "valor"    #Forma de definir un atributo privado
        self.__atributo_muy_privado = ""    #Forma de definiri un atributo MUY privado, el cual no se puede acceder
        

objeto = MiClase()
print(objeto._atributo_privado)