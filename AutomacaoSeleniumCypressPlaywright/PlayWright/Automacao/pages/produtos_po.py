from pages.BasePage import BasePage

class Produto(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.abrir_navegador("https://automationexercise.com/products")
        self.card_produto = page.locator(".single-products")
        self.button_adicionar_produto = page.locator(".overlay-content:visible .btn")
        self.button_continuar_comprando = page.get_by_role("button", name="Continue Shopping")
        self.button_carrinho = page.locator(".fa.fa-shopping-cart")
        self.button_excluir_item = page.locator(".cart_quantity_delete")
        self.texto_carrinho_vazio = page.get_by_text("Cart is empty!")

    def adicionar_produto_carrinho(self, indice_produto = '0'):
        self.card_produto.nth(indice_produto).hover()
        self.button_adicionar_produto.nth(indice_produto).click()

    def acessar_carrinho(self):
        self.button_carrinho.click()