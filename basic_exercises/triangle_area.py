"""
Dado de los valores ingresados por el usuario (base, altura) calcular
y mostrar en pantalla el área de un triángulo.
"""

print("Type the triangle base value, please: ")
base = input()

print("Type the triangle height value, please: ")
height = input()

print("Type measurement unit, please")
m = input()

result = int(base) * int(height) // 2 

print("The triangle area is: ", result, "square", m)

