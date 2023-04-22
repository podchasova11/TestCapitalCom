"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
# import time
# from memory_profiler import profile
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.Header.header import Header
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.My_account.my_account import MyAccount
from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.Signup_login.signup_login_locators import (
    # SignupFormLocators,
    LoginFormLocators,
)

flag_cookies = False
url_language = "?"
url_country = "?"
test_link = "?"
prev_language = "?"
prev_country = "?"
prev_role = "?"


class Conditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    @allure.step("Set preconditions")
    # @profile(precision=3)
    def preconditions(self, d, host, end_point, cur_language, cur_country, cur_role, cur_login, cur_password):
        """
        Method Precondition
        """
        global flag_cookies
        global url_language
        global url_country
        global test_link
        global prev_language
        global prev_country
        global prev_role

        print(f"\n{datetime.now()}   {d.get_window_size()}")
        d.set_window_size(1920, 1080)
        # d.set_window_position(0, 0)
        print(f"\n{datetime.now()}   {d.get_window_size()}")

        # Настраиваем в соответствии с параметром "Роль"
        print(f"\n{datetime.now()}   Prev. Role: {prev_role}")
        if cur_role != prev_role:
            print(f"\n{datetime.now()}   "
                  f'Run preconditions: set "{cur_role}" Role =>')

            self.browser = d
            self.link = host
            self.open_page()
            print(f"\n{datetime.now()}   Before deleting cookies:")
            print(d.get_cookies(), "")
            d.delete_all_cookies()
            print(f"\n{datetime.now()}   After deleting cookies:")
            print(d.get_cookies(), "")
            self.open_page()

            if not flag_cookies:
                self.button_accept_all_cookies_click()
                flag_cookies = True

            match cur_role:
                case "Reg/NoAuth":
                    # self.to_do_registration(d, login, password)
                    self.to_do_authorisation(d, host, cur_login, cur_password)
                    self.to_do_de_authorisation(d, host)
                case "Auth":
                    # self.to_do_registration(d, login, password)
                    self.to_do_authorisation(d, host, cur_login, cur_password)

            prev_role = cur_role
            prev_language = "?"
            prev_country = "?"

        print(f"\n{datetime.now()}   Current role: {cur_role}")

        # устанавливаем Язык, если не соответствует предыдущему
        print(f"\n{datetime.now()}   Prev language: {prev_language}")
        language = cur_language
        if language == "":
            language = "en"
        if cur_language != prev_language:
            print(f"\n{datetime.now()}   "
                  f'Run preconditions: set "{language}" language =>')

            if cur_language != "":
                url_language = f"{host}/{cur_language}{end_point}"
            elif cur_language == "":
                url_language = f"{host}{end_point}"
            print(f"\n"
                  f"{datetime.now()}   Bild url_language = {url_language}")
            test_link = url_language
            self.browser = d
            self.link = url_language
            self.open_page()
            prev_language = cur_language

        print(f"\n{datetime.now()}   Current language: {language}")

        print(f"\n{datetime.now()}   Prev country: {prev_country}")
        if cur_country != prev_country:
            print(f"\n{datetime.now()}   "
                  f'Run preconditions: set "{cur_country}" country')

            if cur_language != "":
                url_country = f"{host}/{cur_language}{end_point}/?country={cur_country}"
            elif cur_language == "":
                url_country = f"{host}{end_point}/?country={cur_country}"
            print(f"\n"
                  f"{datetime.now()}   Bild url_country = {url_country}")
            test_link = url_language
            self.browser = d
            self.link = url_country
            self.open_page()
            prev_country = cur_country

        print(f"\n{datetime.now()}   Current country: {cur_country}")
        return test_link

    # регистрация пользователя
    # @allure.step("Registration")
    # def to_do_registration(self, d, login, password):
    #     """Register user on the login page.
    #
    #     Args:
    #         d: web_driver
    #         login: username user
    #         password: password user
    #     """
    #     assert login != "", "Регистрация невозможна. Не указан e-mail"
    #     assert password != "", "Регистрация невозможна. Не указан пароль"
    #     # нажать в хедере на кнопку "Log in"
    #     # page = HeaderElement(d, test_link)
    #     # page.open_page()
    #     page = Header(d, test_link)
    #     page.header_button_login_click()
    #     # проверить, открылась ли форма "Log in"
    #     # перейти на форму "Signup", нажав кнопку "SignUp"
    #     # проверить, открылась ли форма "SignUp"
    #     # ввести логин, вести пароль, нажать подтвердить

    # авторизация пользователя
    @allure.step("Authorisation")
    # @profile(precision=3)
    def to_do_authorisation(self, d, link, login, password):
        """Authorisation"""
        print(f"\n"
              f"{datetime.now()}   Start Autorization")
        # Setup wait for later
        wait = WebDriverWait(d, 15)

        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        page_ = HeaderButtonLogin(d, link)
        page_.element_click()
        print(f"{datetime.now()}   => 'Login' form opened")

        # User's name is passed to the text element on the login page
        page_.send_keys(login, *LoginFormLocators.LOGIN_INPUT_EMAIL)
        # Password is passed to the text element on the login page
        page_.send_keys(password, *LoginFormLocators.LOGIN_INPUT_PASSWORD)

        print(f"{datetime.now()}   Click button [Continue] on form [Login]")
        page_.click_button(*LoginFormLocators.LOGIN_CONTINUE)
        # time.sleep(2)

        # Wait for the new tab to finish loading content
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        platform_url = "https://capital.com/trading/platform/"
        print(f"{datetime.now()}   -> Page with 'Trading Platform | Capital.com' title opened")

        page_ = TopBar(d, platform_url)
        if page_.trading_platform_logo_is_present():
            print(f'{datetime.now()}   -> "Capital.com" logo is present on trading platform page)')
        else:
            print(f'{datetime.now()}   -> "Capital.com" logo mission')
        del page_
        d.back()

    @allure.step('DeAuthorisation')
    # @profile(precision=3)
    def to_do_de_authorisation(self, d, link):
        """DeAuthorisation"""
        print(f"\n"
              f"{datetime.now()}   Start DeAuthorisation")

        assert Header(d, link).header_button_my_account_click(), "Button 'My account' missing"
        assert MyAccount(d, link).my_account_button_logout_click(), "Button 'Logout' missing"
