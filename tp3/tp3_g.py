"""
Implemente un programa que le pida una cadena al usuario y cuenta la cantidad de 
vocales en ella. El programa deberá pedirle cadenas al usuario hasta que éste 
introduzca la cadena “salir”. 
"""
def hayvocal(cadena):
    hayvocal=False
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
        
rt=" "
while rt!="salir":
    print("ingrese una cadena para sacar contar sus vocales")
    cadena=str(input())
    cadena=cadena.lower()
    hayvocal(cadena)
    print('ponga "salir" para terminar')
    rt=str(input())
    rt=rt.lower()
print("saliendo del programa...")