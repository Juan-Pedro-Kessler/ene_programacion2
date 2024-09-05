"""
dada una lista de diccionarios que contienen información de estudiantes de una 
materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) , 
utilizando list comprehensions: 
a. Crea una lista que contenga los nombres de todos los estudiantes. Salida 
ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana'] 
b. Crea una lista que contenga los nombres de todos los estudiantes que han 
obtenido una calificación superior a 70 en todos los exámenes 
c. Crea una lista que contenga los nombres de todos los estudiantes que han 
obtenido una calificación inferior a 60 en al menos un examen.
"""
nombre_apellido=["juanpedro_kessler", "andy_garcia", "fausto_desch", "lautaro_acosta"]
nota_parcial1=[40, 70, 90, 80]
nota_parcial2=[60, 70, 80, 70]
nota_parcial3=[70, 80, 90, 90]
nota_final=[70, 80, 90, 80]
print("los alumnos son:")
print(nombre_apellido)
aprobados=[nombre_apellido[i] for i in range(len(nombre_apellido)) if nota_parcial1[i]>=70 and nota_parcial2[i]>=70 and nota_parcial3[i]>=70 and nota_final[i]>=70]
desaprobados=[nombre_apellido[i] for i in range(len(nombre_apellido)) if nota_parcial1[i]<60 or nota_parcial2[i]<60 or nota_parcial3[i]<60 or nota_final[i]<60]
print("los aprobados son:")
print(aprobados)
print("los desaprobados son:")
print(desaprobados)