"""
-*- coding: utf-8 -*-
@Time    : 2023/04/11 19:00
@Author  : Alexander Tomelo
"""
# import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
# from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
# from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from src.src import CapitalComPageSrc


# @pytest.mark.us_11_01_07
class TestGlossaryOfTradingTerms:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    # @allure.step("Start test of button [Log in] on Header")
    # def test_01_header_button_login(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc):
    #     """
    #     Check: Button [Log In]
    #     Language: All. License: All.
    #     """
    #     print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_01")
    #
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.01.07", "Educations > Menu item [Glossary of trading terms]",
    #                          "01", "Testing button [Log In] on Header")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
    #
    #     test_element = HeaderButtonLogin(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     if not test_element.element_click():
    #         pytest.fail("Testing element is not clicked")
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_login(d, cur_language, link)
    #
    #     del test_element
    #     del page_menu
    #
    # @allure.step("Start test of button [Sign up] on Header")
    # # @profile(precision=3)
    # def test_02_header_button_signup(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc):
    #     """
    #     Check: Button [Trade]
    #     Language: All. License: All.
    #     """
    #     print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_02")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.01.07", "Educations > Menu item [Glossary of trading terms]",
    #                          "02", "Testing button [Trade] on Header")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
    #
    #     test_element = HeaderButtonTrade(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_signup(d, cur_language, link)
    #
    #     del test_element
    #     del page_menu
    #
    #
    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    # @profile(precision=3)
    def test_01(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             "01",
                             "Testing button [1. Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

        del test_element
        del page_menu
