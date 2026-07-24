import pytest
from playwright.sync_api import sync_playwright

def pytest_sessionstart(session):
    print("=== INÍCIO DA EXECUÇÃO ===")


def pytest_sessionfinish(session, exitstatus):
    print("\n=== FIM DA EXECUÇÃO ===")


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        no_viewport=True,
        record_video_dir="videos"
        # record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.set_default_timeout(25000)
    page.set_default_navigation_timeout(50000)
    yield page
    context.close()