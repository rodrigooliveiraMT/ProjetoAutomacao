emails = ["teste1@gmail.com", "teste2@hotmail", "teste3@support.com.br", 18, 28]
print(f"Índice 0: " + str(emails[0]))
print(f"Índice 1: " + str(emails[1]))
print(f"Índice 2: " + str(emails[2]))
print(f"Índice 3: " + str(emails[3]))
print(f"Índice 4: " + str(emails[4]))

print()

resultado = ["teste1@gmail.com", "teste2@hotmail", "teste3@support.com.br"]
print(f"Índice 0: " + resultado[0])
print(f"Índice 1: " + resultado[1])
print(f"Índice 2: " + resultado[2])

print()

ambiente = ["Release", "Stage", "Homologação", "Produção"]
print(ambiente[0]) # Release
print(ambiente[1]) # Stage
print(ambiente[2]) # Homologação
print(ambiente[3]) # Produção
print("==============")
print("Inverter Ordem")
print("==============")
print(ambiente[-1]) # Produção
print(ambiente[-2]) # Homologação
print(ambiente[-3]) # Stage
print(ambiente[-4]) # Release

print()

# Cenário: inserir o admin sempre na primeira posição da lista
usuarios = ["ana@gmail.com", "carolina@gmail.com"]

usuarios.insert(0, "leticia@gmail.com")
print(usuarios)
# Retorno: ['leticia@gmail.com', 'ana@gmail.com', 'carolina@gmail.com']

print()

# Remover e captura o item removido
usuarios1 = ['leticia@gmail.com', 'ana@gmail.com', 'carolina@gmail.com']
removido = usuarios1.remove("leticia@gmail.com") # remove a primeira informação declarada
print(f"Usuário Removido: {removido}")
print(f"lista de usuários: {usuarios1}")
# Retorno: ['ana@gmail.com', 'carolina@gmail.com']
print("------------------------------------------------------")
usuarios2 = ['leticia@gmail.com', 'ana@gmail.com', 'carolina@gmail.com']
removido = usuarios2.pop(1) # remove a informação escolhida de acordo com o índice
print(f"Usuário Removido: {removido}")
print(f"lista de usuários: {usuarios2}")
# Retorno: ['leticia@gmail.com', 'carolina@gmail.com']
print("------------------------------------------------------")
usuarios3 = ['leticia@gmail.com', 'ana@gmail.com', 'carolina@gmail.com']
removido = usuarios3.pop() # remove a última informação
print(f"Usuário Removido: {removido}")
print(f"lista de usuários: {usuarios3}")
# Retorno: ['leticia@gmail.com', 'ana@gmail.com']
print()

# Cenáio: validar se o número de resultados pela API está correta
resultado_api = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7"]

total = len(resultado_api)
print(f"Total de resultados: {total}")
# Retorno = 7

esperado = 5
if len(resultado_api) == esperado:
    print("Quantidade de resultados correta.")
else:
    print(f"Esperava: {esperado}, mais veio {len(resultado_api)}")

print()

caso_test_lista = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"]
for indice, valor in enumerate(caso_test_lista):
    print(f"{indice}: {valor}")

print()

caso_test_lista = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"]
for indice, valor in enumerate(caso_test_lista):
    print(f"{indice +1}: {valor}")

print()

# VERIFICAR-SE UM DETERMINADO DADO EXISTE NA LISTA
codigos_sucesso = [200, 201, 202, 203, 204, 205, 206]
codigos_recebido = 201

if codigos_recebido in codigos_sucesso:
    print(f"Codigo {codigos_recebido} é um código de sucesso")
else:
    print(f"Codigo {codigos_recebido} não erá esperado")
# retorno: Código 201 é um código de sucesso

codigos_sucesso = [400, 401, 402, 403, 404, 405, 406]
codigos_recebido = 210

if codigos_recebido in codigos_sucesso:
    print(f"Código {codigos_recebido} é um código de sucesso")
else:
    print(f"Código {codigos_recebido} não erá esperado")
# retorno: Código 210 não erá esperado

# VERIFICAR-SE CÓDIGO RETORNADO PERTENCE A LISTA
codigos_servidor = [500, 501, 502, 503, 504, 505, 506]

codigo_servidor_recebido = 404
if codigos_servidor not in codigos_sucesso:
    print(f"Código {codigo_servidor_recebido} não é um erro crítico de servidor")