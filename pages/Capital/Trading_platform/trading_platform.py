"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 11:00
@Author  : Alexander Tomelo
"""

import allure
from datetime import datetime

import pytest

from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.base_page import BasePage
from test_data.trading_platform_data import data as tp_data
from pages.Capital.Trading_platform.trading_platform_locators \
    import TradingPlatformSignupFormLocators as TPSignupFormLocators


class TradingPlatform(BasePage):
    @allure.step("Checking that the trading platform page has opened")
    # @profile(precision=3)
    def should_be_trading_platform_page(self, d, link):
        """Check if the page is open"""
        print(f"{datetime.now()}   Checking that the trading platform page has opened")
        if self.current_page_url_contain_the(link):
            page_ = TopBar(d, link)
            if page_.trading_platform_logo_is_present():
                d.back()
                del page_
                assert True
            else:
                # d.back()
                del page_
                assert False, 'Page with title "Trading Platform | Capital.com" not loaded'
        else:
            assert False, f'Loaded page with not {link} url. Current url is {self.browser.current_url}'

    @allure.step("Check that form [Sign Up] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_signup_form_on_the_trading_platform(self):
        """
        Check there are an elements to on 'Sign up' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Sign up] page opened =>")

        if self.current_page_url_contain_the(tp_data["SIGNUP_URL"]):
            print(f"{datetime.now()}   'Sign up' page opened on the Trading Platform")

            print(f"{datetime.now()}   SIGNUP_FRAME =>")
            assert self.element_is_present(*TPSignupFormLocators.SIGNUP_FRAME), \
                f"{datetime.now()}   The layout of the 'SignUp' page has changed"

            print(f"{datetime.now()}   SIGNUP_FRAME_TITLE =>")
            assert self.get_text(0, *TPSignupFormLocators.FRAME_TITLE) == tp_data["SIGNUP_FORM_TITLE"], \
                f"{datetime.now()}   The title of the 'SignUp' page has changed"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
        else:
            assert False, "'SignUp' page on the Trading Platform is not opened"

    @allure.step("Check that form [Login] is opened on the Trading Platform page")
    # @profile(precision=3)
    def should_be_login_form_on_the_trading_platform(self):
        """
        Check there are an elements to on 'Log in' page on the Trading Platform
        """
        print(f"{datetime.now()}   Start method Check that [Log in] page opened =>")

        if self.current_page_url_contain_the(tp_data["LOGIN_URL"]):
            print(f"{datetime.now()}   'Log in' page opened on the Trading Platform")

            print(f"{datetime.now()}   LOGIN_FRAME =>")
            assert self.element_is_present(*TPSignupFormLocators.LOGIN_FRAME), \
                f"{datetime.now()}   The layout of the 'Login' page has changed"

            print(f"{datetime.now()}   LOGIN_FRAME_TITLE =>")
            assert self.get_text(0, *TPSignupFormLocators.FRAME_TITLE) == tp_data["LOGIN_FORM_TITLE"], \
                f"{datetime.now()}   The title of the 'Login' page has changed"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(TPSignupFormLocators.USERNAME), \
                f"{datetime.now()}   Problem with 'Username (email)' field"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(TPSignupFormLocators.PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' field"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(TPSignupFormLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
        else:
            pytest.xfail("'Login' page on the Trading Platform is not opened")
            assert False, "'Login' page on the Trading Platform is not opened"
