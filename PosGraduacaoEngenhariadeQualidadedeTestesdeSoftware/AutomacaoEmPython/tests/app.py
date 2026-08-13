def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = num1 + num2

if resultado >= 10:
    print("O resultado é maior ou igual a 10.")
else:
    print("O resultado é menor que 10.")