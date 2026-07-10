class CasoTestes:
    def __init__(self, nome, endpoint, metodo = "GET"):
        self.nome = nome
        self.endpoint = endpoint
        self.metodo = metodo
        self.status = "pendente"
        self.duracao_ms = 0

    def executar(self, duracao_ms, sucesso=True):
        self.duracao_ms = duracao_ms
        self.status = "passou" if sucesso else "falhou"

    def resumo(self):
        return (
            f"[{self.status.upper()}] {self.metodo} {self.endpoint}"
            f"- {self.nome} ({self.duracao_ms} ms)"
        )

caso_teste1 = CasoTestes(nome='Login', endpoint=r'\login', metodo="POST")
caso_teste1.executar(duracao_ms=1000, sucesso=True)
print(caso_teste1.resumo())

class RespostaAPI:
    def __init__(self, endpoint, status_code, corpo, tempo_ms):
        self.endpoint = endpoint
        self.status_code = status_code
        self.corpo = corpo
        self.tempo_ms = tempo_ms

    def is_success(self):
        return self.status_code < 300

    def is_lento(self, limite_ms = 500):
        return self.tempo_ms > limite_ms

    def tem_tempo(self, campo):
        return campo in self.corpo

    def validar(self, campo_obrigatorio = None, limite_ms = 500):
        problemas = []
        if not self.is_success():
            problemas.append(f"Status: {self.status_code} (esperado 2xx)")
        if self.is_lento(limite_ms):
            problemas.append(f"Lento: {limite_ms} ms (Limite: {limite_ms})")
        if campo_obrigatorio and not self.tem_tempo(campo_obrigatorio):
            problemas.append(f"Campo: '{campo_obrigatorio}' ausente")
        return {
            "endpoint": self.endpoint,
            "status_code": "OK" if not problemas else "Falha",
            "problemas": problemas,
        }

login = RespostaAPI(endpoint="/login", status_code=500, corpo='{"mensagem":"sucesso"}', tempo_ms=3)
resultado = login.validar()
print(resultado)