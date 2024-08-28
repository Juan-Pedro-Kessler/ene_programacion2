"""
Dado un diccionario de cadenas y sus definiciones, crea una lista que contenga sólo 
las cadenas que comienzan con una letra específica (por ejemplo, "a") indicada por 
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
# Filtrar cadenas que comienzan con la letra específica
cadenas_filtradas = [cadena for cadena in diccionario if cadena.startswith(letra)]

print(cadenas_filtradas)
