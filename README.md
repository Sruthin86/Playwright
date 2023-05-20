# Playwright

[Official Documentation](https://playwright.dev/python/)
## Overview
* Playwright offers end to end testing for web applications.
* Playwright is a Node js library made for browser autmation. This is open-source library made by developers at Microsfot.
* Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
* Playwright API can be used with Python, Javascript, Typescript, .NET, and Java.
* Playwright offers native mobile emulation of Google Chrome for Android and Mobile Safari.

## Test Isolation
* The Playwright Pytest plugin is based on the concept of test fixtures such as the built in page fixture, which is passed into your test. 
* Pages are isolated between tests due to the Browser Context, which is equivalent to a brand new browser profile, where every test gets a fresh environment, even when multiple tests run in a single Browser.

## Testing using pytest

## Testing using node

### Running testing
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
### Pytest Fixtures
* Test fixtures are used to establish environment for each test, giving the test everything it needs and nothing else.
* Fixtures are isolated between each tests

#### Scopes
* `function` - This is the default scope. The fixture setup and teardown is performed for each test function that requests it.
* `class` - The fixture setup and teardown is performed once per test class. Even if multiple test functions within the test classe, the fixture setup/teardown will only be performed once.
* `module` - The fixture setup and teardown is performed once per module. If you have multiple test functions within a module requesting the same fixture, the fixture setup/teardown will be performed once.
* `package` - The fixture setup and teardown is performed once per package. No matter how many tests request the fixture, the fixture setup/teardown will only be performed once.
* `session` - The fixture setup and teardown is performed only once per session, regardless of the number of tests requesting it. A session is simply a single Pytest executed run.

### API Testing
* Playwright can be used to get access to the REST API of your application.
* It uses `APIRequestContext` methods to test REST API.
* It also shares your browser content and cookie storage.
* [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext) can send all kinds of HTTP(S) requests over network.
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



## Setup Commands (TODO - Convert this to an ansible script)
* `docker run -it playwright bash`  run the image as a container
* Install docker compose using `sudo apt-install docker-compose`
* Build the docker image using `docker build . -t playwright`
* Run the image using docker compose in  detached mode `docker-compose up -d`

