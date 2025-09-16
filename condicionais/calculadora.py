n1 = float(input("Informe o primeiro numero -> "))
n2 = float(input("Informe o segundo numero -> "))
op = input("Informe a operação -> (+, -, *, /):")

if op == "+":
    print("resultado", n1 + n2)
elif op == "-":
    print("resultado", n1 - n2)
elif op == "*":
    print("resultado", n1 * n2)
elif op == "/":
    if n2 == 0: 
        print("Erro: divisão por zero invalida")
    else:
        print("resultado", n1 / n2)
else:
    print("Operação ivalida")
    
