frase = 'E Isso Aí'
alfabeto = ' '

qtd_espacos = 0

for letra in frase:
    if letra ==  ' ':
        qtd_espacos += 1

print(f'Existem {qtd_espacos} espaços na frase')
