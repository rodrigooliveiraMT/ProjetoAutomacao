def test_erro(page):
    page.goto("https://www.google.com")
    page.locator("#elemento-que-nao-existe").click()