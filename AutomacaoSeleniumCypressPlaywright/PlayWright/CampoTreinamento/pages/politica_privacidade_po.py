from playwright.sync_api import expect

class PoliticaPrivacidadePO:

    def __init__(self, page):
        self.page = page
        self.titulo = page.locator("#title")
        self.textos = page.locator("#white-background p")

    def validar_texto(self, elemento, texto_esperado):
        assert elemento.inner_text() == texto_esperado, (
            f"Texto esperado: '{texto_esperado}', "
            f"mas foi encontrado: '{elemento.inner_text()}'"
        )

    def validar_politica_privacidade(self, textos_esperados):
        expect(self.textos).to_have_count(len(textos_esperados))

        for indice, texto in enumerate(textos_esperados):
            expect(self.textos.nth(indice)).to_have_text(texto)