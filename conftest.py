import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def setup():
    sauce_username = os.getenv("SAUCE_USERNAME")
    sauce_access_key = os.getenv("SAUCE_ACCESS_KEY")

    sauce_url = f"https://{sauce_username}:{sauce_access_key}@ondemand.us-west-1.saucelabs.com:443/wd/hub"

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "latest")

    sauce_options = {
        "name": "Pytest Login Tests",
        "build": "GitHub Actions Build",
        "seleniumVersion": "4.18.1"
    }

    options.set_capability("sauce:options", sauce_options)

    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=options
    )

    yield driver
    driver.quit()
