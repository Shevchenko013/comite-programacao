numero = int(input("Informe um numero -> "))
fatorial = 1

for n in range(1, numero + 1):
    fatorial *= n
    print(fatorial)