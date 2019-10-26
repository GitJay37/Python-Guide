def greet(name : str) -> None:
    return("Hola " + name)

def suma(a : int, b : int = 100) -> int: #Anotations are guides
    return(a+b)

var_greet = "Jeison"
print(greet(var_greet))

print(suma(40, 30))

