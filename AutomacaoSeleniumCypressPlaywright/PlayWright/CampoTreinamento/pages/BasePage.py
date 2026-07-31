from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def abrir_navegador(self, url, url_base = ''):
        self.page.goto(url or url_base)

    def validar_texto_input(self, elemento, texto_esperado):
        expect(elemento).to_have_value(texto_esperado)
    
    def validar_texto_button(self, elemento, texto_esperado):
        expect(elemento).to_have_text(texto_esperado)
        expect(elemento).to_contain_text(texto_esperado)

    def abrir_nova_guia(self, elemento):
        with self.page.expect_popup() as popup_info:
            elemento.click()
        nova_guia = popup_info.value
        nova_guia.wait_for_load_state()
        return nova_guia