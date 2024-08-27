"""
Implemente una función que, dada una lista de números, devuelva una nueva lista 
que contenga el cuadrado de cada número utilizando list comprehensions. 
"""
rt=1
listanueva=[]
lista=[]
while rt != 0:
    print("elegi un numero, pone 0 para terminar")
    rt=int(input())
    if rt !=0:
        lista.append(rt)
listanueva = [elem**2 for elem in lista]
tope=len(listanueva)
for i in range(0, tope, 1):
    print(f"el cuadrado de {lista[i]} es {listanueva[i]}")