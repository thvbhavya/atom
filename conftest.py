import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup():
    sauce_username = os.getenv("SAUCE_USERNAME")
    sauce_access_key = os.getenv("SAUCE_ACCESS_KEY")

    if not sauce_username or not sauce_access_key:
        raise Exception("Sauce Labs credentials are not set")

    sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "latest")
    options.set_capability("platformName", "Windows 11")

    sauce_options = {
        "username": sauce_username,
        "accessKey": sauce_access_key,
        "name": "Pytest Login Tests",
        "build": "GitHub Actions Build"
    }

    options.set_capability("sauce:options", sauce_options)

    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    yield driver
    driver.quit()
