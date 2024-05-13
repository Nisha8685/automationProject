import time

from pages.base_file import BasePage
from pages.video_page_locator import VideoPageLocators
from resources.config import MAX_WAIT_INTERVAL


class VideoPage(BasePage):

    def click_on_create_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPageLocators.CREATE_BTN)
        self.find_element(VideoPageLocators.CREATE_BTN).click()
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, VideoPageLocators.UPLOAD_VIDEO_BTN)
        self.find_element(VideoPageLocators.UPLOAD_VIDEO_BTN).click()




    def upload_video(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPageLocators.SELECT_FILES_BTN)
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPageLocators.SELECT_FILES_BTN).send_keys("/home/samsunnishamultani/Downloads/trial.mp4")
        title= self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPageLocators.TITLE_TXTBX)
        title.clear()
        title.send_keys("My Son preparing for his speech for the science project")

        time.sleep(3)
        self.find_element(VideoPageLocators.DESC_TXTBX).send_keys("Science Project")
        time.sleep(3)
        self.find_element(VideoPageLocators.RADIO1_BTN).click()
        time.sleep(3)
        self.find_element(VideoPageLocators.NEXT1_BTN).click()
        time.sleep(3)
        self.find_element(VideoPageLocators.NEXT2_BTN).click()
        time.sleep(3)
        self.find_element(VideoPageLocators.NEXT3_BTN).click()
        time.sleep(3)
        self.find_element(VideoPageLocators.RADIO2_BTN).click()
        time.sleep(3)
        self.find_element(VideoPageLocators.SAVE_BTN).click()
        time.sleep(3)


        #Assert method
    def get_video_success_lbl(self):
        return self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPageLocators.VIDEO_SUCCESS_LBL).text











