class Circle:
    pi = 3.14159265
    def __init__(self, radio):
        self.radio = radio # Variable de instancia

#Instancias
circle_a = Circle(10) 
circle_b = Circle(20)

circle_a.radio = 100 #Objeto

print(circle_b.radio)
print(circle_a.radio)

print(circle_a.pi) #Variable de la clase
print(Circle.pi)