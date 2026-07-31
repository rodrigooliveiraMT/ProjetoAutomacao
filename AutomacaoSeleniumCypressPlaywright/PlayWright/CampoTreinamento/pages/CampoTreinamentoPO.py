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
        self.iframe = self.page.frame_locator("#frame1")
        self.botao = self.iframe.locator("#frameButton")
        self.input_nome = self.page.locator("#elementosForm\\:nome")
        self.input_sobrenome = self.page.locator("#elementosForm\\:sobrenome")
        self.radio_sexo_masculino = self.page.locator("#elementosForm\\:sexo\\:0")
        self.radio_sexo_feminino = self.page.locator("#elementosForm\\:sexo\\:1")
        self.input_campo_novo = self.page.locator("#novoCampo")
        self.button_alert = self.page.locator("#alert")
        self.button_confirm = self.page.locator("#confirm")
        self.button_prompt = self.page.locator("#prompt")


    def alerta(self, texto_esperado, elemento):
        def handle_dialog(dialog):
                assert dialog.type == "alert"
                assert texto_esperado in dialog.message, f"Mensagem de alerta incorreta: {format(dialog.message)}"
                dialog.accept()
        self.page.on("dialog", handle_dialog)
        elemento.click()

    def confirmar(
        self,
        elemento,
        texto_confirmacao,
        aceitar_confirmacao=True,
        texto_alerta=None
    ):
        dialogos = []

        def handle_dialog(dialog):
            indice = len(dialogos)
            dialogos.append((dialog.type, dialog.message))

            if indice == 0:
                if aceitar_confirmacao:
                    dialog.accept()
                else:
                    dialog.dismiss()
            else:
                # Segundo diálogo: alert
                dialog.accept()

            self.page.on("dialog", handle_dialog)

            try:
                elemento.click()
            finally:
                self.page.remove_listener("dialog", handle_dialog)

            if len(dialogos) != 2:
                raise AssertionError(
                    f"Esperados 2 diálogos, encontrados {len(dialogos)}."
                )

            tipo, mensagem = dialogos[0]

            if tipo != "confirm":
                raise AssertionError(f"Tipo esperado: confirm. Obtido: {tipo}")

            if texto_confirmacao not in mensagem:
                raise AssertionError(
                    f"Mensagem esperada: {texto_confirmacao}. Obtida: {mensagem}"
                )

            tipo, mensagem = dialogos[1]

            if tipo != "alert":
                raise AssertionError(f"Tipo esperado: alert. Obtido: {tipo}")

            if texto_alerta not in mensagem:
                raise AssertionError(
                    f"Mensagem esperada: {texto_alerta}. Obtida: {mensagem}"
                )

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