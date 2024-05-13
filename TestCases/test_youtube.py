import time

import pytest

from resources.config import TEST_SITE_URL
from pages.login_page import LoginPage
from pages.video_page import VideoPage
from pages.video_play import VideoPlay
from pages.comment_page import CommentPage

class TestYouTube:
#Test Scienario1

    # Test Case 1 - Login the user with correct credentials
    @pytest.mark.group1
    @pytest.mark.group2
    def test_success_login_user(self, driver, username_password):
        login_page= LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.click_on_sign_in_btn()
        login_page.login_username(username_password[0])
        login_page.click_on_next_btn()
        login_page.login_userpassword(username_password[1])
        login_page.click_on_submit_next_btn()
        login_page.click_on_account_lbl()
        time.sleep(5)
        login_success_lbl= login_page.get_login_success_label()
        time.sleep(5)

        assert "Nisha Multani" == login_success_lbl,"Test1 Failed"


    #  Test Case 2 - Login the user with incorrect credentials
    def test_unsuccess_login_user(self,driver,username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.click_on_sign_in_btn()
        login_page.login_username(username_password[0])
        login_page.click_on_next_btn()
        login_page.login_userpassword(username_password[2])
        login_page.click_on_submit_next_btn()
        time.sleep(3)
        login_unsuccess_lbl = login_page.get_login_unsuccess_label()
        assert "Wrong password. Try again or click ‘Forgot password’ to reset it." == login_unsuccess_lbl, "Test2 Failed"

    # Test Case 3- Check working functionality of Show password button
    def test_show_password(self,driver,username_password):
        login_page = LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.click_on_sign_in_btn()
        login_page.login_username(username_password[0])
        login_page.click_on_next_btn()
        login_page.click_on_showpassword_chkbtn()
        login_page.login_userpassword(username_password[1])
        time.sleep(2)
        show_password_success_lbl = login_page.get_password_success_label()
        assert "Saihsaif@786" == show_password_success_lbl, "Test3 Failed"


    def test_password_recovery(self,driver,username_password):
        login_page=LoginPage(driver)
        login_page.navigate_to(TEST_SITE_URL)
        login_page.click_on_sign_in_btn()
        login_page.login_username(username_password[0])
        login_page.click_on_next_btn()
        login_page.forgot_password()





#Test Scenario2

    #Test Case 4 - Check working functionality of video upload facility
    @pytest.mark.group1
    def test_video_upload(self,driver):
        video_page= VideoPage(driver)
        video_page.click_on_create_btn()
        video_page.upload_video()
        video_success= video_page.get_video_success_lbl()
        assert "My Son preparing for his speech for the science project" == video_success, "Test4 Failed"


    #Test Case 5 - Check working functionality of video search and playback facility
    @pytest.mark.group2
    def test_video_play(self,driver):
        video_play=VideoPlay(driver)
        video_play.click_on_search_btn()
        video_play.search_video()
        video_play_success= video_play.get_video_play_success_lbl()
        assert "Git and GitHub Tutorial for Beginners" ==video_play_success, "Test5 Failed"


#Test Scenario3


    #Test Case 6 - Check working functionality of writing comment
    @pytest.mark.group2
    def test_write_comment(self,driver):

        comment_page= CommentPage(driver)
        comment_page.scroll_element()
        time.sleep(10)
        comment_page.comment_click()






