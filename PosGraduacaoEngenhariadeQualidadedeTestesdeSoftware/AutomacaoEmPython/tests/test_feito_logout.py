from playwright.sync_api import Page, expect


def test_logout(page: Page):
    page.goto("https://seu-site.com/dashboard")

    page.get_by_role("button", name="Sair").click()

    expect(page).to_have_url("https://seu-site.com/login")

    expect(
        page.get_by_role("heading", name="Login")
    ).to_be_visible()