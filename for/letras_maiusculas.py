frase = 'E Isso Aí'
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVYWXZ'

qtd_maiusculas = 0

for letra in frase:
    for letra_alfabeto in alfabeto:
        if letra == letra_alfabeto:
            qtd_maiusculas += 1
print(f'Existem {qtd_maiusculas} letra maiusculas')


