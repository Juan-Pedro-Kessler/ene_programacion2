"""
Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad 
total de vocales que aparecen y lo muestre por pantalla. 
"""
hayvocal=False
print("ingresa una cadena")
cadena=str(input())
if cadena.count('a')>0:
    print(f"la letra a se repite {cadena.count('a')}")
    hayvocal=True
if cadena.count('e')>0:
    print(f"la letra e se repite {cadena.count('e')}")
    hayvocal=True
if cadena.count('i')>0:
    print(f"la letra i se repite {cadena.count('i')}")
    hayvocal=True
if cadena.count('o')>0:
    print(f"la letra o se repite {cadena.count('o')}")
    hayvocal=True
if cadena.count('u')>0:
    print(f"la letra u se repite {cadena.count('u')}")
    hayvocal=True
if hayvocal==False:
    print("no habia vocales en la cadena")