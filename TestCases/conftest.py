import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def username_password():
    username = "samsunnisha.multani@bridgingprograms.ca"
    password = "Saihsaif@786"
    password1="Saihsaif786"

    return [username, password,password1]


@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()
