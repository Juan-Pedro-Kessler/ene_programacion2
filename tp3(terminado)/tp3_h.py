"""
Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los 
elementos únicos utilizando list comprehensions. 
"""
listanueva=[]
lista = [1, 1, 5, 6, 6, 10, 10, 11]
[listanueva.append(elem) for elem in lista if elem not in listanueva]
print(listanueva)