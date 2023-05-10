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
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from selenium.common.exceptions import ElementClickInterceptedException
# from pages.Elements.AssertClass import AssertClass
from selenium.webdriver.common.action_chains import ActionChains


# from selenium.webdriver.common.by import By
# from pages.Capital.Trading_platform.trading_platform import TradingPlatform
# from time import sleep


class ButtonTradeOnWidgetMostTraded(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   MOST_TRADED is visible? =>")
        # if self.element_is_visible(ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED):
        if self.browser.find_element(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED):
            print(f"{datetime.now()}   => MOST_TRADED is visible on the page!")
        else:
            print(f"{datetime.now()}   => MOST_TRADED is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button MOST_TRADED")
    def element_click(self, i):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Start Click button MOST_TRADED =>")
        button_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => MOST_TRADED is not present on the page!")
            del button_list
            return False

        print(f"{datetime.now()}   MOST_TRADED scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[i]
        )
        print(f"{datetime.now()}   MOST_TRADED delete js-mostTraded class =>")
        # Удаляем класс js-mostTraded у Most traded блока, чтобы избежать фантомных фейлов
        # (кнопки меняют состояние каждые ~2.5 секунды)
        if i == 0:
            self.browser.execute_script('document.getElementsByClassName("js-mostTraded")[0].'
                                        'classList.remove("js-mostTraded");')

        # Наводим на тестовый элемент, чтобы кнопка могла корректно отработать нажатие
        hover = ActionChains(self.browser).move_to_element(button_list[i])

        print(f"{datetime.now()}   MOST_TRADED click =>")
        try:
            # sleep(2.5*(i+1))
            hover.perform()
            print(f"{datetime.now()}   MOST_TRADED is clickable? =>")
            self.element_is_clickable(button_list[i], 10)
            button_list[i].click()
            print(f"{datetime.now()}   => MOST_TRADED clicked!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")

            page_ = SignupLogin(self.browser)
            if page_.close_signup_form():
                pass
            else:
                page_.close_signup_form()

            del page_
            button_list[0].click()

        del button_list
        return True

    # def arrange_(self, d, cur_item_link):
    #     print(f"\n{datetime.now()}   1. Arrange")
    #
    #     if not self.current_page_is(cur_item_link):
    #         self.link = cur_item_link
    #         self.open_page()
    #
    #     print(f"{datetime.now()}   Is visible MOST_TRADED? =>")
    #     if self.element_is_visible(ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED):
    #         print(f"{datetime.now()}   => MOST_TRADED is visible on the page!")
    #     else:
    #         print(f"{datetime.now()}   => MOST_TRADED is not visible on the page!")
    #         pytest.skip("Checking element is not on this page")
    #
    # @allure.step("Click button MOST_TRADED")
    # def element_click(self, cur_item_link, cur_language, cur_role):
    #     print(f"\n{datetime.now()}   2. Act")
    #     print(f"{datetime.now()}   Start Click button MOST_TRADED =>")
    #     button_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
    #     if len(button_list) >= 1:
    #         self.ClickButton(len(button_list), cur_item_link, cur_language, cur_role)
    #     else:
    #         print(f"{datetime.now()}   => MOST_TRADED is not present on the page!")
    #         del button_list
    #         pytest.skip("Checking element is not present on this page")
    #         return False
    #
    # def ClickButton(self, times, cur_item_link, cur_language, cur_role):
    #     for i in range(times):
    #         button_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
    #         print(f"{datetime.now()}   MOST_TRADED#{i + 1} scroll =>")
    #         self.browser.execute_script(
    #             'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #             button_list[0]
    #         )
    #
    #         print(f"{datetime.now()}   Is MOST_TRADED#{i + 1} clickable? =>")
    #         if self.element_is_clickable(button_list[i], 5):
    #             print(f"{datetime.now()}   => MOST_TRADED#{i + 1} is clickable")
    #
    #         print(f"{datetime.now()}   MOST_TRADED#{i + 1} click =>")
    #         try:
    #             button_list[i].click()
    #             print(f"{datetime.now()}   => MOST_TRADED#{i + 1} clicked!")
    #             test_element = AssertClass(self.browser, cur_item_link)
    #             # test_element.assert_login(self.browser, cur_item_link)
    #             test_element.assert_signup(self.browser, cur_language, cur_role, cur_item_link)
    #
    #         except ElementClickInterceptedException:
    #             print(f"{datetime.now()}   'Signup' or 'Login' form is automatically opened")
    #             page_ = SignupLogin(self.browser)
    #             if page_.close_signup_form():
    #                 pass
    #             else:
    #                 page_.close_signup_form()
    #             del page_
    #         del button_list
    #
    #     return True
