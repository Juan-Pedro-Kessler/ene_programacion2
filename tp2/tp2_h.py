"""
El mismo almacén del punto anterior almacena los datos del stock de productos en 
el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de 
producto; stock mínimo; stock real”. Escriba un programa, que a partir de 
información contenida en los archivos, genere otro archivo de texto, Compras.txt, 
conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo. 
Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y 
cargarle datos utilizando los códigos de los productos del archivo anterior. Ej: 
100;50;60 
102;50;20 
135;20;15 
138;20;20 
140;10;8 
201;20;30       (  etc…  )
"""
codigo=[]
stockm=[]
stockr=[]
arch = open("stock.txt", "r")
for linea in arch:
    datos = linea.strip().split(";")
    codigo.append(int(datos[0]))
    stockm.append(int(datos[1]))
    stockr.append(int(datos[2]))
arch.close()
with open("compras.txt", "w") as compras:
    tope=len(stockr)
    for i in range(0, tope, 1):
        if stockr[i]<stockm[i]:
            compras.write(f"{codigo[i]};{stockm[i]};{stockr[i]}\n")