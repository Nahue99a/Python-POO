class Celular :           #Para crear una clase se utiliza la palabra reservada CLASS, ademas, es una buena practica poner los nombres con PascalCase, que es como camelCase pero la primer letra tambien es mayuscula
    def __init__ (self, marca, modelo, camara):  #este metodo siempre se va a ejecutar cuando creemos el objeto
       self.marca = marca
       self.modelo = modelo
       self.camara = camara
       
    def llamar (self):
        print (f"Estas haciendo un llamado desde un: {self.modelo}")
    
    def cortar (self):
        print ("Cortaste la llamada")
    
celular1 = Celular("Samsung", "S23", "48MP")      #Forma de crear un objeto
celular2 = Celular("Apple", "iPhone 14 Pro", "96MP")

print(celular1.modelo)

celular2.llamar()

