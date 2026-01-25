import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup():
    sauce_username = os.getenv("SAUCE_USERNAME")
    sauce_access_key = os.getenv("SAUCE_ACCESS_KEY")

    print("USERNAME EXISTS:", bool(sauce_username))
    print("ACCESS KEY EXISTS:", bool(sauce_access_key))

    if not sauce_username or not sauce_access_key:
        raise Exception("Sauce credentials not available in CI")

    sauce_url = "https://ondemand.saucelabs.com/wd/hub"

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("platformName", "Windows 11")

    options.set_capability("sauce:options", {
        "username": sauce_username,
        "accessKey": sauce_access_key,
        "name": "GitHub Actions Pytest",
        "build": "CI Build"
    })

    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    yield driver
    driver.quit()
