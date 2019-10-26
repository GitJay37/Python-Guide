# list = []

# for var in range(0, 100):
#     list.append(var)

# print(list)

# la primera variable es cualquir valor: int, float, string, bool, etc
var1 = "Juajuajua"
#estructura = [ var for var in range(0, 100) ] #List comprehensions 

estructura = tuple( ( var for var in range(0, 100) ) )

dictionary = {index:value for index, value in enumerate(estructura)}

print(dictionary)
