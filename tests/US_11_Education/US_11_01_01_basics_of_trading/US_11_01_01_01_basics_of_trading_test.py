import random
from datetime import datetime
import allure
import pytest
import sys
from tests.bild_dynamic_arg import bild_dynamic_arg
from pages.Header.header import Header
from pages.Education.The_basics_of_trading import TheBasicsOfTrading
from pages.Menu.menu import MenuSection
from pages.Signup_login.signup_login import SignupLogin
from pages.conditions import Conditions
from src.src import (
    CapitalComPageSrc,
    # TradingViewPageSrc,
    # ESGPageSrc,
    # LearnToTradePageSrc,
    # ProfessionalClientsAu,
)
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass


# Процент проведения тестов
@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_11_01_01
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class")


class TestBasicsOfTrading:

    page_conditions = None

    # @allure.step("Start test of button [Log in] on Header")
    # # @profile(precision=3)
    # def test_11_01_01_01_header_button_login(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Log In]
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01.01_01")
    #     link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
    #                             cur_login, cur_password, prob_run_tc,
    #                      "11.01.01.01", "01", "Testing button [Log In] on Header")
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     page_menu.sub_menu_basics_of_trading_move_focus_click(d, cur_language)
    #
    #     test_element = HeaderButtonLogin(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_login(d, cur_language)
    #
    #
    #
    # #
    # @allure.step("Start test of button [Trade] on Header")
    # # @profile(precision=3)
    # def test_11_01_01_02_header_button_trade(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Trade]
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01.01_02")
    #     link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
    #                      "11.01.01.01", "02", "Testing button [Trade] on Header")
    #
    #     if cur_role is "Auth":
    #         pytest.skip('This test not for "Auth" role')
    #
    #     test_element = HeaderButtonTrade(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_signup(d, cur_language, cur_role)

    @allure.step("Start test button 'Create_verify_your_account' on the page.")
    def test_11_01_01_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01_3 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                cur_login, cur_password, prob_run_tc,
                                "11.01.01", "03", "Testing button [Create your account] in block [Steps trading]")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_basics_of_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)
