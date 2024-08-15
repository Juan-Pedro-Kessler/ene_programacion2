"""
Escriba un programa que permita el ingreso de números enteros positivos, 
finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de 
menor a mayor. 
"""
ordenado=True
print("ingrese un numero")
a=int(input())
b=a
while ordenado and a!=0:
    print("ingrese un numero")
    a=int(input())
    if b>a and a!=0:
        print("LA SECUENCIA NO ESTA ORDENADA")
        ordenado=False
    b=a
if ordenado:
    print("la secuencia esta ordenada de menor a mayor")