print("ingrese el lado a")
a=int(input())
print("ingrese el lado b")
b=int(input())
print("ingrese el lado c")
c=int(input())
if(a==b and a==c):
    print("el triangulo es esquilatero")
if(a == b or a == c or b == c):
    print("el triangulo es isoceles")
if(a!=b and a!=c and b!=c):
    print("el triangulo es escaleno")