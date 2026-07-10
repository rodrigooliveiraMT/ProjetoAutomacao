idade = input("Digite sua idade: ")
nome = input("Digite seu nome: ")
idade = int(idade)
nome = nome.upper()

retorno = "Bem-vindo: " + str(nome)
print(retorno, f"sua idade é: {idade}")

if idade > 18:
    retorno = f"Aprovado"
    print(retorno)
elif idade < 18:
    retorno = f"Reprovado"
    print(retorno)
else:
    retorno = f"Aceito"
    for numero in range(1, 11):
        print(retorno + " - " + str( numero))