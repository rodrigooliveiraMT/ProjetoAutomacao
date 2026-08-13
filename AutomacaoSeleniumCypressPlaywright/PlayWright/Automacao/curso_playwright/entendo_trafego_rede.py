import json, pytest
from playwright.sync_api import Page, expect

def test_observar_trafego_rede(page: Page):
    page.on("request", lambda request: print(f">> {request.method} - {request.url}"))
    page.on("response", lambda response: print(f">> {response.status} - {response.url}"))
    page.goto("http://localhost:5000")

def test_observar__apenas_chamadas_api(page: Page):
    def logar_apenas_api(request):
        if '/api/' in request.url:
            print(f">> {request.method} - {request.url}")
    page.on("request", logar_apenas_api)
    page.goto('http://localhost:5000/produtos')

def test_login_dispara_requisicao_real(page: Page):
    requisicoes_login = []
    page.on("request", lambda r: requisicoes_login.append(r) if '/api/login' in r.url else None)
    page.goto('http://localhost:5000/login')
    page.get_by_role("textbox", name="E-mail").fill("cliente@loja.com")
    page.get_by_role("textbox", name="Senha").fill("senha123")
    page.get_by_role("button", name="Entrar").click()
    page.wait_for_url("**/produtos")
    print(requisicoes_login)
    assert len(requisicoes_login) == 1
    assert requisicoes_login[0].method == "POST"

def _fazer_login(page: Page):
    page.goto("http://localhost:5000/login")
    page.fill("#input-email", "cliente@loja.com")
    page.fill("#input-senha", "senha123")
    page.click("#botao-entrar")
    page.wait_for_url("**/produtos")

def test_mock_lista_vazia_produtos(page: Page):
    _fazer_login(page)
    def mock_produtos_vazios(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body="[]",
        )
    page.route("**/api/produtos", mock_produtos_vazios)
    page.reload()
    expect(page.locator('[data-testid^=produto-]')).to_have_count(0)

def test_mock_produto_customizado(page: Page):
    _fazer_login(page)

    produto_fake = [
        {
        "id": 1,
        "nome": "Produto Fake Cup",
        "preco": 1500.00,
        "estoque": 500,
        "imagem": "/static/img/imagem-1.svg",
        }
    ]

    def mock_catalago_customizado(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(produto_fake),
        )

    page.route("**/api/produtos", mock_catalago_customizado)
    page.reload()
    expect(page.locator('[data-testid^=produto-]')).to_have_count(1)
    expect(page.get_by_text("Produto Fake Cup")).to_be_visible()