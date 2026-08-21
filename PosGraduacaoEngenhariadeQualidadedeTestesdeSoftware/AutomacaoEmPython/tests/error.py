def test_erro(page):
    page.goto("https://www.google.com")
    assert page.title() == "Google1" # This assertion will fail, causing an error in the test 