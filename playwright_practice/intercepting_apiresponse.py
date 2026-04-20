import time

from playwright.sync_api import Page, Route

fake_order_response = {"data" : [] , "message" : "No Orders"}

def intercept_response(route: Route) -> None:
    route.fulfill(json = fake_order_response)

def test_with_intercepted_api_response(page: Page) -> None:
    page.goto("https://www.rahulshettyacademy.com/client/")
    page.route("https://www.rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
    assert order_text == "You have No orders at this moment!"




# intercept api request calls


def intercept_request(route: Route) -> None:
    route.continue_(url = f"https://www.rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67768wea87127288a182")


def test_with_intercepted_request(page: Page) -> None:
    page.goto("https://www.rahulshettyacademy.com/client/")
    page.route("https://www.rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    assert message == "You are not authorized to view this order."

