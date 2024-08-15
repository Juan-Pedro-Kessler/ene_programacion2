"""
Escriba un programa que, dada una oración ingresada muestre por pantalla: 
a. El número total de caracteres en la oración 
b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación) 
c. La cantidad de palabras separadas por uno o más espacios 
En este ejercicio, para simplificar, asumiremos que los posibles caracteres de 
entrada son letras, espacios, dígitos, signos de puntuación, signos de 
interrogación y de exclamación. 
Investigar si hay funciones de strings que nos faciliten la resolución [len(), 
.isalpha(), .split() , etc.] 
"""
print("ingrese una oracion")
cadena=str(input())
oracion=cadena.lower()
totalc=len(oracion)
print(f"la cadena tiene {totalc} de caracteres en total")
totall = sum(1 for char in oracion if char.isalpha())
print(f"la cadena tiene {totall} de letras")
totale=0
totale=cadena.count(" ")
print(f"hay {totale} espacios simples")
espacios=totale
totale=cadena.count("  ")
print(f"hay {totale} espacios dobles")
espacios+=totale
digitos = 0
for caracter in cadena:
    if caracter.isnumeric():
        digitos += 1
total=totalc-totale-totall-digitos
print(f"resultados \nhay {totalc} de caracteres, hay {totall} de letras, hay {digitos} de digitos, hay {totale} de espacios y un {total} de caracteres especiales")