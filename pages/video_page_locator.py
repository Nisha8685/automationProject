from selenium.webdriver.common.by import By


class VideoPageLocators:

    CREATE_BTN= (By.XPATH,"//yt-icon[@class='style-scope ytd-topbar-menu-button-renderer']//div")
    UPLOAD_VIDEO_BTN= (By.XPATH,"(//yt-formatted-string[@id='label'])[1]")
    SELECT_FILES_BTN=(By.XPATH,"//input[@type='file']")
    TITLE_TXTBX=(By.XPATH,"//ytcp-social-suggestions-textbox[@id='title-textarea']//div[@id='textbox']")
    DESC_TXTBX=(By.XPATH,"//ytcp-social-suggestions-textbox[@id='description-textarea']//div[@id='textbox']")
    RADIO1_BTN=(By.XPATH,"(//div[@id='radioLabel'])[1]")
    NEXT1_BTN=(By.XPATH,"//ytcp-button[@id='next-button']")
    NEXT2_BTN=(By.XPATH,"//div[normalize-space()='Next']")
    NEXT3_BTN = (By.XPATH,"//div[normalize-space()='Next']")
    RADIO2_BTN =(By.XPATH,"(//div[@id='offRadio'])[1]")
    SAVE_BTN= (By.XPATH,"//div[normalize-space()='Save']")
    VIDEO_SUCCESS_LBL= (By.XPATH,"//span[normalize-space()='My Son preparing for his speech for the science project']")

