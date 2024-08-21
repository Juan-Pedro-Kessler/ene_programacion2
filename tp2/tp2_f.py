"""
Escriba un programa que permita leer de un archivo distancias.txt (cada renglón 
tiene una distancia válida) las distancias recorridas por el vehículo de una empresa, 
luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y 
todas las distancias mayores al promedio. 
Ej del contenido del archivo: 
150 
120 
50 
34 
250 
Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor 
son: … , … , …. , …. “ 
"""
distancias=[]
mayores=[]
arch = open("distancias.txt", "r")
for linea in arch:
    distancias.append(int(linea.strip()))
arch.close()
promedio=sum(distancias)/len(distancias)
tope=len(distancias)
for i in range(0, tope, 1):
    if distancias[i]>promedio:
        mayores.append(distancias[i])
print(f"el promedio es de {promedio} y todas las mayores son: ")
tope=len(mayores)
for i in range(0, tope, 1):
    print(mayores[i])