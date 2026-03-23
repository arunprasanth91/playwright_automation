import time

from playwright.sync_api import Playwright, Page



def test_playwrightBasics(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    #browser.close()

# chromium, headless mode, 1 single context
def test_playwright_invoke_shortcut(page: Page):
    page.goto("https://rahulshettyacademy.com")



def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    time.sleep(5)

