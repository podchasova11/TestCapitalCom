from datetime import datetime

import allure
import pytest

from pages.common import Common
from pages.Menu.menu import MenuSection
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from pages.Elements.ButtonCreateAccountBlockOurCourses import ButtonCreateAccountBlockOurCourses
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_01_05
class TestTradingCourses:
    page_conditions = None

    @allure.step("Start test_11.01.05_01 button [Create account] in the block 'Our courses'.")
    def test_01_create_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Block 'Our courses' -> button [Create account]
        Language: All. License: All. Role: All
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_01 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role,
                                    prob_run_tc,
                                    "11.01.05", "Education > Menu Item [Trading courses]",
                                    "01", "Testing button [Create account] in block [Our courses]")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = ButtonCreateAccountBlockOurCourses(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)

    @allure.step("Start test_11.01.05_04 button [1. Create your account] in block 'Steps trading'.")
    def test_04_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Steps trading -> button [1. Create your account]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_04 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role,
                                    prob_run_tc,
                                    "11.01.05", "Education > Menu Item [Trading courses]",
                                    "04", "Testing button [1. Create your account] in block [Steps trading]")

        if cur_language in ["ar"]:
            Common().skip_test_for_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v3(d, link)
