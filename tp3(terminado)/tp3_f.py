"""
Dado un diccionario de personas y sus edades, crea una lista que contenga solo los 
nombres de las personas cuya edad es mayor a una edad ingresada por el usuario, 
utilizando list comprehensions.
"""
diccionario={
    "juan":19,
    "leo":54,
    "colo":21
}
print("ingrese la edad minima")
edadminima=int(input())
mayores=[nombre for nombre,  edad in diccionario.items() if edad > edadminima]
print(mayores)