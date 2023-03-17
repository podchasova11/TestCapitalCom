import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException
)
from datetime import datetime
from pages.base_page import BasePage
from pages.Signup_login.signup_login import SignupLogin
from pages.Header.header_locators import HeaderElementLocators
# from .src.src import HeaderSrc


class Header(BasePage):

    @allure.step("Check if the element is visible on this page")
    def header_button_login_is_visible(self):
        print(f"{datetime.now()}   Is visible BUTTON_LOGIN? =>")
        if self.element_is_visible(HeaderElementLocators.BUTTON_LOGIN):
            print(f"{datetime.now()}   => BUTTON_LOGIN is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not visible on the page!")
            return False

    @allure.step("Click 'Log In' button")
    def header_button_login_click(self):
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_LOGIN)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGIN is not present on the page!")
            return False

        print(f"{datetime.now()}   BUTTON_LOGIN is scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Login' form is auto opened")
            page_ = SignupLogin(self.browser)
            page_.close_login_form()
            button_list[0].click()

        return True

    @allure.step("Check if the element is visible on the page")
    def header_button_signup_is_visible(self):
        print(f"{datetime.now()}   Is visible BUTTON_SIGNUP? =>")
        if self.element_is_visible(HeaderElementLocators.BUTTON_SIGNUP):
            print(f"{datetime.now()}   => BUTTON_SIGNUP is visible on the page!")
            return True
        else:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not visible on the page!")
            return False

    @allure.step("Click 'Trade Now' button")
    def header_button_signup_click(self):
        print(f"{datetime.now()}   Is present BUTTON_SIGNUP? =>")
        button_list = self.browser.find_elements(*HeaderElementLocators.BUTTON_SIGNUP)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_SIGNUP is not present on the page!")
            return False
        print(f"{datetime.now()}   => BUTTON_SIGNUP is present on the page!")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        self.element_is_clickable(button_list[0], 5)

        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Sign up' form is auto opened")
            page_ = SignupLogin(self.browser)
            page_.close_signup_form()
            button_list[0].click()

        return True
