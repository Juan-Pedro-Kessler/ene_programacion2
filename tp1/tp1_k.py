"""
 Escriba un programa que permita el ingreso de números enteros positivos para 
calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número 
negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej: 
“El promedio es ….. con un total de …. ingresos.”
"""
seguir=True
total=0
valores=0
while seguir:
    print("ingrese un numero positivo")
    a=int(input())
    if a>0:
        total+=a
        valores+=1
    elif a<0:
        seguir=False
print(f"se ingresaron {valores} valores, el total es de {total} y el promedio es de {total/valores}")