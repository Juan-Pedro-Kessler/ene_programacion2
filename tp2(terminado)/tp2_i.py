"""
Un profesor almacenó los datos de los alumnos de su materia en un archivo 
alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas 
finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de 
legajo.  
En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de 
legajo, apellido y nombre de cada uno. 
En ambos archivos los datos están separados por punto y coma  ( ; )  . 
Desea escribir un programa para generar un archivo Promoción.txt con los apellidos 
y nombres de los alumnos que promocionan la materia, esto es, alumnos que el 
promedio de las tres notas supere los 7 puntos.  
El archivo debe quedar ordenado alfabéticamente
"""
promedios=[]
legajo=[]
oral=[]
escrito=[]
tp=[]
arch=open("alumnos.txt","r")
for linea in arch:
    datos = linea.strip().split(";")
    legajo.append(int(datos[0]))
    oral.append(int(datos[1]))
    escrito.append(int(datos[2]))
    tp.append(int(datos[3]))
arch.close()
tope=len(oral)
with open("promocion.txt", "w") as promocion:
    for i in range(0, tope, 1):
        promedio=(oral[i]+escrito[i]+tp[i])/3
        promedios.append(promedio)
        if (promedio)>=7:
            promocion.write(f"{legajo[i]};{oral[i]};{escrito[i]};{tp[i]};{promedios[i]}\n")
        