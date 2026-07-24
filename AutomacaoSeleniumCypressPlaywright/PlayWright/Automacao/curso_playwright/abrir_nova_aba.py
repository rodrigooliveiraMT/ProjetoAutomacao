import pytest
from playwright.sync_api import expect

def test_nova_aba(page):
    page.goto("https://bootswatch.com/default/")
    # page.pause()  # deixe só pra debug

    with page.expect_popup() as popup_info:
        page.keyboard.down("Control")
        page.get_by_role("link", name="Help").click()
        page.keyboard.up("Control")

    nova_aba = popup_info.value
    nova_aba.wait_for_load_state()

    texto = nova_aba.locator("#quickstart").text_content()
    print(f"Texto da página: {texto}")

    expect(nova_aba.locator("#quickstart")).to_have_text("Quick Start")
    nova_aba.screenshot(path="nova_aba.png")

    nova_aba.close()
    print(f"Voltamos para: {page.title()}")