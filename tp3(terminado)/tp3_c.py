"""
Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas 
las líneas del archivo, utilizando list comprehensions. 
"""
lineas=[]
arch = open("datos.txt", "r")
lineas = [linea for linea in arch]
arch.close()
tope=len(lineas)
for i in range(0, tope, 1):
    print(lineas[i])