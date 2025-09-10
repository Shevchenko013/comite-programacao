idade = int(input("Informe a idade -> "))

if  0 <= idade <= 12:
     print("Voce é uma criança")
elif 13 <= idade <= 17:
    print("Voce é um adolescente")
elif 18 <= idade <= 59:
     print("Voce é um adulto")
else:
    print("Idade invalida")
    