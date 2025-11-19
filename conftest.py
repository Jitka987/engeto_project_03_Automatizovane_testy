from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        page.goto("https://www.dumlatek.cz/")
        page.locator("a.btn.cookie_consent_banner__btn-accept-all").click()
        yield page