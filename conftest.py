import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def app():
    browser.config.base_url = "https://demoqa.com"
    yield browser
    browser.quit()
