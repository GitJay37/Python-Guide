<<<<<<< HEAD
"""
Metodo append, este metodo agrega valores 
dentro de un arreglo lleno o vacío
"""

numbers = [1, 2, 3, 4, 5]
update = []
for value in numbers:
    update.append(value*2)
print(update)

"""
El metodo map opera una función contra un arreglo,
luego devuelve un array o lista con el metodo reservado
en python list
"""
def method_map(var):
    return var * 2
print(list(map(method_map,numbers)))

# usando lambda
print(list(map((lambda variable: variable * 2), numbers)))
=======
"""
Metodo append, este metodo agrega valores 
dentro de un arreglo lleno o vacío
"""

numbers = [1, 2, 3, 4, 5]
update = []
for value in numbers:
    update.append(value*2)
print(update)

"""
El metodo map opera una función contra un arreglo,
luego devuelve un array o lista con el metodo reservado
en python list
"""
def method_map(var):
    return var * 2
print(list(map(method_map,numbers)))

# usando lambda
print(list(map((lambda variable: variable * 2), numbers)))
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
