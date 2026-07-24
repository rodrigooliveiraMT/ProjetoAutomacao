from pages.produtos_po import Produto
from playwright.sync_api import expect

def test_produtos(page):
    dsl = Produto(page)
    #page.pause()
    preco_produto = int(dsl.card_produto.nth(1).locator(".productinfo h2").inner_text().replace("Rs. ", ""))
    print(preco_produto)
    print(type(preco_produto))
    if preco_produto <= 500:
        dsl.adicionar_produto_carrinho(indice_produto=1)
        print("Produto com valor menor que 500, foi adicionado ao carrinho")
    else:
        print("Produto com valor maior que 500, não foi adicionado ao carrinho")

def test_excluir_itens_carrinho(page):
    dsl = Produto(page)
    page.pause()
    dsl.acessar_carrinho()
    while dsl.button_excluir_item.first.is_visible():
        dsl.button_excluir_item.first.click()
        page.wait_for_timeout(1000)
    else:
        expect(dsl.texto_carrinho_vazio, "Cart is empty!").to_be_visible()