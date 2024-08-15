""""
Implemente un programa que a partir del ancho, alto y largo de una habitación 
rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo 
que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una 
puerta de 0,80 de ancho por 2 mts de alto. 
"""
anchopuerta=0.8
altopuerta=2
areapuerta=anchopuerta*altopuerta
print("ingrese el ancho")
ancho=float(input())
print("ingrese el alto")
alto=float(input())
print("ingrese el largo")
largo=float(input())
area=2*(ancho*alto)+(largo*alto)-areapuerta
total=area/10
print(f"se necesitaran {total} de litros de pintura para una pieza de {alto} de alto, {largo} de largo y {ancho} de ancho")