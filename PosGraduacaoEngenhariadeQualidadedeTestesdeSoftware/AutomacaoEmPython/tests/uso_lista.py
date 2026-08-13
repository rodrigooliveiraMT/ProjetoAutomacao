list = ["soma", "subtracao", "multiplicacao", "divisao"]
print(f"Escolha uma operação: {list[3]}, {list[1]}, {list[2]}, {list[0]}")

def test_soma():
    assert 2 + 2 == 4

def test_subtracao():
    assert 5 - 3 == 2

def test_multiplicacao():
    assert 3 * 4 == 12

def test_divisao():
    assert 10 / 2 == 5