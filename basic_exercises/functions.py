def function(paramether):
    return ("Hola ", paramether)

def welcome_mess(name):
    return "Hello {} Welcome to the Python course 3".format(name)

def add(a,b,c):
    print("Type first number: ")
    a = input()
    print()

    print("Type first number: ")
    b = input()
    print()

    print("Type first number: ")
    c = input()
    print()

    result = int(a) + int(b) + int(c)
    return result


fun = function("Mundo!")
print(fun)
print()

welcome = welcome_mess("Jason")
print(welcome)
print()

res = add(1,2,3)
print("The add total is: ", res)