"""
Realizar un programa que solicite al usuario un número entero positivo, y luego en 
pantalla muestre la secuencia de números desde el 1 hasta el número ingresado. 
Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10
"""
equivocado=True
while equivocado==True:
    print("ingrese un numero entero positivo")
    n=int(input())
    if(n>0 and n%1==0):
        for i in range(1, n+1, 1):
            print(f"el numero es {i}")
            equivocado=False
    else:
        print("pone un numero valido la proxima")