import pytest
from playwright.sync_api import expect

def test_iframe(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
    iframe = page.frame_locator("#iframeResult")
    inner_frame = iframe.frame_locator('[src="demo_iframe.htm"]')
    texto = inner_frame.locator("h1").inner_text()
    assert texto == "This page is displayed in an iframe"
    print(texto)