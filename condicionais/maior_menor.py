número = float(input("Informe o primeiro numero -> "))
número_2 = float(input("Informe o segundo numero -> "))
número_3 = float(input("Informe o terceiro numero -> "))

if número > número_2 and número > número_3:
    print("O numero", número, "é o maior!")
elif  número < número_2 and número_2 < número_3:
    print("O numero", número_2, "é o maior!")
elif número == número_2 == número_3:
    print("Os numeros são iguais")

    print("O numero maior é", número)
else: 
    print("O numero menor é",número_2, número_3)