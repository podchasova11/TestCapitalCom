"""
-*- coding: utf-8 -*-
@Time    : 2023/06/19 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
# import random
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
# from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
# from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
# from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
# from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Menu.menu import MenuSection

count = 1


# def pytest_generate_tests(metafunc):
#     """
#     Fixture generation test data
#     """
#     if "cur_item_link" in metafunc.fixturenames:
#         name_file = "tests/US_11_Education/US_11-02-07_ETF_trading/list_of_href.txt"
#
#         list_item_link = list()
#         try:
#             file = open(name_file, "r")
#         except FileNotFoundError:
#             print(f"{datetime.now()}   There is no file with name {name_file}!")
#         else:
#             for line in file:
#                 list_item_link.append(line[:-1])
#             file.close()
#
#         if len(list_item_link) == 0:
#             pytest.skip("Отсутствуют тестовые данные: нет списка ссылок на страницы")
#
#         metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_07
class TestETFTrading:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "01", "Testing button [Log In] in header")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, link)

    @allure.step("Start test of button [Trade] in Header")
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_02")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "02", "Testing button [Trade] in header")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        # test_element.assert_signup(d, cur_language, cur_role, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "03", "Testing button [Start Trading] on Main banner")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        # test_element.assert_signup(d, cur_language, cur_role, link)
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
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "04", "Testing button [Try demo] on Main banner")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        # test_element.assert_signup(d, cur_language, cur_role, link)
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
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "05", "Testing button [Trade] in Most traded block")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        # times = 5
        most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        if cur_country != 'gb':
            for i in range(len(most_traded_quantity)):
                test_element = ButtonTradeOnWidgetMostTraded(d, link)
                test_element.arrange_(d, link)

                # test_element.element_click(link, cur_language, cur_role)
                test_element.element_click(i, cur_role)

                test_element = AssertClass(d, link)
                match cur_role:
                    case "NoReg":
                        # test_element.assert_signup(d, cur_language, cur_role, link)
                        test_element.assert_signup(d, cur_language, link)
                    case "Reg/NoAuth":
                        test_element.assert_login(d, link)
                    case "Auth":
                        test_element.assert_trading_platform(d)
        else:
            pytest.skip("This test is not supported on UK location")

    # @allure.step("Start test of button [Start trading] in article")
    # def test_06_start_trading_in_article_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [Start trading] in article
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_06")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "06", "Testing button [Start trading] in article")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = ArticleStartTrading(d, link)
    #     test_element.arrange_(link)
    #
    #     test_element.element_click(link, cur_language, cur_role)
    #
    # @allure.step("Start test of buttons [Sign up] on page")
    # def test_07_sign_up_on_page_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [Start trading] in article
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_07")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "07", "Testing buttons [Sign up] on page")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = PageSignUpLogin(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click(link, cur_language, cur_role)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_06_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Educations > Menu item [ETF trading]",
                             "06", "Testing button [Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        # test_element.assert_signup(d, cur_language, cur_role, link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform(d)

    # @allure.step("Start test of button [Sell] in content block")
    # def test_09_content_block_button_sell(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [1. Sell] in content block
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_09")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "09", "Testing button [Sell] in content block")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = SellButtonContentBlock(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click(cur_role)
    #
    #     test_element = AssertClass(d, link)
    #     # test_element.assert_signup(d, cur_language, cur_role, link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, link)
    #         case "Reg/NoAuth":
    #             test_element.assert_login(d, link)
    #         case "Auth":
    #             test_element.assert_trading_platform(d)
    #
    # @allure.step("Start test of button [Buy] in content block")
    # def test_10_content_block_button_buy(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [1. Buy] in content block
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_10")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "10", "Testing button [Sell] in content block")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = BuyButtonContentBlock(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click(cur_role)
    #
    #     test_element = AssertClass(d, link)
    #     # test_element.assert_signup(d, cur_language, cur_role, link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, link)
    #         case "Reg/NoAuth":
    #             test_element.assert_login(d, link)
    #         case "Auth":
    #             test_element.assert_trading_platform(d)

    # @allure.step("Start test of button [Get started] on Sticky bar")
    # def test_11_sticky_bar_button_get_started(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
    #     """
    #     Check: Button [1. Get started] on Sticky bar
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_11")
    #     build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
    #                          "11.02.07", "Educations > Menu item [ETF trading]",
    #                          "11", "Testing button [Get started] on Sticky bar")
    #
    #     page_conditions = Conditions(d, "")
    #     link = page_conditions.preconditions(
    #         d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     link = page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
    #
    #     test_element = GetStartedOnStickyBar(d, link)
    #     test_element.arrange_(d, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     # test_element.assert_signup(d, cur_language, cur_role, link)
    #     match cur_role:
    #         case "NoReg":
    #             test_element.assert_signup(d, cur_language, link)
    #         case "Reg/NoAuth":
    #             test_element.assert_login(d, link)
    #         case "Auth":
    #             test_element.assert_trading_platform(d)
