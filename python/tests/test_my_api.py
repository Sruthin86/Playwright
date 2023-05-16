from typing import Generator

import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect


# provides consistent content for the test
@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://catalog.lib.msu.edu/"
    )
    yield request_context
    request_context.dispose()

def test_should_create_bug_report(api_request_context: APIRequestContext) -> None:
    headers = {
        "Accept": "application/json",
    }
    query_params = {
      "lookfor": "9780472028870",
      "type": "AllFields",
      "sort": "relevance",
      "page": 1,
      "limit": 1,
      "lng": "en",
    }

    expected_data = {
      'records': [{'authors': {'corporate': [],
                               'primary': {'Rosentreter, Roger L.': []},
                               'secondary': []},
                   'formats': ['Electronic',
                               'eBook'],
                   'id': 'hlm.ebs2490674e',
                   'languages': ['English'],
                   'series': [],
                   'subjects': [['Michigan',
                                 'History.']],
                   'title': 'Michigan a history of explorers, entrepreneurs, and '
                            'everyday people ',
                   'urls': [{'desc': 'ProQuest Ebook Central: 2014 (Ebook Central @ '
                                     'Proquest)',
                             'url': 'https://ezproxy.msu.edu/login?url=https://ebookcentral.proquest.com/lib/michstate-ebooks/detail.action?docID=3570514'}]}],
      'resultCount': 2,
      'status': 'OK',
       }

    books = api_request_context.get(url="/api/v1/search", headers=headers, params=query_params)
    books_response = books.json()
    print(books_response)
    assert books.ok
    assert books.status == 200
    assert books.json()["resultCount"] == 2
    assert books.json() == expected_data


