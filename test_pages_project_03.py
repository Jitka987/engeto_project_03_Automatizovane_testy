from playwright.sync_api import Page


def test_dumlatek_cookies(page: Page):
    cookies_bar = page.locator("#js--cookie_consent_banner_container")
    assert cookies_bar.is_visible() == False
    


def test_voucher(page: Page):
    page.goto("https://www.dumlatek.cz/poukaz/darkovy-poukaz-100-kc/")
    pridat = page.locator(".pdetail__order-btn")
    pridat.click()
    modal = page.locator(".bootbox.modal")
    modal.wait_for(state="visible")
    modal.locator("a.btn.btn--cta", has_text="K pokladně").click()
    page.wait_for_url("https://www.dumlatek.cz/cs/baskets/edit/") 
    page.locator(".js--basket-destroy i.icon").click()
    kosik = page.locator("#basketinfo")
    prazdny_kosik = kosik.get_by_text("(0 Kč)")
    assert prazdny_kosik.is_visible() == True
    
    
def test_find_cotton(page: Page):
    page.get_by_role("textbox", name="...hledat výraz").click()
    page.get_by_role("textbox", name="...hledat výraz").type("bavlna", delay=50)
    page.wait_for_selector(".search-suggestions.js--suggesting-area")
    page.locator(".search-suggestions-category-list li").nth(1).first.click()
    assert page.url == "https://www.dumlatek.cz/katalog/odevni-latky/bavlnene-latky/"

def test_red_dress(page: Page):
    page.click("select[name='f_c[]']")
    page.select_option("[name='f_c[]']", "6")
    page.click("select[name='f_u[]']")
    page.select_option("[name='f_u[]']", "38")
    page.click("select[name='f_m[]']")
    page.select_option("[name='f_m[]']", "74")
    page.click("#quicksearch_form button")
    assert page.url == "https://www.dumlatek.cz/katalog/?f_c%5B%5D=6&f_u%5B%5D=38&f_m%5B%5D=74"
    
    
    