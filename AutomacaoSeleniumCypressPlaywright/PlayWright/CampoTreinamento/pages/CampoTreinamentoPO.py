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


    def dialogo_alert(self, botao_locator, texto_esperado):
        def alert(dialog):
            assert dialog.type == "alert"
            assert dialog.message == texto_esperado, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_esperado}"
            dialog.accept()
        self.page.once("dialog", alert)
        botao_locator.click()

    def dialogo_confirm(self, botao, texto1: str, texto_esperado: str, clicar_sim: bool):
        def alert(dialog):
            assert dialog.type == "alert"
            assert dialog.message == texto_esperado, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_esperado}"
            dialog.accept()  # OK no alert
        def confirm(dialog):
            assert dialog.type == "confirm"
            assert dialog.message == texto1, f"Texto apresentado: {dialog.message} - Texto esperado: {texto1}"
            # Prepara o tratamento do alert que virá após a resposta.
            self.page.once("dialog", alert)
            if clicar_sim:
                dialog.accept()   # Sim no confirm
            else:
                dialog.dismiss()  # Cancelar no confirm
        self.page.once("dialog", confirm)
        botao.click()

    def dialogo_prompt(self, botao, texto_prompt: str, numero: str, clicar_prompt: bool, texto_confirm: str, clicar_confirm: bool, texto_alert: str):
        def alert(dialog):
            assert dialog.type == "alert"
            assert dialog.message == texto_alert, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_alert}"
            dialog.accept()  # OK no alert
        def confirm(dialog):
            assert dialog.type == "confirm"
            assert dialog.message == texto_confirm, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_confirm}"
            # O alert aparecerá após responder ao confirm.
            self.page.once("dialog", alert)
            if clicar_confirm:
                dialog.accept()   # Sim
            else:
                dialog.dismiss()  # Cancelar
        def prompt(dialog):
            assert dialog.type == "prompt"
            assert dialog.message == texto_prompt, f"Texto apresentado: {dialog.message} - Texto esperado: {texto_prompt}"
            # O confirm aparecerá após informar o número e clicar em OK.
            if clicar_prompt:
                self.page.once("dialog", confirm)
                dialog.accept(numero)   # Sim
            else:
                self.page.once("dialog", confirm)
                dialog.dismiss()  # Cancelar
        self.page.once("dialog", prompt)
        botao.click()