import re
import pytest
from playwright.sync_api import Page, Playwright, expect, sync_playwright


def test_turf_grass(set_up):
    page = set_up
    # find the browse link
    browse = page.get_by_role("link", name="Browse All Turfgrass")

    # Expect an attribute "to be strictly equal" to the value.
    expect(browse).to_have_attribute("href", '/search?&fq=subject_display:("Turf management" OR Turfgrasses OR Grasses)')

    # Click the browse link.
    browse.click()
    expect(page).to_have_url(re.compile("/search"))


