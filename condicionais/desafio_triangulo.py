x = float(input("Informe o primeiro lado -> "))
y = float(input("Informe o segundo lado -> "))
z = float(input("Informe o terceiro lado -> "))

if x + y > z or x + z > y or y + z > x:
    print("É um triangulo valido")
x == y == z

if x == y == z:
     print(" Triangulo Equilátero")
elif x == y or\
y == z or\
x == z:
    print("Triangulo Isóceles")
elif x != y != z: 
    print("Triangulo escaleno")
else:
    print("Triangulo invalido")

   
