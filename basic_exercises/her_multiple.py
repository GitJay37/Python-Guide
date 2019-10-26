class Clasea:
    def a(self):
        print("Soy la clase a")

class Claseb:
    def b(self):
        print("Soy la clase b")
    
class Clasec:
    def c(self):
        print("Soy la clase c")

class Clased:
    def d(self):
        print("Soy la clase d")
    
class Clasee(Clasea, Claseb, Clasec, Clased): #Herencia multiple
    def e(self):
        print("Soy la clase e")

obj_e = Clasee()
obj_e.a()
obj_e.b()
obj_e.c()
obj_e.d()
obj_e.e()
print()
obj_a = Clasea()
obj_a.a()

    

    