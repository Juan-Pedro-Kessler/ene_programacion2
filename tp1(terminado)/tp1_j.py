"""
Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un 
rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje 
en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más 
largo, con el fin de evitar problemas de visualización en la consola. Verificar en los 
datos de entrada que se cumpla este requisito. 
"""
print("ingrese el lado ancho")
ancho=int(input())
print("ingrese el lado alto")
alto=int(input())
linea=ancho*"*"
for i in range(0, alto, 1):
    print(f"{linea}")