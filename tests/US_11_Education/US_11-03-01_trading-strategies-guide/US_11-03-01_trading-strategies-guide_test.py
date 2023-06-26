import random

import allure
import pytest
from datetime import datetime

from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Menu.menu import MenuSection
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def cur_time():
    return str(datetime.now())


@pytest.fixture()
def prob_run_tc():
    """
    Выбор процента покрытия тестов
    """
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_11_03_01
class TestTradingStrategiesGuides:

    page_conditions = None

    @allure.step("Start test_11.03.01_01 of button [Log in] on Header")
    def test_11_03_01_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_01")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
                                 "01", "Testing button [Log In] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)
        test_element.element_click()
        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language)

    @allure.step("Start test_11.03.01_02 of button [Trade] on Header")
    def test_11_03_01_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_02")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
                                 "02", "Testing button [Trade] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)
        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.03.01_03 button 'Create_verify_your_account' on the page.")
    def test_11_03_01_03_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role,
            cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_03")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
                                 "03", "Testing button [Create your account] in block [Steps trading]")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)
        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.03.01_04 of button [Start Trading] on Main banner")
    def test_11_03_01_04_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_04")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.03.01", "Education > Menu Item [Trading Strategies Guides]",
                                 "04", "Testing button [Start Trading] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)
        test_element.element_click()

        test_element = AssertClass(d, link)

        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, link)
            case "Auth":
                test_element.assert_trading_platform(d)

    @allure.step("Start test_11.03.01_05 of button [Try demo] on Main banner")
    def test_11_03_01_05_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.01_05")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                 prob_run_tc,
                                 "11.03.01", "Educations > Menu item [Trading Strategies Guides]",
                                 "05", "Testing button [Try demo] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_strategies_guide_move_focus_click(d, cur_language)
        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)
        test_element.element_click()

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, link)
            case "Auth":
                test_element.assert_trading_platform(d)
