"""
Escriba un programa que para un texto ingresado nos muestre cual es la palabra 
más larga dentro de ese texto y cuántas letras tiene. 
"""
print("ingrese una frase")
frase=str(input())
palabras=frase.split(" ")
elementos=len(palabras)
max=palabras[0]
for i in range(0, elementos, 1):
    if len(palabras[i])>len(max):
        max=palabras[i]
print(f"la palabra mas larga es {max} y tiene {len(max)} letras")