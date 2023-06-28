"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import random
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin
from pages.Elements.AssertClass import AssertClass
from pages.Elements.testing_elements_locators import ButtonTradeOnWidgetMostTradedLocators

count = 1


@pytest.fixture()
def prob_run_tc():
    prob = 10
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов."


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-02-03_Commodities_trading/list_of_href.txt"

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
            pytest.exit("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_02_03
class TestCommoditiesTrading:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    # @profile(precision=3)
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "01", "Testing button [Log In] in header")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_item_link)

    @allure.step("Start test of button [Trade] in Header")
    # @profile(precision=3)
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_02")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "02", "Testing button [Trade] in header")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_item_link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "03", "Testing button [Start Trading] on Main banner")

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
                test_element.assert_login(d, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

    @allure.step("Start test of button [Try demo] on Main banner")
    # @profile(precision=3)
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "04", "Testing button [Try demo] on Main banner")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    # @profile(precision=3)
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "05", "Testing button [Trade] in Most traded block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if cur_country != 'gb':
            most_traded_quantity = d.find_elements(*ButtonTradeOnWidgetMostTradedLocators.MOST_TRADED)
            for i in range(len(most_traded_quantity)):
                test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
                test_element.arrange_(d, cur_item_link)

                # test_element.element_click(cur_item_link, cur_language, cur_role)
                test_element.element_click(i, cur_role)

                test_element = AssertClass(d, cur_item_link)
                match cur_role:
                    case "NoReg":
                        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
                        test_element.assert_signup(d, cur_language, cur_item_link)
                    case "Reg/NoAuth":
                        test_element.assert_login(d, cur_item_link)
                    case "Auth":
                        test_element.assert_trading_platform(d)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Start trading] in article")
    # @profile(precision=3)
    def test_06_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "06", "Testing button [Start trading] in article")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        test_element = ArticleStartTrading(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of buttons [Sign up] on page")
    # @profile(precision=3)
    def test_07_sign_up_on_page_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Buttons [Sign up] on page
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "07", "Testing buttons [Sign up] on page")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        test_element = PageSignUpLogin(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_item_link, cur_language, cur_role)

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    # @profile(precision=3)
    def test_08_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "08", "Testing button [Create your account] in block [Steps trading]")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        if cur_country != 'gb':
            test_element = BlockStepTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg" | "Reg/NoAuth":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform(d)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Sell] in content block")
    # @profile(precision=3)
    def test_09_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Sell] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "09", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        if cur_country != 'gb':
            test_element = SellButtonContentBlock(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform(d)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Buy] in content block")
    # @profile(precision=3)
    def test_10_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Buy] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_10")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "10", "Testing button [Buy] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        if cur_country != 'gb':
            test_element = BuyButtonContentBlock(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click(cur_role)

            test_element = AssertClass(d, cur_item_link)
            # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
            match cur_role:
                case "NoReg":
                    test_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    test_element.assert_login(d, cur_item_link)
                case "Auth":
                    test_element.assert_trading_platform(d)
        else:
            pytest.skip("This test not for FCA licence.")

    @allure.step("Start test of button [Get started] on Sticky bar")
    # @profile(precision=3)
    def test_11_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_11")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.03", "Educations > Menu item [Commodities trading]",
                             "11", "Testing button [Get started] on Sticky bar")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)


        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)
