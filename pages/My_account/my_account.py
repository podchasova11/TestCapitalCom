import allure
from datetime import datetime
from pages.base_page import BasePage
from selenium.common.exceptions import (
    ElementClickInterceptedException
)
from pages.My_account.my_account_locators import MyAccountLocator


class MyAccount(BasePage):

    @allure.step("Click 'Logout' button")
    def my_account_button_logout_click(self):
        button_list = self.browser.find_elements(*MyAccountLocator.LOGOUT)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => BUTTON_LOGOUT is not present!")
            return False
        print(f"{datetime.now()}   => BUTTON_LOGOUT is present!")

        print(f"{datetime.now()}   BUTTON_LOGOUT is scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        print(f"{datetime.now()}   BUTTON_LOGOUT is clickable? =>")
        self.element_is_clickable(button_list[0], 5)
        print(f"{datetime.now()}   BUTTON_LOGOUT click =>")
        try:
            button_list[0].click()
        except ElementClickInterceptedException:
            print(f'{datetime.now()}   It\'s a problem! Button "Logout" are not clicked!')
            # page_ = SignupLogin(self.browser)
            # page_.close_login_form()
            # button_list[0].click()
        print(f"{datetime.now()}   => BUTTON_LOGOUT clicked")

        return True

    @allure.step(f"{datetime.now()}.   Click 'Trading Platform' button")
    def click_button_trading_platform(self):
        button = self.browser.find_element(*MyAccountLocator.TRADING_PLATFORM)
        self.element_is_clickable(button, 5)
        button.click()

    @allure.step(f"{datetime.now()}.   Click 'Close MyAccount panel'")
    def click_close_user_panel(self):
        button = self.browser.find_element(*MyAccountLocator.CLOSE)
        self.element_is_clickable(button, 5)
        button.click()
