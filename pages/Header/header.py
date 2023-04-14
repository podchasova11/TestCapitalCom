"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import time

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException
)
from datetime import datetime
from pages.base_page import BasePage
# from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
from pages.My_account.my_account_locators import MyAccountLocator
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step("Click button [My account]")
    def header_button_my_account_click(self):
        print(f"{datetime.now()}   Start Click button [My account]:")

        print(f"{datetime.now()}   BUTTON_MY_ACCOUNT is present? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on this page!")
            del button_list
            return False
        print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is present on this page!")

        print(f"{datetime.now()}   BUTTON_MY_ACCOUNT is clickable? =>")
        if not self.element_is_clickable(button_list[0], 5):
            print("Button [My account] is not clicable!")

        print(f"{datetime.now()}   BUTTON_MY_ACCOUNT click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT clicked")
        except ElementNotInteractableException:
            print(f'{datetime.now()}   It\'s a problem! Button [My account] is not clicked! But, 1 second later ...')
            time.sleep(1)
            button_list[0].click()
            print(f"{datetime.now()}   => 1 second later BUTTON_MY_ACCOUNT clicked")
        except ElementClickInterceptedException:
            print(f'{datetime.now()}   It\'s a problem! Button [My account] is not clicked!')
            time.sleep(1)
            print(f"{datetime.now()}   => 1 second later BUTTON_MY_ACCOUNT clicked")
            button_list[0].click()

        if not self.element_is_visible(MyAccountLocator.USER_LOGIN, 5):
            print(f"{datetime.now()}   => User panel [My account] not opened")
            print(f"{datetime.now()}   BUTTON_MY_ACCOUNT click again =>")
            button_list[0].click()

        if not self.element_is_visible(MyAccountLocator.USER_LOGIN, 5):
            print(f"{datetime.now()}   => User panel [My account] not opened")
            print(f"{datetime.now()}   BUTTON_MY_ACCOUNT click again =>")
            button_list[0].click()

        del button_list
        return True
