import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    username = "samsunnisha.multani@bridgingprograms.ca"
    password = "Abcd@123_456"
    wrong_password= "Abcd@786"

    return [username, password, wrong_password]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
