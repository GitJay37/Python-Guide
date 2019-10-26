# class Triangulo:

#     def area(self):
#         return(self.base * self.altura) / 2

# triangulo = Triangulo()
# triangulo.base = 10
# triangulo.altura = 20

# result = triangulo.area()
# print(result)


class Triangulo:
    @staticmethod
    def area(base, area):
        return(base * altura) / 2

result = Triangulo.area(10, 20)
print(result)

