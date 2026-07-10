class ResultadoTeste:
    def __init__(self, nome):
        self.nome = nome
        self._status = "pendente"

    def difinir_status(self, novo_status):
        validos = ["pendente", "passou", "falhou", "bloqueado"]
        if novo_status not in validos:
            raise ValueError(f"Status {novo_status} inválido")
        self._status = novo_status

teste = ResultadoTeste("Teste")
teste.difinir_status = "aprovado"
print(teste.difinir_status)

print()

class ContadorTestes:
    def __init__(self, nome_suite):
        self.nome_suite = nome_suite #Público
        self._valor = 0              #Protegido
        self.__segredo = "Será"     #Privado

contador = ContadorTestes("Hellow")

print(contador.nome_suite)  # Funciona
print(contador._valor)      # Funciona, mas não é o indicado (Apresenta aviso)
print(contador._ContadorTestes__segredo) # Funciona
#print(contador.__segredo)   # Não Funciona, apresenta AttributeError!

print()

class Ambiente:
    def __init__(self, nome, url):
        self.nome = nome
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, nova_url):
        if not nova_url.startswith("https://"):
            raise ValueError(f"URL deve começar com https://")
        self._url = nova_url

    @property
    def esta_ativo(self):
        return self._url is not None and len(self._url) > 0

homologacao = Ambiente("hml", "https://homologacao.com")

print(homologacao.url)
homologacao.url = "https://dev.homologacao.com"
print(homologacao.url)
print(homologacao.esta_ativo) # Serve somente para leitura da mensagem

print()

class CasoTestes:
    def __init__(self, id_teste, nome, prioridade = "média"):
        self.id_teste = id_teste
        self.nome = nome
        self.prioridade = prioridade
        self._status = "pendente"

    def __str__(self) -> str:
        return f"[{self._status.upper()} - {self.id_teste} - {self.nome}]"

tc = CasoTestes("TC-001", "Login Válido")
print(tc) # Retorno: [PENDENTE] - TC-0001 - Login Válido