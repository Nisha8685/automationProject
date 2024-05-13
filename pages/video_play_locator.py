from selenium.webdriver.common.by import By


class VideoPlayLocators:
    SEARCH_TXTBX = (By.XPATH,"//input[@id='search']")
    SEARCH_BTN = (By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']//div")
    SELECT_LINK= (By.XPATH,"//yt-formatted-string[normalize-space()='Git and GitHub Tutorial for Beginners']")
    PLAY_BTN=(By.XPATH,"//button[@title='Play (k)']")
    SHOW_CAPTION_BTN=(By.XPATH,"//button[@title='Subtitles/closed captions (c)']")
    VIDEO_PLAY_SUCCESS_LBL=(By.XPATH,"//yt-formatted-string[@class='style-scope ytd-watch-metadata'][normalize-space()='Git and GitHub Tutorial for Beginners']")

