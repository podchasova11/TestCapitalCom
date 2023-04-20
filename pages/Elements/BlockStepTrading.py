"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 08:30
@Author  : Alexander Tomelo
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import BlockStepTradingLocators
from selenium.common.exceptions import ElementClickInterceptedException


class BlockStepTrading(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        if not self.button_create_your_account_is_visible():
            # pytest.fail("Checking element is not on this page")
            pytest.skip("Checking element is not on this page")

    @allure.step("Check if the element is present on the page")
    # @profile(precision=3)
    def button_create_your_account_is_visible(self):
        print(f"{datetime.now()}   BUTTON_CREATE_YOUR_ACCOUNT =>")
        if self.element_is_visible(BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT):
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT IS PRESENT")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT IS NOT PRESENT")
            return False

        # Act
    @allure.step("Click '1. Create your account' button in 'Three first steps' section")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT)
        if len(button_list) == 0:
            del button_list
            return False
        print(f"{datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        self.element_is_clickable(button_list[0], 5)
        try:
            print(f"{datetime.now()}   Click BUTTON_CREATE_YOUR_ACCOUNT =>")
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser, "")
            print(f"{datetime.now()}   Close 'Sign up' form =>")
            if page_.close_signup_form():
                print(f"{datetime.now()}   => 'Sign up' form closed")
            else:
                print(f"{datetime.now()}   => 'Sign up' page is auto opened")
                page_.close_signup_page()
                print(f"{datetime.now()}   => 'Sign up' page closed")

            print(f"{datetime.now()}   Click BUTTON_CREATE_YOUR_ACCOUNT =>")
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")
            del page_

        del button_list
        return True
