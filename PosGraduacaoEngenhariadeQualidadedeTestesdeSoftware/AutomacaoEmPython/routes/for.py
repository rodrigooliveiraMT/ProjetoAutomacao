nome = input("Digite o nome do arquivo: ")
print(f"Você digitou: {nome}")

if nome == "for":
    print("Você digitou isso >>> 'for'.")
else:
    print(f"Você não digitou 'for', mas sim {nome}.")

lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(f"Número atual: {numero}")

quantidade = 10
while quantidade > 0:
    print(f"Quantidade atual: {quantidade}")
    quantidade -= 1 #QUERO de 1 a 10, mas está de 10 a 1. Como faço para inverter?Para inverter a contagem de 10 a 1 para 1 a 10, você pode