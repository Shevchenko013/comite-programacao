media = 0
soma = 0

for n in range(0,10):
    numero = int(input(f"Informe o {n+1} º numero -> "))

    soma += numero

print(f"A media é {soma / 10}")