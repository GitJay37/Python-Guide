def tabla_multiplicar(num, max=10):
    for pos in range(1, max + 1):
        yield num * pos, num, pos


for result, number, position in  tabla_multiplicar(3,20):
    print(number, "x", position, "=", result)