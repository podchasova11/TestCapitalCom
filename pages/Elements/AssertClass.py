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
    page_glossary = None
    platform_url = ""

<<<<<<< HEAD
    def assert_signup(self, d, cur_language, cur_role, cur_link):
=======
    def assert_signup(self, d, cur_language, cur_role, cur_item_link):
>>>>>>> master

        print(f"\n{datetime.now()}   3. Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
<<<<<<< HEAD
                self.page_signup_login = SignupLogin(d, cur_link)
=======
                self.page_signup_login = SignupLogin(d, cur_item_link)
>>>>>>> master
                if self.page_signup_login.should_be_signup_form(cur_language):
                    self.page_signup_login.close_signup_form()
                elif self.page_signup_login.should_be_signup_page(cur_language):
                    self.page_signup_login.close_signup_page()
                else:
                    del self.page_signup_login
                    pytest.fail("Unknown registration method")
                del self.page_signup_login
            case "Auth":
                self.platform_url = "https://capital.com/trading/platform"
                self.page_glossary = TradingPlatform(d)
                self.page_glossary.should_be_trading_platform_page(d, self.platform_url)
                del self.page_glossary

<<<<<<< HEAD
    def assert_login(self, d, cur_link):
        """Method Assert"""
        print(f"\n{datetime.now()}   3. Assert")
        self.page_signup_login = SignupLogin(d, cur_link)
=======
    def assert_login(self, d, cur_item_link):
        """Method Assert"""
        print(f"\n{datetime.now()}   3. Assert")
        self.page_signup_login = SignupLogin(d, cur_item_link)
>>>>>>> master
        if self.page_signup_login.should_be_login_form():
            self.page_signup_login.close_login_form()
            del self.page_signup_login
        elif self.page_signup_login.should_be_login_page():
            self.page_signup_login.close_login_page()
            del self.page_signup_login
        else:
            del self.page_signup_login
            pytest.xfail("Unknown authorization method")
