import time

import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException
)
from datetime import datetime
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
from pages.My_account.my_account_locators import MyAccountLocator
# from .src.src import HeaderSrc


class Header(BasePage):

    def header_button_login_is_visible(self):
        print(f"{datetime.now()}   Is visible BUTTON_LOGIN? =>")
        if self.element_is_visible(HeaderElementLocators.BUTTON_LOGIN):
            print(f"{datetime.now()}   => BUTTON_LOGIN is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not visible on the page!")
            return False

    @allure.step("Click button [Log In]")
    def header_button_login_click(self):
        print(f"{datetime.now()}   Start Click button [Log in] =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_LOGIN)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not present on the page!")
            return False

        print(f"{datetime.now()}   BUTTON_LOGIN scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_LOGIN is clickable? =>")
        self.element_is_clickable(button_list[0], 5)

        print(f"{datetime.now()}   BUTTON_LOGIN click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_LOGIN clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
            page_ = SignupLogin(self.browser)
            page_.close_login_form()
            button_list[0].click()

        return True

    def header_button_signup_is_visible(self):
        print(f"{datetime.now()}   BUTTON_SIGNUP is visible? =>")
        if self.element_is_visible(HeaderElementLocators.BUTTON_SIGNUP):
            print(f"{datetime.now()}   => BUTTON_SIGNUP is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not visible on the page!")
            return False

    @allure.step("Click button [Trade Now]")
    def header_button_signup_click(self):
        print(f"{datetime.now()}   BUTTON_SIGNUP is present? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_SIGNUP)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not present on the page!")
            return False
        print(f"{datetime.now()}   => BUTTON_SIGNUP is present on the page!")

        print(f"{datetime.now()}   BUTTON_SIGNUP scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_SIGNUP is clickable? =>")
        self.element_is_clickable(button_list[0], 5)

        print(f"{datetime.now()}   BUTTON_SIGNUP click =>")
        try:
            button_list[0].click()
            print(f"{datetime.now()}   => BUTTON_SIGNUP clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => 'Sign up' or 'Log in' form is automatically opened")
            page_ = SignupLogin(self.browser)
            page_.close_signup_form()
            button_list[0].click()

        return True

    @allure.step("Click button [My account]")
    def header_button_my_account_click(self):
        print(f"\n"
              f"{datetime.now()}   Start Click button [My account]:")

        print(f"{datetime.now()}   BUTTON_MY_ACCOUNT is present? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_MY_ACCOUNT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_MY_ACCOUNT is not present on this page!")
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

        return True
