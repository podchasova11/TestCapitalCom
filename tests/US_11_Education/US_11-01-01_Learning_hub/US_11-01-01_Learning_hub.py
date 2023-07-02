from datetime import datetime
import allure
import pytest
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Menu.menu import MenuSection
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_01_01
class TestLearningHub:
    page_conditions = None

    @allure.step("Start test_11.01.01_01 of button [Log in] on Header")
    # @profile(precision=3)
    def test_11_01_01_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01_01")
        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role,
                                    prob_run_tc,
                                    "11.01.01", "Education > Menu Item [Learning hub]",
                                    "01", "Testing button [Log In] on Header")
        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language)

    @allure.step("Start test_11.01.01_02 of button [Trade] on Header")
    def test_11_01_01_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01_02")
        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role,
                                    prob_run_tc,
                                    "11.01.01", "Education > Menu Item [Learning hub]",
                                    "02", "Testing button [Trade] on Header")
        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.01.01_03 button 'Create your account' in the block [Steps trading].")
    def test_11_01_01_03_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.01_03 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role,
                                    prob_run_tc,
                                    "11.01.01", "Education > Menu Item [Learning hub]",
                                    "03", "Testing button [Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_learning_hub_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform(d)
