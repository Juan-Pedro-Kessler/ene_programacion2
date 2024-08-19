"""
Escriba un programa que permita cargar las notas de exámenes, primero debe 
permitir ingresar por teclado la cantidad de notas que desea cargar, y luego 
cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e 
indicar en qué índice del arreglo se encuentra
"""
notas=[]
print("ingrese la cantidad de notas que sea guardar")
cant=int(input())
for i in range(0, cant, 1):
    print(f"ingrese la nota {i+1}")
    notas.append(int(input()))
max=notas[0]
indice=0
for i in range(1, cant):
    if max < notas[i]:
        max = notas[i]
        indice = i
print(f"la nota mas alta es {max} y se encuentra en el indice {indice}")