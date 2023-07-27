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
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


class ButtonTradeOnWidgetMostTraded(BasePage):

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        print(f"{datetime.now()}   MOST_TRADED is visible? =>")
        try:
            if self.browser.find_element(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED):
                print(f"{datetime.now()}   => MOST_TRADED is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => MOST_TRADED is not visible on the page!")
            pytest.skip("Checking element is not on this page")

    @allure.step("Click button MOST_TRADED")
    def element_click(self, i, cur_role):
        button_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        # Вытаскиваем линку из кнопки
        button_link = button_list[i].get_attribute('href')
        # Берём ID итема, на который кликаем для сравнения с открытым ID на платформе
        target_link = button_link[button_link.find("spotlight") + 10:button_link.find("?")]
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Start Click button MOST_TRADED =>")
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
        # Удаляем класс js-mostTraded у Most traded блока, чтобы избежать рандомных фейлов
        # (кнопки меняют состояние каждые ~2.5 секунды)
        if i == 0:
            self.browser.execute_script('document.getElementsByClassName("js-mostTraded")[0].'
                                        'classList.remove("js-mostTraded");')

        # Наводим на тестовый элемент, чтобы кнопка могла корректно отработать нажатие
        # hover = ActionChains(self.browser).move_to_element(button_list[i])

        print(f"{datetime.now()}   MOST_TRADED click =>")
        try:
            # sleep(2.5*(i+1))
            # hover.perform()
            print(f"{datetime.now()}   MOST_TRADED is clickable? =>")
            self.element_is_clickable(button_list[i], 10)
            # button_list[i].click()
            self.browser.execute_script("arguments[0].click();", button_list[i])
            print(f"{datetime.now()}   => MOST_TRADED clicked!")

            # Сравниваем ID
            if not self.browser.current_url.find(target_link) and (cur_role == "Auth"):
                pytest.fail(f"[{button_list[i].text}] Opened page's link doesn't match with clicked link")
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

    @allure.step("Works ARRANGE MOST_TRADED (generator) - ver 2")
    def arrange_v2_(self):
        print(f"\n{datetime.now()}   1. Arrange")
        self.open_page()
        item_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)
        if len(item_list) == 0:
            pytest.skip("No items found for testing")
        print(f"{datetime.now()}   => Found {len(item_list)} elements in block MOST_TRADED")
        for i in range(len(item_list)):
            yield item_list[i]
            self.open_page()
            item_list = self.browser.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED_LIST)

    @allure.step("Click button MOST_TRADED - ver 2")
    def element_click_v2(self, web_element):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   Start Click button MOST_TRADED =>")
        print(f"{datetime.now()}   MOST_TRADED Deleting a class that expanded items =>")
        self.browser.execute_script(
            'document.getElementsByClassName("mostTraded__box--expanded")[0]'
            '.classList.remove("mostTraded__box--expanded");')
        print(f"{datetime.now()}   MOST_TRADED scroll =>")
        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            web_element
        )
        print(f"{datetime.now()}   MOST_TRADED click ver 2 =>")
        try:
            web_element.click()
            return True
        except ElementClickInterceptedException:
            return False
