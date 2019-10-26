animal = "Lion" #Global variable

def show_animal():
    global animal #convertir standard variable a global
    animal = "Dog"
    print(animal) #Local variable

show_animal()
print(animal)

