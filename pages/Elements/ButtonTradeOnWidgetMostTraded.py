"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 15:30
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonUnderVideoBannerLocators
from selenium.common.exceptions import ElementClickInterceptedException


class ButtonTradeOnWidgetMostTraded(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if not self.button_trade_now_under_video_banner_is_visible():
            # pytest.fail("Checking element is not on this page")
            pytest.skip("Checking element is not on this page")

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def button_trade_now_under_video_banner_is_visible(self):
        print(f"{datetime.now()}   BUTTON_UNDER_VIDEO_BANNER =>")
        if self.element_is_visible(ButtonUnderVideoBannerLocators.BUTTON_UNDER_VIDEO_BANNER):
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS NOT PRESENT")
            return False

        # Act
    @allure.step("Click on button under video banner")
    def element_click(self):
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*ButtonUnderVideoBannerLocators.BUTTON_UNDER_VIDEO_BANNER)
        if len(button_list) == 0:
            del button_list
            return False

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print("'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser, "")
            page_.close_signup_form()
            button_list[0].click()
            del page_

        del button_list
        return True
