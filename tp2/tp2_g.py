"""
Un almacén guarda los códigos, los nombres de los productos y sus precios, 
respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer 
un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del 
archivo y buscar el precio de un artículo ingresado por teclado. Para probar el 
algoritmo crear un archivo “productos.txt” y cargarle datos al estilo: 
100;arroz;10 
102;fideos;5 
135;lentejas;8 
138;porotos;6 
140;sal gruesa;5 
201;aceite;20       (  etc…  ) 
"""
nombre=[]
codigo=[]
precio=[]
seguir=True
encontrado=False
arch = open("productos.txt", "r")
for linea in arch:
    datos = linea.strip().split(";")
    codigo.append(int(datos[0]))
    nombre.append(str(datos[1]))
    precio.append(int(datos[2]))
arch.close()
while seguir:
    print("ingrese el codigo del producto que desea encontrar: ")
    rt=int(input())
    tope=len(codigo)
    for i in range(0, tope, 1):
        if(codigo[i]==rt):
            encontrado=True
            indice=i
    if(encontrado):
        print(f"nombre: {nombre[indice]}, codigo: {codigo[indice]}, precio: {precio[indice]}")
    else:
        print("el producto no ha sido encontrado")
    encontrado=False
    print("desea seguir?")
    rta=str(input())
    rta=rta.lower()
    if(rta=="no"):
        seguir=False
print("saliendo del programa...")