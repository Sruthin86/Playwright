import re
from playwright.sync_api import Page, expect


def test_homepage_has_title_and_browse_link(page: Page):
    page.goto("https://sandhill.lib.msu.edu/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Digital Repository"))

    # find the browse link
    browse = page.get_by_role("link", name="Browse All Turfgrass")

    # Expect an attribute "to be strictly equal" to the value.
    expect(browse).to_have_attribute("href", '/search?&fq=subject_display:("Turf management" OR Turfgrasses OR Grasses)')

    # Click the browse link
    browse.click()

    # Expects the URL to contain search.
    expect(page).to_have_url(re.compile("/search"))
