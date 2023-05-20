import pytest
from playwright.sync_api import Page, Playwright, expect, sync_playwright


@pytest.fixture(scope="function")
def set_up( playwright: Playwright):
    # Start playwright
    browser =  playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open a new page and yeild the page with the browser context
    page = context.new_page()
    # Go to the starting url before each test.
    page.goto("https://sandhill.lib.msu.edu/")
    yield page
    # teardown of the context and browser after tests are done.
    context.close()
    browser.close()

