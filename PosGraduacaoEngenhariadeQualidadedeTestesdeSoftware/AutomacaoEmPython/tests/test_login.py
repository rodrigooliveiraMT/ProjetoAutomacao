from pathlib import Path

from playwright.sync_api import Page, expect


STORAGE_FILE = Path("storage/state.json")


def test_login(page: Page):
    page.goto("https://seu-site.com/login")

    page.get_by_label("Usuário").fill("seu_usuario")
    page.get_by_label("Senha").fill("sua_senha")

    page.get_by_role("button", name="Entrar").click()

    expect(page).to_have_url("https://seu-site.com/")

    # Salva a sessão autenticada
    STORAGE_FILE.parent.mkdir(parents=True, exist_ok=True)
    page.context.storage_state(path=STORAGE_FILE)