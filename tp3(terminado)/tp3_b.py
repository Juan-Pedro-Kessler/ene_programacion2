"""
Implemente una función que, dada una lista de nombres, devuelva una nueva lista 
que contenga solo los nombres que tengan una longitud mayor o igual a una 
cantidad de caracteres pasada por parámetro, utilizando list comprehensions. 
"""
def averiguar(nombres, caracteres):
    return [nombre for nombre in nombres if len(nombre) >= caracteres]

seguir = "si"
nombres = []

while seguir == "si":
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    
    valido = False
    while not valido:
        rt = input("¿Deseas seguir? (si o no): ").lower()
        if rt == "si" or rt == "no":
            valido = True
        else:
            print("Respuesta inválida, por favor ingresa 'si' o 'no'.")
    
    if rt == "no":
        seguir = "no"
caracteres = int(input("Ingrese el número de caracteres: "))
nombresnuevo = averiguar(nombres, caracteres)

print("Los nombres que superan o igualan ese parámetro son:")
for nombre in nombresnuevo:
    print(nombre)
