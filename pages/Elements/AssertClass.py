"""
-*- coding: utf-8 -*-
@Time    : 2023/03/28 09:00
@Author  : Alexander Tomelo
"""

import pytest
import allure
from datetime import datetime
from pages.Capital.Trading_platform.trading_platform import TradingPlatform
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin


class AssertClass(BasePage):
    page_signup_login = None
    page_trading = None
    platform_url = ""

    @allure.step('Checking that "Signup" form or page opened')
    def assert_signup(self, d, cur_language, cur_role, cur_link):
        """Method Assert Signup form or page"""
        print(f"\n{datetime.now()}   3. Assert")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_signup_form(cur_language):
            self.page_signup_login.close_signup_form()
        elif self.page_signup_login.should_be_signup_page(cur_language):
            self.page_signup_login.close_signup_page()
        else:
            del self.page_signup_login
            pytest.fail("Unknown registration method")
        # time.sleep(2)
        del self.page_signup_login

    @allure.step('Checking that "Login" form or page opened')
    def assert_login(self, d, cur_link):
        """Method Assert Login form or page"""
        print(f"\n{datetime.now()}   3. Assert")
        print(f"\n{datetime.now()}   self = {self}")
        self.page_signup_login = SignupLogin(d, cur_link)
        if self.page_signup_login.should_be_login_form():
            self.page_signup_login.close_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_login_page():
            self.page_signup_login.close_login_page()
            del self.page_signup_login
        else:
            del self.page_signup_login
            pytest.fail("Unknown authorization method")

    @allure.step('Checking that "Trading platform" page opened')
    def assert_trading_platform(self, d):
        print(f"\n{datetime.now()}   3. Assert")
        self.platform_url = "https://capital.com/trading/platform"
        self.page_trading = TradingPlatform(d)
        self.page_trading.should_be_trading_platform_page(d, self.platform_url)
        del self.page_trading
