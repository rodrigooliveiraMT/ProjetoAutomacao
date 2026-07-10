usuario = {
    "nome": "servidor",
    "email": "teste@gmail.com",
    "senha": "123com",
    "idade": 30,
    "ativo": True
}

print(usuario)
# retorno: {'nome': 'servidor', 'email': 'teste@gmail.com', 'senha': '123com', 'idade': 30, 'ativo': True}

print(usuario.keys())
# retorna apenas as chaves: ['nome', 'email', 'senha', 'idade', 'ativo']

print(usuario.values())
# retorna apenas os valores: ['servidor', 'teste@gmail.com', '123com', 30, True]

# Pegar uma informação específica
print(usuario["nome"])
print(usuario["idade"])

# adicionar uma nova informação na chave
produto = {
    "nome": "farinha",
    "email": "teste@farinha.com",
    "senha": "123com",
    "idade": 30,
    "ativo": True
}

produto["valor"] = 30.50
print(produto)
#mudar dado da chave
produto['ativo'] = False
print(produto)
#remover elemento
produto.pop("idade")
print(produto)
#descobrir o tamanho da chave
print(len(produto))

#Utilização de FOR
vendas = {
    "Nome": "Abacate",
    "Email": "teste@vendas.com",
    "Senha": "123",
}

#Imprimir somente valores
for valor in vendas:
    print(valor)

#Imprimir chaves e valores
for chave, valor in vendas.items():
    print(chave, valor)

#Imprimir somente chaves
for chave in vendas.keys():
    print(chave)

#Verificar-se possui chave VENDAS
if "Nome" in vendas:
    print("Chave encontrada")

#Verificar-se possui valor VENDAS
if "Abacate" in vendas.values():
    print("Valor encontrada")