import pytest

from tests.helpers.selenium_utils import SeleniumUtils


@pytest.fixture(scope="session", autouse=True)
def selenium():
    selenium_utils = SeleniumUtils()
    url = 'http://localhost:8000'
    selenium_utils.driver.get(url)
    yield selenium_utils


class TestHappyPath:

    def test_public_access(self, selenium):
        center_panel = selenium.get_element_by_id("centerPanel")
        assert center_panel.text == "Welcome to Prowessive"
