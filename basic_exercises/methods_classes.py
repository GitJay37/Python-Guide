# Constructor method
"""
    class User:
        def __init__(self, nombre):
            self.nombre = nombre

        def saluda(self, parametro):
            print(parametro + self.nombre)

    class Employed(User):
        salario = 5000000

        def modify_salario(self, salario):
            self.salario = salario
        
        def show_salario(self):
            print(self.salario)

        def saluda(self): #overwrite
            super().saluda("Hi there!! my nombres ")
            print("Hi, my nombre is: "+ self.nombre+ "  and I earn "+str(self.salario)+" Colombian pesos") 

    class Page:
        def print_footnote(self):
            print(self.footnote)

    class LegalPage(Page):
        def print_footnote(self):
            print("All rights reserved")
            super().print_footnote()



    jay = User("Jeison De Jesús Anillo Pérez")
    jay.saluda("Hi there, my nombre is: ")

    employed = Employed("Rodmy Jeraldin Jerez Numpaque")
    employed.saluda()

    html = LegalPage()
    html.footnote = "<p> I'm a footnote </p>"
    html.print_footnote()
"""
# Emcapsulamiento
class Usuario:
    __edad = 0 # var privada __
    def __init__(self, nombre): # Metodo constructor
        self._nombre = nombre

    def saluda(self, parametro):
        print(parametro + self.nombre)

    @property # Metodo getter
    def edad(self):
        return self.__edad

    @edad.setter # Metodo setter
    def edad(self, valor):
        if(valor < 0):
            raise ValueError("Edad no puede ser menor a 0")
        self.__edad = valor

class Empleado(Usuario):
    __salario = 5000000

    def modificar_salario(self, salario): # Metodo setter y publico _
        self.__salario = salario
    
    def mostrar_salario(self): # Metodo getter
        print(self.__salario)

    def saluda(self): #overwrite
        super().saluda("Hi there!! my nombres ")
        print("Hi, my nombre is: "+self._nombre+" y mi salario es: "+str(self.__salario))
    
empleado = Empleado("Jesus' Jason  Ring Perez")
empleado.edad = 30
print(empleado.edad)