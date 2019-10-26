class Animal:
    def eat(self):
        print("Comer")
    
class Cat(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
        print("arañar")

class Dog(Animal):
    def __init__(self, nombre):
        self.nombre = nombre
        print("ladrar")

gatito = Cat("ThunderCat")
gatito.eat()
perrito = Dog("Yonclin")
perrito.eat()





