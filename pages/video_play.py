import time

from pages.base_file import BasePage
from pages.video_play_locator import VideoPlayLocators
from resources.config import MAX_WAIT_INTERVAL


class VideoPlay(BasePage):

    def click_on_search_btn(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,VideoPlayLocators.SEARCH_TXTBX)
        self.find_element(VideoPlayLocators.SEARCH_TXTBX).send_keys("git and github full tutorial")

    def search_video(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, VideoPlayLocators.SEARCH_BTN)
        self.find_element(VideoPlayLocators.SEARCH_BTN).click()
        time.sleep(5)
        self.find_element(VideoPlayLocators.SELECT_LINK).click()
        time.sleep(6)
        self.find_element(VideoPlayLocators.SHOW_CAPTION_BTN).click()


    def get_video_play_success_lbl(self):
        return self.find_element(VideoPlayLocators.VIDEO_PLAY_SUCCESS_LBL).text






