from pages.BasePage import BasePage
from resources.CampoTreinamentoUrl import url_campo_treinamento

class CampoTreinamentoPO(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navedor(url_campo_treinamento)
        self.iframe = self.page.frame_locator("#frame1")
        self.botao = self.iframe.locator("#frameButton")
        self.input_nome = self.page.locator("#elementosForm\\:nome")
        self.input_sobrenome = self.page.locator("#elementosForm\\:sobrenome")
        self.radio_sexo_masculino = self.page.locator("#elementosForm\\:sexo\\:0")
        self.radio_sexo_feminino = self.page.locator("#elementosForm\\:sexo\\:1")
        self.button_simple = self.page.locator("#buttonSimple")


    def alert(self, texto_esperado, elemento):
        def handle_dialog(dialog):
                assert dialog.type == "alert"
                assert texto_esperado in dialog.message, f"Mensagem de alerta incorreta: {format(dialog.message)}"
                dialog.accept()
        self.page.on("dialog", handle_dialog)
        elemento.click()