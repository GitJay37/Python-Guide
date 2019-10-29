# Constructor method

class User:
    def __init__(self, name):
        self.name = name

    def greet(self, param):
        print(param + self.name)

class Employed(User):
    salary = 5000000

    def modify_salary(self, salary):
        self.salary = salary
    
    def show_salary(self):
        print(self.salary)

    def greet(self): #overwrite
        pass 

jay = User("Jeison De Jesús Anillo Pérez")
jay.greet("Hi there, my name is: ")

employed = Employed("Rodmy Jeraldin Jerez Numpaque")
employed.greet("Hello I'm the new employed, my names is: ")
employed.modify_salary(7000000)
employed.show_salary()