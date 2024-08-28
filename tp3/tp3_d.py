"""
Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo 
las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por 
el usuario, utilizando list comprehensions. 
"""
diccionario = {
    "amarillo": "Amarillo amarillo los platanos",
    "boludo": "te vas a morir virgen boludoooo",
    "culos": "que rico culito que tenes mamiiii",
    "daniel": "danieeeeel",
    "marcelo": "agachate y conocelo",
    "marito": "maritoooooo"
}

print("ingresa la letra")
letra=input()
# Filtrar palabras que comienzan con la letra específica
palabras_filtradas = [palabra for palabra in diccionario if palabra.startswith(letra)]

print(palabras_filtradas)
