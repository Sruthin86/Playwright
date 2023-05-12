# Playwright

[Official Documentation](https://playwright.dev/python/)
## Overview
* Playwright offers end to end testing for web applications.
* Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
* Playwright offers native mobile emulation of Google Chrome for Android and Mobile Safari.
* Playwright API can be used with Python, Javascript, Typescript, .NET, and Java.

## Test Isolation
* The Playwright Pytest plugin is based on the concept of test fixtures such as the built in page fixture, which is passed into your test. 
* Pages are isolated between tests due to the Browser Context, which is equivalent to a brand new browser profile, where every test gets a fresh environment, even when multiple tests run in a single Browser.

## Testing using pytest

## Testing using node

### Running testing in UI Mode
* [Running tests](https://playwright.dev/docs/intro)

## Setup Commands (TODO - Convert this to an ansible script)
* `docker run -it playwright bash`  run the image as a container
* Install docker compose using `sudo apt-install docker-compose`
* Build and run the docker image using ` docker-compose up -d --build`
* Run the image using docker compose in  detached mode `docker-compose up -d`

