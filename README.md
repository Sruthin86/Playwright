# Playwright


[Official Documentation](https://playwright.dev/python/)
## Overview
* Playwright offers end to end testing for web applications.
* Playwright is a Node js library made for browser automation. This is an open-source library made by developers at Microsoft.
* Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
* Playwright API can be used with Python, Javascript, Typescript, .NET, and Java.
* Playwright offers native mobile emulation of Google Chrome for Android and Mobile Safari.


## Test Isolation
* The Playwright Pytest plugin is based on the concept of test fixtures such as the built in page fixture, which is passed into your test.
* Pages are isolated between tests due to the Browser Context, which is equivalent to a brand new browser profile, where every test gets a fresh environment, even when multiple tests run in a single Browser.


## Playwright Locators
* [Locators](https://playwright.dev/docs/locators) represent a way to find elements on the page at the given state of the page
* Recommended built in locators
```
page.getByRole() to locate by explicit and implicit accessibility attributes.
page.getByText() to locate by text content.
page.getByLabel() to locate a form control by associated label's text.
page.getByPlaceholder() to locate an input by placeholder.
page.getByAltText() to locate an element, usually image, by its text alternative.
page.getByTitle() to locate an element by its title attribute.
page.getByTestId() to locate an element based on its data-testid attribute (other attributes can be configured).


```


## Testing using pytest


### Running tests
* [Running tests](https://playwright.dev/docs/intro)


* Running tests on Chromium
```
pytest
```


* Running a single test file
```
pytest test_file_name.py
```
* Run a set of test files
```
pytest tests/first-page/ tests/next-page/
```
* Run the test with the function name
```
pytest -k "test_function_name"
```


* Running tests in headed mode
```
pytest --headed test_login.py
```


* Running Tests on specific browsers
```
pytest test_file_name.py --browser webkit
```
* Running Tests on multiple browsers
```
pytest test_file_name.py --browser webkit --browser firefox
```
* Running Tests in parallel
```
pytest --numprocesses auto
```
* Running test in debug mode in an editor of your choice
```
PWDEBUG=1 pytest -s
```
* Generate test code using pytest
```
playwright codegen
```
### Pytest Fixtures
* Test fixtures are used to establish environment for each test, giving the test everything it needs and nothing else.
* Fixtures are isolated between each tests


#### Scopes
* `function` - This is the default scope. The fixture setup and teardown is performed for each test function that requests it.
* `class` - The fixture setup and teardown is performed once per test class. Even if multiple test functions are within the test class, the fixture setup/teardown will only be performed once.
* `module` - The fixture setup and teardown is performed once per module. If you have multiple test functions within a module requesting the same fixture, the fixture setup/teardown will be performed once.
* `package` - The fixture setup and teardown is performed once per package. No matter how many tests request the fixture, the fixture setup/teardown will only be performed once.
* `session` - The fixture setup and teardown is performed only once per session, regardless of the number of tests requesting it. A session is simply a single Pytest executed run.


### API Testing
* Playwright can be used to get access to the REST API of your application.
* It uses `APIRequestContext` methods to test REST API.
* It also shares your browser content and cookie storage.
* [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext) can send all kinds of HTTP(S) requests over the network.
```
api_request_context.get(url, params=query_params)


api_request_context.post(url, **kwargs)


api_request_context.put(url, **kwargs)


api_request_context.delete(url, **kwargs)
```
* Requesting headers of a url
```
api_request_context.head(url)
```


## Testing using npx


### Running tests
* [Running tests](https://playwright.dev/docs/intro)


* Running tests on Chromium
```
npx playwright test
```


* Running a single test file
```
npx playwright test test_file_name.py
```
* Run a set of test files
```
npx playwright test tests/first-page/ tests/next-page/
```
* Run the test with the "string" in file name
```
npx playwright test {string1} {string2}
```


* Running tests in headed mode
```
npx playwright test test_login --headed
```


* Running Tests on specific browsers
```
npx playwright test --browser=firefox
```
* Running Tests on all browsers
```
npx playwright test --browser=all
```
* Running Tests on multiple browsers
```
npx playwright test test_file_name.py --browser webkit --browser firefox
```
* Running Tests in parallel
```
npx playwright test --workers 4
```
* Running test in debug mode in an editor of your choice
```
PWDEBUG=1 npx playwright test
```
* Generate tests using codegen
```
npx playwright codegen
```




## Setup Commands - Python project (TODO - Convert this to an ansible script)
* Install docker compose using `sudo apt-install docker-compose`
* Build the docker image using `docker build . -t playwright`
* Run the image as a container using `docker run -it playwright bash`
* Run the image using docker compose in  detached mode `docker-compose up -d`


## Setup Commands - JavaScript project (TODO - Convert this to an ansible script)
* Install docker compose using `sudo apt-install docker-compose`
* Build the docker image using `docker build . -t playwright-jammy`
* Run the image as a container using `docker run -it playwright-jammy bash`
* Run the image using docker compose in  detached mode `docker-compose up -d`
