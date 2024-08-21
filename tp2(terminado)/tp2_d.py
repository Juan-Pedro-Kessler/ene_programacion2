"""
Escriba un programa que permita ingresar un número, se debe validar que 
realmente se haya ingresado un número, y crear una lista para almacenar por 
separado los dígitos del número. Luego recorrer la lista y mostrar el índice que 
contiene el dígito mayor. 
"""
lista=[]
seguir=True
while seguir:
    print("ingrese un numero")
    num=input()
    if(num.isnumeric()):
        entero=True
    else:
        entero=False
    if entero:
        lista.append(num)
    print("desea seguir?")
    rt=str(input())
    if rt=="no":
        seguir=False
elementos=len(lista)
max=lista[0]
indice=0
for i in range(1, elementos, 1):
    if max<lista[i]:
        indice=i
        max=lista[i]
print(f"el maximo es {max} y el indice es {indice}")