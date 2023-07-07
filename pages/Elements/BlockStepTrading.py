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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class BlockStepTrading(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_CREATE_YOUR_ACCOUNT? =>")
        # if self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
        try:
            if self.browser.find_element(*BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT):
                print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is present on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not present on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click '1. Create your account' button in 'Three first steps' section")
    def element_click(self):
        """Method"""
        print(f"\n{datetime.now()}   2. Act")
        button_list = self.browser.find_elements(*BlockStepTradingLocators.BUT_CREATE_YOUR_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not present on the page!")
            del button_list
            pytest.fail("Checking element is not on this page")
        print(f"{datetime.now()}   "
              f"{len(button_list)} checking element(s) with current CSS locator is(are) present(s) on this page")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )
        if not self.element_is_clickable(button_list[0], 5):
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is not clickable")

        try:
            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT is clicked")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => BUTTON_CREATE_YOUR_ACCOUNT NOT CLICKED")
            print("'Sign up' form or page is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_page()

            # button_list[0].click()
            self.browser.execute_script("arguments[0].click();", button_list[0])
            del page_

        del button_list
        return True
