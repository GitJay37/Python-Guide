# dictionary = {}

# dictionary["name"] = "Jay" #key and value
# value = dictionary["name"] 
# dictionary["name"] = "Ring"

# diccionario = {"a": 9, "b": 2, "c": 3, "a": 4} # --> When a key is duplicated the dictionary takes the last value in it

# validate = "f" in diccionario # valida if a key exists
# val = diccionario.get("a") # valida if a key exists
# valu = diccionario.get("z", "The key don't exists") # The key don't exists, The second value can be any type value: int, float, string, tuple, list, dictionary, etc...
# set_def = diccionario.setdefault("z", {"key": 3})

# print(validate)
# print(val)
# print(valu)
# print(set_def)
# print(diccionario)

diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10}

# result = diccionario.keys()
# result = diccionario.values()
# result = tuple(result)
# result = diccionario.items()
# result = list(result)

#diccionario = {}

#del diccionario["a"]
#diccionario.pop("d")
#valor = diccionario.pop("d")

diccionario.clear()

print(len(diccionario))
#print(valor)
print(diccionario)



