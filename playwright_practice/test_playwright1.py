import time

from playwright.sync_api import Playwright, Page, expect
from pytest_playwright.pytest_playwright import browser


def test_playwrightBasics(playwright: Playwright) -> None:
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
    devices = ["Samsung Note 8", "iphone X"]
    # instead of below code we can also use filter locator in playwright
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    print(f" iphone_product = {iphone_product.text_content()}")
    products = page.locator("//app-card-list[@class='row']//div[@class='card h-100']").all()
    for product in products:
        if product.locator("h4 a").text_content() in devices:
            print(product.locator("p").text_content())
            product.get_by_role("button", name = "Add ").click()
    time.sleep(3)
    page.locator("//a[@class='nav-link btn btn-primary']").click()
    expect(page.locator(".media-body")).to_have_count(len(devices))


def test_auto_wait_IncorrectCredentials(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefox_run(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    test_auto_wait_IncorrectCredentials(page)


def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText:first-child").click()
        child_page = newPage_info.value
        email_text = child_page.locator(".red").text_content()
        print(email_text.split("at ")[1].split(" with")[0].strip())



def test_get_by_placeholder(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


def test_js_alert(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(5)
    page.on("dialog", lambda dialog : dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(3)


def test_iframe(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frame = page.frame_locator("#courses-iframe")
    frame.get_by_role("link", name="All Access plan").click()
    expect(frame.locator("body")).to_contain_text(" Happy Subscibers!")


def test_handling_webtables(page: Page):
    price_column = None
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # get index of price column
    price_col = True
    for index in range(page.locator(".table-bordered tr").count()):
        if price_col and page.locator(".table-bordered tr").nth(index).filter(has_text="Price").count() > 0:
            price_column = index
            price_col = False
        if page.locator(".table-bordered tr").nth(index).filter(has_text="Tomato").count() > 0:
            expect(page.locator(".table-bordered tr").nth(index).locator("td").nth(price_column + 1)).to_contain_text("37")
            break

def test_mouse_hover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()



