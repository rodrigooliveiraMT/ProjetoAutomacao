def exibier_status_testes(nome, status):
    print(f"Nome: {nome} - Status: {status}")

exibier_status_testes("Abacate", "A")
exibier_status_testes("Abacate", "B")
exibier_status_testes("Abacate", "C")

def classificr_status_code(codigo):
    if 200 <= codigo < 300:
        print(f"Status: {codigo} Sucesso")
    elif 400 <= codigo <500:
        print(f"Status: {codigo} Erro do Cliente")
    elif 500 <= codigo < 600:
        print(f"Status: {codigo} Erro do Servidor")

classificr_status_code(201)
classificr_status_code(401)
classificr_status_code(501)