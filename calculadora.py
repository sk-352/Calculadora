# esse código é uma calculadora simples que realiza operações matemáticas com dois números inseridos pelo usuário
# o usuário insere os números e a operação desejada
num1 = input("Insira o primeiro número: ")
print(num1)
operacao = input("Insira a operação desejada (+, -, *, /, **, %): ")
print(num1, operacao)
num2 = input("Insira o segundo número: ")
print(num1, operacao, num2)

# as condições verificam e realizam a operação matemática desejada
# se o input for inválido, uma mensagem de erro é exibida
if operacao == "+":
    print(f"{num1} + {num2} = ", float(num1) + float(num2))
elif operacao == "-":
    print(f"{num1} - {num2} = ", float(num1) - float(num2))
elif operacao == "*":
    print(f"{num1} * {num2} = ", float(num1) * float(num2))
elif operacao == "/":
    if float(num2) != 0:
        print(f"{num1} / {num2} = ", float(num1) / float(num2))
    else:
        print("É impossível dividir por 0.")
elif operacao == "**":
    print(f"{num1} ^ {num2} = ", float(num1) ** float(num2))
elif operacao == "%":
    if float(num2) != 0:
        print(f"{num1} % {num2} = ", float(num1) % float(num2))
    else:
        print("É impossível dividir por 0.")
else:
    print("Erro na calculadora :(, insira números válidos e uma operação válida.")
