from selenium.webdriver.common.by import By


class LoginPageLocators:
    SIGN_IN_LINK = (By.XPATH, "//ytd-button-renderer[@class='style-scope ytd-masthead']//a[@aria-label='Sign in']//div[@class='yt-spec-touch-feedback-shape__fill']")
    EMAIL_TXTBX = (By.ID, "identifierId")
    NEXT_BTN = (By.XPATH, "//div[@id='identifierNext']")
    PASSWORD_TXTBX = (By.NAME, "Passwd")
    SUBMIT_NEXT_BTN= (By.XPATH,"//span[normalize-space()='Next']")
    ACCOUNT_LBL=(By.XPATH,"//yt-img-shadow[@class='style-scope ytd-topbar-menu-button-renderer no-transition']//img[@id='img']")
    LOGIN_SUCCESS_LBL=(By.XPATH,"//yt-formatted-string[@id='account-name']")
    LOGIN_UNSUCCESS_LBL=(By.XPATH,"//span[contains(text(),'Wrong password.')]")
    SHOW_PASS_CHKBTN=(By.XPATH,"//input[@type='checkbox']")
    PASSWORD_SUCCESS_VAL=(By.XPATH,"//input[@name='Passwd']")

