contagem_pares = 0
for numero in range(2, 51, 2):
    contagem_pares += 1

    print(contagem_pares)


for indice, numero, in enumerate(range(2,51,2)):
    print(indice + 1, numero)