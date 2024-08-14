#Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura. 
anchopuerta=0.8
altopuerta=2
areapuerta=anchopuerta*altopuerta
print("ingrese el ancho")
ancho=float(input())
print("ingrese el alto")
alto=float(input())
print("ingrese el largo")
largo=float(input())
print("cuantas manos de pintura quiere usar?")
manos=int(input())
area=2*(ancho*alto)+(largo*alto)-areapuerta
total=(area/10)*manos
print(f"se necesitaran {total} de litros de pintura para una pieza de {alto} de alto, {largo} de largo y {ancho} de ancho")