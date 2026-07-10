if True:
    print("Esta linha está dentro do if!")
    valor = input("Digite um valor: ")
    valor = int(valor)

    if (valor > 10):
        print("Valor > 10")
    elif (valor < 0):
        print("Valor negativo")
    else:
        print("Valor < 10")

print("Esta linha está fora do if!")

if False:
    print("Esta linha está dentro do if!")
    valor = input("Digite um valor: ")
    valor = int(valor)

    if (valor > 10):
        print("Valor > 10")
    elif (valor < 0):
        print("Valor negativo")
    else:
        print("Valor < 10")

"""Comentário Com Três Aspas Duplas"""
print("!\nLinha!")
print("!\tLinha!")
print("!\rLinha!")
print("!\aLinha!")
print("!\fLinha!")
print("!\vLinha!")
print("!\bLinha!")

#|Caractere | Nome               | efeito no print                                 |
#|--------- | ------------------ | ----------------------------------------------- |
#| \n       | nova linha         | avança para a próxima linha                     |
#| \t       | tabulação          | adiciona espaço de tab (indentação)             |
#| \r       | retorno de carro   | volta ao início da linha (em alguns terminals)  |
#| \a       | alarme/som         | emite beep (se o terminal suportar)             |
#| \f       | avanço de página   | forma de controle antigo de papel               |
#| \v       | tabulação vertical | avanço vertical (em poucos ambientes)           |
#| \b       | retrocesso         | remove caractere anterior (em alguns terminais) |
