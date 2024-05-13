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
    FORGOT_PASSWORD_LINK= (By.XPATH,"//span[normalize-space()='Forgot password?']")
    VERIFICATION_LINK=(By.CSS_SELECTOR,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > c-wiz:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > span:nth-child(1) > section:nth-child(2) > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(2)")
    ANOTHER_LINK=(By.XPATH,"(//span[normalize-space()='Try another way'])[1]")
    UPDATE_PASSWORD_LINK=(By.XPATH,"//span[normalize-space()='Update password']")
    CREATE_PASSWORD_TXTBX=(By.XPATH,"//input[@name='Passwd']")
    CONFIRM_PASSWORD_TXTBX=(By.XPATH,"//input[@name='ConfirmPasswd']")
    SAVE_PASSWORD_LINK=(By.XPATH,"//span[normalize-space()='Save password']")
    CHANGE_PASSWORD_LINK=(By.XPATH,"(//span[@class='RveJvd snByac'][normalize-space()='Change password'])[2]")

