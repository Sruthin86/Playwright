import re
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    page.goto("https://sandhill.lib.msu.edu/")
    yield
    print("afterEach")

def test_turf_grass(page: Page):
    # find the browse link
    browse = page.get_by_role("link", name="Browse All Turfgrass")

    # Expect an attribute "to be strictly equal" to the value.
    expect(browse).to_have_attribute("href", '/search?&fq=subject_display:("Turf management" OR Turfgrasses OR Grasses)')

    # Click the get started link.
    browse.click()
    expect(page).to_have_url(re.compile("/search"))

def test_turf_grass(page: Page):
    # find the browse link
    browse = page.get_by_role("link", name="Cookbooks")

    # Expect an attribute "to be strictly equal" to the value.
    expect(browse).to_have_attribute("href", '/search?fq=genre_aat:Cookbooks')

    # Click the get started link.
    browse.click()
    expect(page).to_have_url(re.compile("/search"))
    

