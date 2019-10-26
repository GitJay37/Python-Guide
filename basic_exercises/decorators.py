#a,b,c
#(a,b) -> c

def decorator(func):

    def new_func(*args, **kwargs):
        print("first statement")
        result = func(*args, **kwargs)
        print("second statement")
        return result

    return new_func

@decorator
def func_to_work():
    print("This is a function to work")

@decorator
def suma(a,b):
    return a + b

func_to_work()
print()
var_sum = suma(30,70)
print(var_sum)