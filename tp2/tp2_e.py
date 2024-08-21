"""
Escriba un programa que permita cargar una lista de alumnos junto con su nota del 
parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego 
de ingresados los datos debe generar una lista donde figure si aprobaron o no (se 
aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente 
(el resultado no se almacena, se calcula): 
"""
notas=[]
nombres=[]
aprobado=[]
seguir=True
valido=False
while seguir:
    print("ingrese el nombre del alumno")
    nom=str(input())
    nombres.append(nom)
    print("ingrese la nota del alumno")
    while valido==False:
        nota=int(input())
        if nota<40 and nota>=0:
            notas.append(nota)
            apro="desaprobado"
            aprobado.append(apro)
            valido=True
        elif nota>=40 and nota<=100:
            notas.append(nota)
            apro="aprobado"
            aprobado.append(apro)
            valido=True
        else:
            print("ingrese un valor valido")
    print("deseas seguir? si o no")
    rt=str(input())
    rt=rt.lower()
    if rt=="no":
        seguir=False
    if rt=="si":
        valido=False
tope=len(notas)
for i in range(0, tope, 1):
    print(f"nombre: {nombres[i]}, nota: {notas[i]}, estado: {aprobado[i]}.")
    print("-----------------------------------------------------------------------")