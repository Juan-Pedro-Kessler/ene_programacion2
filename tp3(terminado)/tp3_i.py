"""
Dada una lista de números, crea dos listas separadas: una que contenga los 
números pares y otra que contenga los números impares utilizando list 
comprehensions.
"""
numeros=[1,2,3,4,5,6,7,8,9]
numerosi=[numi for numi in numeros if numi%2!=0]
print("los impares son")
print(numerosi)
numerosp=[nump for nump in numeros if nump%2==0]
print("los pares son")
print(numerosp)