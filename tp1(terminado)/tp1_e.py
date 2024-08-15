"""
Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.
"""
print("ingrese una cadena de texto para que podamos contar los espacios que tiene")
cadena=str(input())
espacios=cadena.count(" ")
print(f"la cadena tiene estos espacios: {espacios}")