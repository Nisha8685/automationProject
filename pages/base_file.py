from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def explicitly_wait_and_find_element(self, interval, locator):
        return WebDriverWait(self.driver, interval).until(
            expected_conditions.presence_of_element_located(locator))

    def navigate_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window()


    def find_element(self, locator):
        return self.driver.find_element(*locator)


    def scroll_element(self):
        self.driver.execute_script("scrollBy(0,500)")


    def explicity_wait_till_clickable(self,interval,locator):
        return WebDriverWait(self.driver,interval).until(
        expected_conditions.element_to_be_clickable(locator))


