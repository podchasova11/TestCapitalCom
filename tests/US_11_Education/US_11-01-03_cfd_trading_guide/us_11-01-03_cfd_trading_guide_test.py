"""
-*- coding: utf-8 -*-
@Time    : 2023/05/14 19:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import random
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime

from pages.Elements.ButtonBuyInTable import BuyButtonTable
from pages.Elements.ButtonSellInTable import SellButtonTable
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        if len(list_item_link) == 0:
            pytest.skip("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_03
class TestCFDTradingGuide:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language not in ["", "de", "el", "es", "fr", "it", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test is not for {cur_language} language")

    def check_country(self, cur_country):
        if cur_country in ["gb"]:
            pytest.skip(f"This test is not for {cur_country} country")

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "01", "Testing button [Start Trading] on Main banner")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "02", "Testing button [Try demo] on Main banner")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "03", "Testing button [Trade] in Most traded block")

        self.check_language(cur_language)
        self.check_country(cur_country)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_element.arrange_v3(d, cur_item_link)

        most_traded_list = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
        i = random.randint(1, len(most_traded_list))
        print(f"\n{datetime.now()}   Rand i = {i}")
        test_element.element_click_v3(i, cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_04_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "04", "Testing button [Create your account] in block [Steps trading]")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Start trading] in article")
    def test_05_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "05", "Testing button [Start trading] in article")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ArticleStartTrading(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Most traded tab")
    def test_06_cfd_table_button_sell_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Sell] in block "CFDs table" in Most traded tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "06", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='most_traded')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Most traded tab")
    def test_07_cfd_table_button_buy_most_traded_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Buy] in block "CFDs table" in Most traded tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "07", "Testing button [Buy] in block \"CFDs table\" in Most traded tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='most_traded')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Top Risers tab")
    def test_08_cfd_table_button_sell_top_risers_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Sell] in block "CFDs table" in Top risers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "08", "Testing button [Sell] in block \"CFDs table\" in Most traded tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='top_risers')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Top risers tab")
    def test_09_cfd_table_button_buy_top_risers_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Buy] in block "CFDs table" in Top risers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "09", "Testing button [Buy] in block \"CFDs table\" in Top risers tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='top_risers')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Top fallers tab")
    def test_10_cfd_table_button_sell_top_fallers_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Sell] in block "CFDs table" in Top fallers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_10")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "10", "Testing button [Sell] in block \"CFDs table\" in Top fallers tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='top_fallers')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Top fallers tab")
    def test_11_cfd_table_button_buy_top_fallers_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Buy] in block "CFDs table" in Top fallers tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_11")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "11", "Testing button [Buy] in block \"CFDs table\" in Top fallers tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='top_fallers')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Sell] in block \"CFDs table\" in Most volatile tab")
    def test_12_cfd_table_button_sell_most_volatile_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Sell] in block "CFDs table" in Most volatile tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_12")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "12", "Testing button [Sell] in block \"CFDs table\" in Most volatile tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='most_volatile')

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Buy] in block \"CFDs table\" in Most volatile tab")
    def test_13_cfd_table_button_buy_most_volatile_tab(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Buy] in block "CFDs table" in Most volatile tab
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_13")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "13", "Testing button [Buy] in block \"CFDs table\" in Most volatile tab")

        self.check_language(cur_language)

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonTable(d, cur_item_link)
        test_element.arrange_(d, cur_item_link, tab='most_volatile')

        test_element.element_click(cur_item_link, cur_language, cur_role)
