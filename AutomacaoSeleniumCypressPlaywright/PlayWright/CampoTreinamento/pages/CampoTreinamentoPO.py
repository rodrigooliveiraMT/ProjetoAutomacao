from playwright.sync_api import expect

from pages.BasePage import BasePage
from resources.CampoTreinamentoUrl import url_campo_treinamento

class CampoTreinamentoPO(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador(url_campo_treinamento)
        self.button_simple = self.page.locator("#buttonSimple")
        self.button_abri_popup = self.page.locator("#buttonPopUpEasy")
        self.input_textarea = self.page.locator("textarea")
        self.button_abri_popup_hard = self.page.locator("#buttonPopUpHard")
        self.button_resposta_demorada = self.page.locator("#buttonDelay")
        self.inner_iframe = self.page.frame_locator("#frame1")
        self.ifram1 = self.inner_iframe.locator("#frameButton")
        self.input_nome = self.page.locator("#elementosForm\\:nome")
        self.input_sobrenome = self.page.locator("#elementosForm\\:sobrenome")
        self.radio_sexo_masculino = self.page.locator("#elementosForm\\:sexo\\:0")
        self.radio_sexo_feminino = self.page.locator("#elementosForm\\:sexo\\:1")
        self.input_campo_novo = self.page.locator("#novoCampo")
        self.button_alert = self.page.locator("#alert")
        self.button_confirm = self.page.locator("#confirm")
        self.button_prompt = self.page.locator("#prompt")


    def handle_alert(self, botao_locator, texto_esperado):
        def _on_dialog(dialog):
            assert dialog.type == "alert"
            assert dialog.message == texto_esperado, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_esperado}"
            dialog.accept()
        self.page.once("dialog", _on_dialog)
        botao_locator.click()

    def handle_confirm(self, botao, texto_confirm: str, confirmar: bool, texto_alert_final: str):
        mensagens = []

        def primeiro(dialog):
            print("PRIMEIRO:", dialog.type, dialog.message)
            mensagens.append((dialog.type, dialog.message))
            if confirmar:
                dialog.accept()
            else:
                dialog.dismiss()

        def segundo(dialog):
            print("SEGUNDO:", dialog.type, dialog.message)
            mensagens.append((dialog.type, dialog.message))
            dialog.accept()

        self.page.once("dialog", primeiro)
        self.page.once("dialog", segundo)
        botao.click()

        print("MENSAGENS CAPTURADAS:", mensagens)

        assert mensagens[0] == ("confirm", texto_confirm)
        assert mensagens[1] == ("alert", texto_alert_final)

    