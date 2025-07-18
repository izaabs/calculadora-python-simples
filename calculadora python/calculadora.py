n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número:"))
operacao = input("Escolha uma das operações (+, -, *, /):")

if operacao == '+':
    print("O resultado é: ", n1+n2)
elif operacao == '-':
    print("O resultado é: ", n1-n2)
elif operacao == '*':
    print("O resultado é: ", n1*n2)
elif operacao == '-':
    print("O resultado é: ", n1/n2)
else:
    print("Operação inválida!")
