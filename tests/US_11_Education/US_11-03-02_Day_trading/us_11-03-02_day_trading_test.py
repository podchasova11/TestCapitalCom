import random

import pytest
import allure
from datetime import datetime

from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_11_03_02
class TestDayTrading:

    page_conditions = None

    @allure.step("Start test of button [Log in] on Header")
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_01")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                 prob_run_tc,
                                 "11.03.02", "Educations > Menu item [Day Trading]",
                                 "01", "Testing button [Log In] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_login(d, link)

    @allure.step("Start test of button [Trade] on Header")
    def test_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_02")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                 prob_run_tc,
                                 "11.03.02", "Educations > Menu item [Day Trading]",
                                 "02", "Testing button [Trade] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_03")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.03.02", "Educations > Menu item [Day Trading]",
                          "03", "Testing button [Start Trading] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

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

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_04")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.03.02", "Educations > Menu item [Day Trading]",
                          "04", "Testing button [Try demo] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

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

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_05")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.03.02", "Educations > Menu item [Day Trading]",
                          "05", "Testing button [Trade] in Most traded block")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

        most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        for i in range(len(most_traded_quantity)):
            test_element = ButtonTradeOnWidgetMostTraded(d, link)
            test_element.arrange_(d, link)

            test_element.element_click(i, cur_role)

            test_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, link)
                case "Auth":
                    test_element.assert_trading_platform(d)

    @allure.step("Start test of button [Start trading] in content block")
    def test_06_start_trading_in_content_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.02_06")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.03.02", "Educations > Menu item [Day Trading]",
                          "06", "Testing button [Start trading] in Content block")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_day_trading_move_focus_click(d, cur_language)

        test_element = ArticleStartTrading(d, link)
        test_element.arrange_(link)

        test_element.element_click(link, cur_language, cur_role)

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, link)
            case "Auth":
                test_element.assert_trading_platform(d)
