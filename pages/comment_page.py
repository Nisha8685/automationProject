import time

from pages.base_file import BasePage
from pages.comment_page_locator import CommentPageLocators
from resources.config import MAX_WAIT_INTERVAL


class CommentPage(BasePage):

    def comment_click(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,CommentPageLocators.COMMENT_TXTBX)
        time.sleep(5)
        self.find_element(CommentPageLocators.COMMENT_TXTBX).send_keys("This is a very helpfull video")
        self.find_element(CommentPageLocators.COMMENT_TXTBX).send_keys(KEYS.ENTER)
        time.sleep(10)
        self.find_element(CommentPageLocators.COMMENT_BTN).click()
