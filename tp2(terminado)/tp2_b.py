"""
Escriba una función llamada EsBisiesto que permita ingresar un número de año y 
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año 
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por 
pantalla si la fecha es válida o no.
"""
def EsBisiesto(year):
    if year%4==0 and (year%100!=0 or year%400==0):
        print("es bisiesto.")
    else:
        print("no es bisiesto")
seguir=True
while seguir:
    print("ingrese un año")
    year=int(input())
    EsBisiesto(year)
    print("desea seguir?")
    rt=str(input())
    if rt=="no":
        seguir=False