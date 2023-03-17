import time

import allure
from datetime import datetime
from pages.base_page import BasePage
from pages.Signup_login.signup_login_locators import (
    SignupFormLocators,
    LoginFormLocators,
    LoginPageLocators,
    SignupPageLocators
)


class SignupLogin(BasePage):

    @allure.step("Check that the 'Sign up' form is open.")
    def should_be_signup_form(self, cur_language):
        """
        Check there are an elements to on Sign up form
        """
        if self.element_is_visible(SignupFormLocators.SIGNUP_FRAME):
            print(f"{datetime.now()}   'Sign up' form is opened")

            print(f"{datetime.now()}   SIGNUP_HEADER =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_HEADER), \
                f"{datetime.now()}   The layout of the 'SignUp' form has changed"
            
            print(f"{datetime.now()}   SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_REF_LOGIN), \
                f"{datetime.now()}   Problem with 'Login' reference"

            print(f"{datetime.now()}   SIGNUP_INPUT_EMAIL =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_EMAIL), \
                f"{datetime.now()}   Problem with 'E-mail' fild"

            print(f"{datetime.now()}   SIGNUP_INPUT_PASSWORD =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_INPUT_PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' fild"

            print(f"{datetime.now()}   SIGNUP_SUBMIT_BTN =>")
            assert self.element_is_visible(SignupFormLocators.SIGNUP_SUBMIT_BTN), \
                f"{datetime.now()}   Problem with 'Continue' button"

            print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_2):
                
                print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(SignupFormLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    assert False, \
                        f"{datetime.now()}   Problem with 'Privacy policy' reference on '{cur_language}' language!"

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            return True
        else:
            print(f"{datetime.now()}   'Sign up' form is not opened")
            return False

    @allure.step("Close the 'Sign up' form.")
    def close_signup_form(self):
        self.element_is_clickable(SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM, 5)
        self.browser.find_element(*SignupFormLocators.BUTTON_CLOSE_ON_SIGNUP_FORM).click()
        print(f"{datetime.now()}.   'Sign up' form is closed")

    @allure.step("Check that the 'Sign up' page is open.")
    def should_be_signup_page(self, cur_language):
        """
        Check there are an elements to on 'Sign up' page
        """
        time.sleep(2)
        if self.current_page_is("https://capital.com/trading/signup"):
            print(f"{datetime.now()}   'Sign up' page is opened")

            print(f"{datetime.now()}   SIGNUP_SIGNUP_FORM =>")
            assert self.element_is_present(*SignupPageLocators.SIGNUP_FORM), \
                f"{datetime.now()}   The layout of the 'SignUp' page has changed"

            print(f"{datetime.now()}   SIGNUP_REF_LOGIN =>")
            assert self.element_is_visible(SignupPageLocators.REF_LOGIN), \
                f"{datetime.now()}   Problem with 'Login' reference"

            print(f"{datetime.now()}   INPUT_EMAIL =>")
            assert self.element_is_visible(SignupPageLocators.INPUT_EMAIL), \
                f"{datetime.now()}   Problem with 'E-mail' fild"

            print(f"{datetime.now()}   INPUT_PASS =>")
            assert self.element_is_visible(SignupPageLocators.INPUT_PASS), \
                f"{datetime.now()}   Problem with 'Password' fild"

            print(f"{datetime.now()}   BUTTON_CONTINUE =>")
            assert self.element_is_visible(SignupPageLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"

            print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_2 =>")
            if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_2):

                print(f"{datetime.now()}   SIGNUP_PRIVACY_POLICY_ALL_1 =>")
                if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_ALL_1):
                    # if not self.element_is_visible(SignupPageLocators.SIGNUP_PRIVACY_POLICY_DE_1):
                    #     print(f"{datetime.now()}   SIGNUP_REF_LOGIN")
                    #
                    assert False, \
                        f"{datetime.now()}   Problem with 'Privacy policy' reference on '{cur_language}' language!"

            print(f"{datetime.now()}   => SIGNUP_PRIVACY_POLICY_ALL")

            return True
        else:
            print(f"{datetime.now()}   'Sign up' page is not opened")
            return False

    @allure.step("Close the 'Sign up' page.")
    def close_signup_page(self):
        self.browser.back()
        print("'Sign up' page is closed")

    @allure.step("Check that the 'Login' form is open.")
    def should_be_login_form(self):
        """
        Check there are an elements to on Login form
        """
        if self.element_is_visible(LoginFormLocators.LOGIN_FRAME):
            print(f"{datetime.now()}   'Login' form is opened")
            assert self.element_is_visible(LoginFormLocators.LOGIN_HEADER), \
                f"{datetime.now()}   The layout of the 'Login' form has changed"
            assert self.element_is_visible(LoginFormLocators.LOGIN_REF_SIGNUP), \
                f"{datetime.now()}   Problem with 'Sign up' reference"
            assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_EMAIL), \
                f"{datetime.now()}   Problem with 'Email address' fild"
            assert self.element_is_visible(LoginFormLocators.LOGIN_INPUT_PASSWORD), \
                f"{datetime.now()}   Problem with 'Password' fild"
            assert self.element_is_visible(LoginFormLocators.LOGIN_CHECKBOX), \
                f"{datetime.now()}   Problem with 'Log me out after 7 days' check box"
            assert self.element_is_visible(LoginFormLocators.LOGIN_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            assert self.element_is_visible(LoginFormLocators.LOGIN_PASS_FORGOT), \
                f"{datetime.now()}   Problem with 'Forgot password' reference"
            return True
        else:
            print(f"{datetime.now()}   'Login' form is not opened")
            return False

    @allure.step("Close the 'Login' form.")
    def close_login_form(self):
        # self.element_is_clickable(LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM)
        self.browser.find_element(*LoginFormLocators.BUTTON_CLOSE_ON_LOGIN_FORM).click()
        print(f"{datetime.now()}   'Login' form is closed")

    @allure.step("Check that the 'Login' page is open.")
    def should_be_login_page(self):
        """
        Check there are elements to on SignUp page
        """
        # time.sleep(2)
        if self.current_page_is("https://capital.com/trading/login"):
            print(f"{datetime.now()}   'Login' page is opened")
            assert self.element_is_present(*LoginPageLocators.LOGIN_FORM), \
                f"{datetime.now()}   The layout of the 'Login' page has changed"
            assert self.element_is_visible(LoginPageLocators.REF_SIGNUP), \
                f"{datetime.now()}   Problem with 'Sign up' reference"
            assert self.element_is_visible(LoginPageLocators.INPUT_EMAIL), \
                f"{datetime.now()}   Problem with 'E-mail' fild"
            assert self.element_is_visible(LoginPageLocators.INPUT_PASS), \
                f"{datetime.now()}   Problem with 'Password' fild"
            assert self.element_is_visible(LoginPageLocators.BUTTON_CONTINUE), \
                f"{datetime.now()}   Problem with 'Continue' button"
            assert self.element_is_visible(LoginPageLocators.LOGIN_PASS_FORGOT), \
                f"{datetime.now()}   Problem with 'Forgot password' reference"
            return True
        else:
            print(f"{datetime.now()}   'Login' page is not opened")
            return False

    @allure.step("Close the 'Login' page.")
    def close_login_page(self):
        self.browser.back()
        print(f"{datetime.now()}   'Login' page is closed")
