"""
Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos
y mostrar el resultado en pantalla.
"""
print("Type dollars to convert: ")
dollars = input() 
pesos = 3.11218
result = float(dollars) * pesos

print("Your", dollars, " dollars are equals to: ", result, "Colombian pesos")


