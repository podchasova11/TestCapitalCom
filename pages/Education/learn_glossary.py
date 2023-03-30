"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
import datetime
# from memory_profiler import profile
from selenium.common.exceptions import (
    ElementClickInterceptedException
)
from pages.base_page import BasePage
from pages.Capital.Trading.Platform.Topbar.topbar import TopBar
from pages.Education.learn_glossary_locators import (
    ItemFinancialDictionary,
    WidgetStillLookingFor
)
from pages.Signup_login.signup_login import SignupLogin


class ItemPage(BasePage):

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def tc_05_03_video_banner_is_visible(self):
        print(f"{datetime.datetime.now()}   VIDEO_BANNER =>")
        if self.element_is_visible(ItemFinancialDictionary.VIDEO_BANNER):
            print(f"{datetime.datetime.now()}   => VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}   => VIDEO_BANNER IS NOT PRESENT")
            return False

    @allure.step("Click on video banner")
    # @profile(precision=3)
    def tc_05_03_video_in_frame_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.VIDEO_BANNER)
        if len(button_list) == 0:
            return False

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        
        self.element_is_clickable(button_list[0], 5)
        
        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print("'Sign up' or 'Log in' form is automatically opened")
            page_ = SignupLogin(self.browser, "")
            page_.close_signup_form()
            button_list[0].click()

        return True

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def tc_05_04_button_trade_now_under_video_banner_is_visible(self):
        print(f"{datetime.datetime.now()}   BUTTON_UNDER_VIDEO_BANNER =>")
        if self.element_is_visible(ItemFinancialDictionary.BUTTON_UNDER_VIDEO_BANNER):
            print(f"{datetime.datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}   => BUTTON_UNDER_VIDEO_BANNER IS NOT PRESENT")
            return False

    @allure.step("Click on button under video banner")
    # @profile(precision=3)
    def tc_05_04_button_trade_now_under_video_banner_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.BUTTON_UNDER_VIDEO_BANNER)
        if len(button_list) == 0:
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

        return True
    
    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def tc_05_05_vert_hor_banner_button_is_visible(self):
        print(f"{datetime.datetime.now()}   VER_HOR_BANNER_BUTTON =>")
        if self.element_is_visible(ItemFinancialDictionary.VER_HOR_BANNER_BUTTON):
            print(f"{datetime.datetime.now()}   => VER_HOR_BANNER_BUTTON IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}   => VER_HOR_BANNER_BUTTON IS NOT PRESENT")
            return False

    @allure.step("Click button on vertical or horizontal banner")
    # @profile(precision=3)
    def tc_05_05_vert_hor_banner_button_click(self):
        button_list = self.browser.find_elements(*ItemFinancialDictionary.VER_HOR_BANNER_BUTTON)
        
        if len(button_list) == 0:
            return False

        print(f"{datetime.datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 3)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f"{datetime.datetime.now()}   'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser)
            page_.close_signup_form()
            button_list[0].click()

        return True

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def tc_05_06_button_create_your_account_is_visible(self):
        print(f"{datetime.datetime.now()}   BUT_CREATE_YOUR_ACCOUNT =>")
        if self.element_is_visible(WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT):
            print(f"{datetime.datetime.now()}   => BUT_CREATE_YOUR_ACCOUNT IS PRESENT")
            return True
        else:
            print(f"{datetime.datetime.now()}   => BUT_CREATE_YOUR_ACCOUNT IS NOT PRESENT")
            return False

    @allure.step("Click '1. Create your account' button in 'Three first steps' section")
    # @profile(precision=3)
    def tc_05_06_button_create_your_account_click(self):
        """Method"""
        button_list = self.browser.find_elements(*WidgetStillLookingFor.BUT_CREATE_YOUR_ACCOUNT)
        if len(button_list) == 0:
            return False
        print(f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
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
        return True

    @allure.step("Checking that the trading platform page has opened")
    # @profile(precision=3)
    def should_be_trading_platform_page(self, d):
        """Check if the page is open"""
        page_ = TopBar(self.browser)
        if page_.trading_platform_logo_is_present():
            d.back()
            assert True
        else:
            d.back()
            assert False, 'Page with title "Trading Platform | Capital.com" not loaded'
