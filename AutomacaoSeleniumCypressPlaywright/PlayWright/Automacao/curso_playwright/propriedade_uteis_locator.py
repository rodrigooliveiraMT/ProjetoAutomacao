import pytest

def test_locate(page):
    page.goto("https://bootswatch.com/default/")

    texto_com_inner_text = page.get_by_text("Navbars").inner_text()
    print("Resultado: ", texto_com_inner_text)

    texto_sem_inner_text = page.get_by_text("Navbars")
    print("Resultado: ", texto_sem_inner_text)