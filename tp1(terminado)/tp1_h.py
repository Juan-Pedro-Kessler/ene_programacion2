"""
Desarrollar un programa que permita al usuario indicar cuantos valores quiere 
ingresar, luego que permita la carga de los valores por teclado y nos muestre 
posteriormente la suma de los valores ingresados y su promedio.
"""
seguir=True
total=0
a=0
while seguir:
    a+=1
    print("ingrese un numero")
    nro=int(input())
    total+=nro
    print("desea seguir?")
    rta=str(input())
    if rta=='no':
        seguir=False
print(f"la suma es {total} y el promedio es de {total/a}")