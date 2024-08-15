"""
Se desea realizar una aplicación que solicite al usuario tres números enteros 
positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén 
entre A y B inclusive.  
"""
print("ingrese a")
a=int(input())
print("ingrese b")
b=int(input())
print("ingrese x")
x=int(input())
for i in range(a, b+1, 1):
    print(f"{x*i}")