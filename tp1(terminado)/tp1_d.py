"""
Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el 
mayor de los 3 y mostrar un mensaje por pantalla.
"""
print("Ingrese el numero a")
a = int(input())
print("Ingrese el numero b")
b = int(input())
print("Ingrese el numero c")
c = int(input())
if(a>b and a>c):
    mayor=a
if(b>a and b>c):
    mayor=b
if(c>b and c>a):
    mayor=c    