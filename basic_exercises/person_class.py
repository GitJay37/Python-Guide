class Person:
    # Metodos de clase
    def attribes(self):
        print("A person knows to dance!!")

    def eat(self):
        print("I'm eating")

    def sleep(self):
        print("I'm sleeping")

class Persona(Person): # Esto es una herencia 
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id 

class Personb(Person):
    def beauty(self):
        print("Hi there, I'm a beatyful Princess")   

yeye = Persona("Jason", 30, 112957)
print(yeye.name) 
print(yeye.age)
print(yeye.id)
print()
yeye.attribes()
yeye.eat()
yeye.sleep()
print()
yeya = Personb()
yeya.attribes()
yeya.beauty()


# class Example:
#     something = 3*3
        
# obj = Example()
# print(obj.something)
