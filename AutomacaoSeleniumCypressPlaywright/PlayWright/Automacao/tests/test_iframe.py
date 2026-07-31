from playwright.sync_api import expect
from pages.iframe_po import iframe_po

def test_iframe(page):
    dsl = iframe_po(page)
    expect(dsl.label_texto).to_be_visible()
    expect(dsl.label_texto).to_have_text("This page is displayed in an iframe1")