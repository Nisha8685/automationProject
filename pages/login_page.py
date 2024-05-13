import time

from pages.base_file import BasePage
from pages.login_page_locator import LoginPageLocators
from resources.config import MAX_WAIT_INTERVAL


class LoginPage(BasePage):

    def click_on_sign_in_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginPageLocators.SIGN_IN_LINK).click()



    def login_username(self,username):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,LoginPageLocators.EMAIL_TXTBX)
        self.find_element(LoginPageLocators.EMAIL_TXTBX).send_keys(username)

    def click_on_next_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.NEXT_BTN).click()


    def login_userpassword(self, password):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.PASSWORD_TXTBX)
            self.find_element(LoginPageLocators.PASSWORD_TXTBX).send_keys(password)


    def click_on_submit_next_btn(self):
            self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.SUBMIT_NEXT_BTN).click()



    # For assertion of Test Case 1
    def click_on_account_lbl(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.ACCOUNT_LBL)
        self.find_element(LoginPageLocators.ACCOUNT_LBL).click()


    def get_login_success_label(self):

        return self.find_element(LoginPageLocators.LOGIN_SUCCESS_LBL).text

    # For assertion of Test Case 2

    def get_login_unsuccess_label(self):
        return self.find_element(LoginPageLocators.LOGIN_UNSUCCESS_LBL).text


    def click_on_showpassword_chkbtn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.SHOW_PASS_CHKBTN).click()

    # For assertion of Test Case 3

    def get_password_success_label(self):
        return self.find_element(LoginPageLocators.PASSWORD_SUCCESS_VAL).get_attribute("value")

