"""
Dado un rango de números, crea una lista que contenga todos los números primos 
dentro de ese rango utilizando list comprehensions. 
"""
def esprimo(n):
    a=0
    for j in range(1, n+1, 1):
        if n%j==0:
            a=a+1
    if a<=2:
        return True
    else:
        return False
primos=[]
print("elija un rango de numero")
rango=int(input())
for i in range(0, rango+1, 1):
    primos=[n for n in range(1, rango+1, 1) if esprimo(n)]
print(primos)