""""
Realizar un programa que pida los tres lados de un triángulo e indique el tipo de 
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos 
lados iguales) o Escaleno (tres lados distintos). 
"""
print("Ingrese el lado a")
a = int(input())
print("Ingrese el lado b")
b = int(input())
print("Ingrese el lado c")
c = int(input())

if (a == b and a == c):
    print("El triángulo es equilátero")
elif (a == b or a == c or b == c):
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")