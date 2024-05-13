from selenium.webdriver.common.by import By


class CommentPageLocators:
    COMMENT_TXTBX = (By.XPATH,"(//div[@id='contenteditable-root'])[1]")
    COMMENT_BTN = (By.XPATH, "//div[@class='yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--down yt-spec-touch-feedback-shape--touch-response-inverse']//div[@class='yt-spec-touch-feedback-shape__fill']")