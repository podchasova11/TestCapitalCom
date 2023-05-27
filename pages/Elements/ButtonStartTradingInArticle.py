"""
-*- coding: utf-8 -*-
@Time    : 2023/04/29 00:30
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.Signup_login.signup_login import SignupLogin
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
from selenium.common.exceptions import ElementClickInterceptedException
from pages.Elements.AssertClass import AssertClass


class ArticleStartTrading(BasePage):

    def arrange_(self, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   Is visible BUTTON_START_TRADING_IN_ARTICLE? =>")

        print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE =>")
        if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE2 =>")
            if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
                pytest.skip("Checking element is not on this page")

    @allure.step("Click button BUTTON_START_TRADING_IN_ARTICLE")
    def element_click(self, cur_item_link, cur_language, cur_role):
        button_list = None
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Start Click button BUTTON_START_TRADING_IN_ARTICLE =>")
        if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
        elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
            button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
        if len(button_list) >= 1:
            self.click__button(len(button_list), cur_item_link, cur_language, cur_role)
        else:
            print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
            pytest.skip("Checking element is not present on this page")
            return False

    def click__button(self, times, cur_item_link, cur_language, cur_role):
        for i in range(times):
            if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
                button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
            elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
                button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
            else:
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
                pytest.skip("Checking element is not present on this page")
                return False
            print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} scroll =>")
            self.browser.execute_script(
                'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
                button_list[i]
            )

            print(f"{datetime.now()}   Is BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clickable? =>")
            if self.element_is_clickable(button_list[i], 5):
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} is clickable")

            print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} click =>")
            try:
                button_list[i].click()
                print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clicked!")
                test_element = AssertClass(self.browser, cur_item_link)
                test_element.assert_signup(self.browser, cur_language, cur_role, cur_item_link)
                self.browser.get(cur_item_link)

            except ElementClickInterceptedException:
                print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
                page_ = SignupLogin(self.browser)
                if page_.close_signup_form():
                    pass
                else:
                    page_.close_signup_form()
                del page_
            del button_list

        return True


#
# """
# -*- coding: utf-8 -*-
# @Time    : 2023/04/29 00:30
# @Author  : Suleyman Alirzaev
# """
# from datetime import datetime
# import pytest
# import allure
# from pages.Signup_login.signup_login import SignupLogin
# from pages.base_page import BasePage
# from pages.Elements.testing_elements_locators import ButtonsOnPageLocators
# from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# from pages.Elements.AssertClass import AssertClass
# from selenium.webdriver.common.action_chains import ActionChains
#
# class ArticleStartTrading(BasePage):
#
#     def arrange_(self, d, cur_item_link):
#         print(f"\n{datetime.now()}   1. Arrange")
#
#         if not self.current_page_is(cur_item_link):
#             self.link = cur_item_link
#             self.open_page()
#
#         print(f"{datetime.now()}   Is visible BUTTON_START_TRADING_IN_ARTICLE? =>")
#
#         print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE =>")
#         if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
#             print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE2 =>")
#             if not self.element_is_visible(ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
#                 pytest.skip("Checking element is not on this page")
#
#     @allure.step("Click button BUTTON_START_TRADING_IN_ARTICLE")
#     def element_click(self, cur_item_link, cur_language, cur_role):
#         print(f"\n{datetime.now()}   2. Act")
#         print(f"{datetime.now()}   Start Click button BUTTON_START_TRADING_IN_ARTICLE =>")
#         if self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE):
#             self.button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE)
#         elif self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2):
#             self.button_list = self.browser.find_elements(*ButtonsOnPageLocators.BUTTON_START_TRADING_IN_ARTICLE2)
#         if len(self.button_list) >= 1:
#             self.ClickButton(len(self.button_list), cur_item_link, cur_language, cur_role)
#         else:
#             print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE is not present on the page!")
#             # del self.button_list
#             pytest.skip("Checking element is not present on this page")
#             return False
#
#     def ClickButton(self, times, cur_item_link, cur_language, cur_role):
#         for i in range(times):
#             print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} scroll =>")
#             # self.browser.execute_script(
#             #     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#             #     button_list[i]
#             # )
#             hover = ActionChains(self.browser).move_to_element(self.button_list[i])
#
#             print(f"{datetime.now()}   Is BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clickable? =>")
#             if self.element_is_clickable(self.button_list[i], 5):
#                 print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} is clickable")
#
#             print(f"{datetime.now()}   BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} click =>")
#             try:
#                 hover.perform()
#                 self.button_list[i].click()
#                 print(f"{datetime.now()}   => BUTTON_START_TRADING_IN_ARTICLE_#{i + 1} clicked!")
#                 test_element = AssertClass(self.browser, cur_item_link)
#                 test_element.assert_signup(self.browser, cur_language, cur_role, cur_item_link)
#                 self.browser.get(cur_item_link)
#
#             except ElementClickInterceptedException:
#                 print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
#                 page_ = SignupLogin(self.browser)
#                 if page_.close_signup_form():
#                     pass
#                 else:
#                     page_.close_signup_form()
#                 del page_
#             del self.button_list
#
#         return True
