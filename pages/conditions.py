import allure
# import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.Header.header import Header
from pages.My_account.my_account import MyAccount
from pages.Capital.Trading.Platform.Topbar.topbar import TopBar
from pages.Signup_login.signup_login_locators import (
    # SignupFormLocators,
    LoginFormLocators,
)

flag_cookies = False
url_language = "?"
url_license = "?"
test_link = "?"
prev_role = "?"
prev_license = "?"
prev_language = "?"


class Conditions(BasePage):
    """This class used as a base class for other page classes that represent specific pages on a website"""

    @allure.step("Set preconditions")
    def preconditions(self, d, host, end_point, login, password, cur_role, cur_language, cur_license):

        global flag_cookies
        global url_language
        global url_license
        global test_link
        global prev_language
        global prev_license
        global prev_role

        print(d.get_window_size())

        # Настраиваем в соответствии с параметром "Роль"
        if cur_role != prev_role:
            self.browser = d
            self.link = host
            self.open_page()
            print("\nBefore deleting cookies:")
            print(d.get_cookies(), "")
            d.delete_all_cookies()
            print("\nAfter deleting cookies:")
            print(d.get_cookies(), "")
            self.open_page()
            self.button_accept_all_cookies_click()

            print(f"\n{datetime.now()}   "
                  f'Run preconditions: set "{cur_role}" role')

            if cur_role == "Reg/NoAuth":
                # self.to_do_registration(d, login, password)
                self.to_do_authorization(d, host, login, password)
                self.to_do_deauthorization(d, host)

            if cur_role == "Auth":
                # self.to_do_registration(d, login, password)
                self.to_do_authorization(d, host, login, password)

            prev_role = cur_role
            prev_language = "?"
            prev_license = "?"

        # устанавливаем Язык, если не соответствует предыдущему
        if cur_language != prev_language:
            if cur_language != "":
                url_language = f"{host}/{cur_language}{end_point}"
            elif cur_language == "":
                url_language = f"{host}{end_point}"
            print(f"\n"
                  f"{datetime.now()}   "
                  f'Run preconditions: set "{cur_language}" language. Bild url_language = {url_language}')
            test_link = url_language
            self.browser = d
            self.link = url_language
            self.open_page()
            prev_language = cur_language

        if cur_license != prev_license:
            if cur_language != "":
                url_license = f"{host}/{cur_language}{end_point}/?license={cur_license}"
            elif cur_language == "":
                url_license = f"{host}{end_point}/?license={cur_license}"
            print(f"\n"
                  f"{datetime.now()}   "
                  f'Run preconditions: set "{cur_license}" license. Bild url_license = {url_license}')
            self.browser = d
            self.link = url_license
            self.open_page()
            prev_license = cur_license

        return test_link

    # регистрация пользователя
    # @allure.step("Registration")
    def to_do_registration(self, d, login, password):
        """Register user on the login page.

        Args:
            d: web_driver
            login: username user
            password: password user
        """
        assert login != "", "Регистрация невозможна. Не указан e-mail"
        assert password != "", "Регистрация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        # page = HeaderElement(d, test_link)
        # page.open_page()
        page = Header(d, test_link)
        page.header_button_login_click()
        # проверить, открылась ли форма "Log in"
        # перейти на форму "Signup", нажав кнопку "SignUp"
        # проверить, открылась ли форма "SignUp"
        # ввести логин, вести пароль, нажать подтвердить

    # авторизация пользователя
    @allure.step("Autorization")
    def to_do_authorization(self, d, link, login, password):

        print(f"\n"
              f"{datetime.now()}   Start Autorization")
        # Setup wait for later
        wait = WebDriverWait(d, 15)

        assert login != "", "Авторизация невозможна. Не указан e-mail"
        assert password != "", "Авторизация невозможна. Не указан пароль"
        # нажать в хедере на кнопку "Log in"
        page_ = Header(d, link)
        page_.header_button_login_click()
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

        d.back()

    @allure.step("Deautorization")
    def to_do_deauthorization(self, d, link):

        print(f"\n"
              f"{datetime.now()}   Start Deautorization")

        assert Header(d, link).header_button_my_account_click(), "Button [My account] missing"
        assert MyAccount(d, link).my_account_button_logout_click(), "Button [Logout] missing"
