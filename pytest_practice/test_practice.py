import pytest
from playwright.sync_api import Page, expect, sync_playwright


# file name should start with test.

@pytest.fixture
def prerequisite(scope = "function"):
    # when scope = function it will run before/after every function
    # when scope = module it will run only once for the complete file.
    # scope = class also works like module but use when test file defined as a class.
    # scope = session

    print('runs before everything else.')
    # we can also return from fixture can be directly accessed by the fixture ref passed as arguemnt to test methods
    return "Done with Prerequisite setup!"

# start with test keyword

def test_first(prerequisite): # fixture name should be passed as argument to run before/after.
    print('hello world')
    assert prerequisite == 'Done with Prerequisite setup!'

def test_second(prerequisite1): print('hello world22222')


# retry flaky test
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_flaky_element(page):
    page.goto("https://example.com")
    # your test logic


# Define parameters: "search_term" and "expected_title"
@pytest.mark.parametrize("search_term, expected_title", [
    ("Playwright", "Playwright"),
    ("Pytest", "pytest: helps you write better programs"),
])
def test_search_and_verify(page: Page, search_term, expected_title):
    page.goto("https://google.com")
    # Using get_by_label as recommended in Playwright Best Practices
    search_input = page.get_by_label("Search", exact=True)
    search_input.fill(search_term)
    search_input.press("Enter")

    expect(page).to_have_title(pytest.match(expected_title))