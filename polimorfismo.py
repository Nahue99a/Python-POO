class Gato ():
    def sonido (self):
        return "MIAU"
    
class Perro ():
    def sonido (self):
        return "GUAU"
    
def hacer_sonido(animal):
    print (animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(perro)     #POLIMORFISMO ES UNA MISMA FUNCION QUE HACE ALGO DIFERENTE DEPENDIENDO EL OBJETO
