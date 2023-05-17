"""
-*- coding: utf-8 -*-
@Time    : 2023/05/14 19:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import os.path

import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime

from pages.Elements.ButtonBuyInTable import BuyButtonTableMostTraded
from pages.Elements.ButtonSellInTable import SellButtonTableMostTraded
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import SubPages
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators

count = 1


@pytest.mark.us_11_01_03_pre_2
@allure.epic('US_11.01.03 | Find links pages in "CFD trading guide" menu')
class TestCFDTradingGuide:
    page_conditions = None

    def test_cfd_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        print(f"PATH TO FILE IS: {os.path.abspath(__file__)}")
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_00")

        if count == 0:
            pytest.skip("Так надо")
            return

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                                 cur_role, cur_login, cur_password, prob_run_tc,
                                 "11.01.03", "",
                                 "00", "Pretest")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_cfd_trading_guide_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = f"tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href_{cur_language}.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        print(f"Cryptocurrency trading include {len(list_items)} coins items on selected '{cur_language}' language")
        f = open(name_file, "w")
        try:
            if len(list_items) > 0:
                for i in range(len(list_items)):
                    item = list_items[i]
                    f.write(item.get_property("href") + "\n")
            elif len(list_items) == 0:
                f.write(d.current_url + "\n")
        finally:
            f.close()

        count -= 1

        del page_menu


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = ""
        name_file = f"tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href_{cur_language}.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_03_2
class TestCryptocurrencyTrading:
    page_conditions = None

    # @allure.step("Start test of button [Log In] in Header")
    # def test_01_button_login_in_header(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Log In] in Header
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_01")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
    #                       cur_login, cur_password, prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "01", "Testing button [Log In] in header")
    #     test_element = HeaderButtonLogin(d, cur_item_link)
    #     test_element.arrange_(d, cur_role, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_login(d, cur_item_link)
    #
    # @allure.step("Start test of button [Trade] in Header")
    # def test_02_button_trade_in_header(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Trade] in Header
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_02")
    #
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
    #                       cur_login, cur_password, prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "02", "Testing button [Trade] in header")
    #     test_element = HeaderButtonTrade(d, cur_item_link)
    #     test_element.arrange_(d, cur_role, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
    #
    # @allure.step("Start test of button [Start trading] on Main banner")
    # def test_03_main_banner_start_trading_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Start Trading] on Main banner
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_03")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "03", "Testing button [Start Trading] on Main banner")
    #     test_element = MainBannerStartTrading(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
    #
    # @allure.step("Start test of button [Try demo] on Main banner")
    # def test_04_main_banner_try_demo_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Try demo] on Main banner
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_04")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "04", "Testing button [Try demo] on Main banner")
    #     test_element = MainBannerTryDemo(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
    #
    # @allure.step("Start test of buttons [Trade] in Most traded block")
    # def test_05_most_traded_trade_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Trade] in Most traded block
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_05")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "05", "Testing button [Trade] in Most traded block")
    #
    #     # times = 5
    #     most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
    #     for i in range(len(most_traded_quantity)):
    #         test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
    #         test_element.arrange_(d, cur_item_link)
    #
    #         # test_element.element_click(cur_item_link, cur_language, cur_role)
    #         test_element.element_click(i)
    #
    #         test_element = AssertClass(d, cur_item_link)
    #         match cur_role:
    #             case "NoReg" | "Auth":
    #                 test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
    #             case "Reg/NoAuth":
    #                 test_element.assert_login(d, cur_item_link)
    #
    # @allure.step("Start test of button [Create your account] in block [Steps trading]")
    # def test_06_block_steps_trading_button_create_your_account(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [1. Create your account] in block [Steps trading]
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_06")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "06", "Testing button [Create your account] in block [Steps trading]")
    #     test_element = BlockStepTrading(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
    #
    # @allure.step("Start test of button [Start trading] in article")
    # def test_07_start_trading_in_article_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Button [Start trading] in article
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_07")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                       prob_run_tc,
    #                       "11.01.03", "Educations > Menu item [CFD trading guide]",
    #                       "07", "Testing button [Start trading] in article")
    #     if cur_role == 'Auth':
    #         test_element = ArticleStartTrading(d, cur_item_link)
    #         test_element.arrange_(d, cur_item_link)
    #
    #         test_element.element_click(cur_item_link, cur_language, cur_role)
    #     else:
    #         pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Most traded tab")
    def test_08_01_cfd_table_button_sell_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Sell] in block "CFDs table" in Most traded tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_08_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "08_01", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")
        if cur_role == 'Auth':
            test_element = SellButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='most_traded')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Top Risers tab")
    def test_08_02_cfd_table_button_sell_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Sell] in block "CFDs table" in Top risers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_08_02")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "08_02", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")
        if cur_role == 'Auth':
            test_element = SellButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='top_risers')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Top fallers tab")
    def test_08_03_cfd_table_button_sell_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Sell] in block "CFDs table" in Top fallers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_08_03")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "08_03", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")
        if cur_role == 'Auth':
            test_element = SellButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='top_fallers')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Most Volatile tab")
    def test_08_04_cfd_table_button_sell_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Sell] in block "CFDs table" in Most volatile tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_08_04")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "08_04", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")
        if cur_role == 'Auth':
            test_element = SellButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='most_volatile')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Most traded tab")
    def test_09_01_cfd_table_button_buy_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Buy] in block "CFDs table" in Most traded tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_09_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "09_01", "Testing button [Buy] in block \"CFDs table\" in Most traded tab")
        if cur_role == 'Auth':
            test_element = BuyButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='most_traded')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Top risers tab")
    def test_09_02_cfd_table_button_buy_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Buy] in block "CFDs table" in Top risers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_09_02")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "09_02", "Testing button [Buy] in block \"CFDs table\" in Top risers tab")
        if cur_role == 'Auth':
            test_element = BuyButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='top_risers')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Top fallers tab")
    def test_09_03_cfd_table_button_buy_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Buy] in block "CFDs table" in Top fallers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_09_03")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "09_03", "Testing button [Buy] in block \"CFDs table\" in Top fallers tab")
        if cur_role == 'Auth':
            test_element = BuyButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='top_fallers')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Most volatile tab")
    def test_09_04_cfd_table_button_buy_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Buy] in block "CFDs table" in Most volatile tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_09_04")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.03", "Educations > Menu item [CFD trading guide]",
                          "09_04", "Testing button [Buy] in block \"CFDs table\" in Most volatile tab")
        if cur_role == 'Auth':
            test_element = BuyButtonTableMostTraded(d, cur_item_link)
            test_element.arrange_(d, cur_item_link, tab='most_volatile')

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test is not completed for non-Auth roles")
