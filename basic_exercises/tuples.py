#tuple = (1,2,3,4,5,6,7,8,9,0)
#element = tuple[:9:2] # Recorre la tupla de 2 en 2 desde el prímer índice
#print(element)
# tuple[2] = 20 #los valores de una tupla no pueden modificarse
#tupla = (1,2,3,4,5)
#one, two, three, four, five = tupla
#print(one, two, three, four, five)

array = [1, 2, 3, 4, 5]

tuplas = (2, 4, 6, 8, 10)
tuplas_1 = (3, 5, 7, 9, 11)
ten, *twenty, fifty, sixty = tuplas

print(ten)
print(twenty)
print(fifty)
print(sixty)

result = zip(array, tuplas, tuplas_1 )
result = tuple(result)
test = type(result)

print(test)
print(result)

#http://docs.python.org.ar/tutorial/
