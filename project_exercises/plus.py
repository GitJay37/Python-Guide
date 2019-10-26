<<<<<<< HEAD
"""
Función que valida para que los datos ingresados por consola
sean si o si enteros o decimales
"""
#declaracion de función que recibe un string como parametro
def validations(message):
    #ciclo while que siempre se ejecutará con el True
    while True:
        #función o metodo try
        try: 
            # la variable data almacena el valor tipo float dado por consola
            data = float(input("Digita: "+message))
            # si el dato ingresado es tipo int o float se retorna
            return data
        except ValueError:
            #si hay un error en el metodo try se imprime el sgte string siempre
            print("Digita un valor entero o decimal")
        
#datos de entrada
largo = validations("el largo en metros: ")
ancho = validations("el ancho en metros: ")
m2xcja = validations("los metros cuadrados por caja: ")
precioxm2 = validations("el precio por metro cuadrado: ")
"""
Regla de tres
1m2 = $162 pesos mexicanos
1.5m2= $ ?
"""
precioxcja = m2xcja * precioxm2
#metros cuadrados que tiene el cuarto o habitación
m2cuarto = largo * ancho
#numero de veces que caben las baldosas en la habitación
cajas = m2cuarto/m2xcja
#precio tatal a invertir en cantidad de cajas por comprar
preciototal = cajas * precioxcja
print("Total necesario de cajas :", cajas)
print("Precio total :", preciototal)
=======
"""
Función que valida para que los datos ingresados por consola
sean si o si enteros o decimales
"""
#declaracion de función que recibe un string como parametro
def validations(message):
    #ciclo while que siempre se ejecutará con el True
    while True:
        #función o metodo try
        try: 
            # la variable data almacena el valor tipo float dado por consola
            data = float(input("Digita: "+message))
            # si el dato ingresado es tipo int o float se retorna
            return data
        except ValueError:
            #si hay un error en el metodo try se imprime el sgte string siempre
            print("Digita un valor entero o decimal")
        
#datos de entrada
largo = validations("el largo en metros: ")
ancho = validations("el ancho en metros: ")
m2xcja = validations("los metros cuadrados por caja: ")
precioxm2 = validations("el precio por metro cuadrado: ")
"""
Regla de tres
1m2 = $162 pesos mexicanos
1.5m2= $ ?
"""
precioxcja = m2xcja * precioxm2
#metros cuadrados que tiene el cuarto o habitación
m2cuarto = largo * ancho
#numero de veces que caben las baldosas en la habitación
cajas = m2cuarto/m2xcja
#precio tatal a invertir en cantidad de cajas por comprar
preciototal = cajas * precioxcja
print("Total necesario de cajas :", cajas)
print("Precio total :", preciototal)
>>>>>>> 1acbfc0d3d8287f854e112ab3e308f34cebe1af2
