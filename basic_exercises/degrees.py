"""
Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit
y mostrar el resultado en pantalla.
"""
print("Type the celcius degrees to convert to Fahrenheit degrees: ")
degrees_c = input()

result = (float(degrees_c) * 9//5) + 32

print("The degrees Fahrenheit are: ", result)
