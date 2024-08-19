"""
Escribir un procedimiento “reverso” que permita ingresar como parámetro una 
cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego 
un programa que determine si una cadena de caracteres es un palíndromo (un 
palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”). 
Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas, 
utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es 
distinto a radaR.
"""
a=True
print("ingrese una palabra: ")
palabra=str(input())
palabra=palabra.lower()
palabrai=""
tope=len(palabra)
caracteres=tope-1
palindromo=True
while a:
    print("deseas averiguar si es un palindromo o ver la cadena invertida(invertida o palindromo)")
    rt=str(input())
    if rt=="invertida":
        for i in range(0, tope, 1):
            palabrai+=palabra[caracteres]
            caracteres-=1
        print(f"la palabra es {palabra} y la invertida es {palabrai}")
    if rt=="palindromo":
        for i in range(0, tope // 2):
            if palabra[i] != palabra[tope - i - 1]:  # Comparar extremos
                palindromo = False
                break
        if palindromo:
            print("la palabra es palindromo")
    print("deseas seguir? si o no")
    rt=str(input())
    if rt=="no":
        a=False