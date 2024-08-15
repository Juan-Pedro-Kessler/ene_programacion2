"""
Se desea realizar una aplicación que solicite al usuario un caracter y un número 
natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces 
consecutivas. 
Ej:  
Ingrese un caracter: + 
Ingrese la cantidad de repeticiones: 15 
+++++++++++++++ 
"""
print("ingrese el caracter")
car=str(input())
print("ingrese la cantidad n de veces que queres que se repita")
num=int(input())
linea=num*car
print(f"la linea es la siguiente: {linea}")