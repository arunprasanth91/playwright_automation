from playwright.sync_api import Page, Route, expect, Playwright

from playwright_practice.apiBase import APIUtils


# Token are stored in browser local storage or session storage.

def test_api_cookies(playwright: Playwright):
    token = APIUtils().getToken(playwright)
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localstorage.setitem('token','{token}')""")
    page.goto("https://rahulettyacademy.com/client")
    page.get_by_role("button", name= "ORDERS").click()
    time.sleep(5)



