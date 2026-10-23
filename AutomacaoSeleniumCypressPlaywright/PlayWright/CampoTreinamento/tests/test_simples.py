def test_simples():
    assert False, "Este teste falhou propositalmente para fins de demonstração."

def minha_funcao(x, y):
    return x + 2 * y

def test_minha_funcao():
    resultado = minha_funcao(3, 2)
    assert resultado == 7
    print("Resultado da função:", resultado)

def test_loop_numbers():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        print(number)

def test_condicional_if_only():
    x = 10
    y = 10
    if x == y:
        print("x é igual a y")

def test_condicional_if_else():
    x = 10
    y = 5
    if x == y:
        print("x é igual a y")
    else:
        print("x não é igual a y")

def test_condicional_if_elif_else():
    a = 5
    b = 10
    c = 15
    d = 20
    if a == b:
        print("a é igual a b")
    elif a == c:
        print("a é igual a c")
    elif a == d:
        print("a é igual a d")
    else:
        print("a não é igual a b, c ou d")