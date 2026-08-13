from playwright.sync_api import Page, expect


def test_acesso_area_autenticada(page: Page):
    page.goto("https://seu-site.com/dashboard")

    expect(page).to_have_url("https://seu-site.com/dashboard")

    expect(
        page.get_by_role("heading", name="Dashboard")
    ).to_be_visible()