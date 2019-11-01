class Number:
    value = 0

    def __init__(self, value):
        self.value = value

    def compare(self, number):
        if number.value > self.value:
            return number.value
        return self.value

class String:
    value = ""

    def __init__(self, value):
        self.value = value

    def compare(self, string):
        words =  [self,value,string, value]
        words.sort()
        return words[0]

class List:
    value = []
    def __init__(self, value):
        self.value = value
    
    def compare(self, list):
        if len(self.value) > len(list.value):
            return aself.value
        return list.value

def returnBiggest(a,b):
    return a.compare(b)

num_one = Number(28)
num_two = Number(30)
str_one = String("Jeison")
str_two = String("Rodmy")
list_one = List([1,2,3])
list_two = List([4,5,6,7])

print( returnBiggest(list_one, list_two) )

"""
    def returnBiggest(a,b):
        if isinstance(a, int) and isinstance(b, int):
            if a > b:
                return a
            return b
        if isinstance(a, str) and isinstance(b, str):
            words =  [a,b]
            words.sort()
            return words[0]
        if isinstance(a,list) and isinstance(b,list):
            if len(a) > len(b):
                return a
            return b
    
    print( returnBiggest( [1,2,3],[1,2,3,4,5] ) )
"""