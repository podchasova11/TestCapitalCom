"""
-*- coding: utf-8 -*-
@Time    : 2023/05/14 19:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime

from pages.Elements.ButtonCreateAccountArticle import ArticleCreateAccount
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInContent import ContentStartTrading
from pages.Elements.AssertClass import AssertClass
from pages.Elements.ButtonSignupLoginOnPage import PageSignUpLogin


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-01-04_spread_betting_guide/list_of_href.txt"

        list_item_link = list()
        try:
            file = open(name_file, "r")
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
            pytest.skip("File not found")
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        if len(list_item_link) == 0:
            pytest.skip("Отсутствуют тестовые данные: нет списка ссылок на страницы")

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_04
class TestSpreadBettingGuide:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "01", "Testing button [Start Trading] on Main banner")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

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
        Language: All. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "02", "Testing button [Try demo] on Main banner")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

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

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_03_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "03", "Testing button [Create your account] in block [Steps trading]")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

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
    def test_04_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: EN, ES. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "04", "Testing button [Start trading] in article")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ContentStartTrading(d, cur_item_link)
        test_element.arrange_(cur_item_link)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Create account] in article")
    def test_05_create_account_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Create account] in article
        Language: All. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "05", "Testing button [Create account] in article")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ArticleCreateAccount(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        # test_element.assert_signup(d, cur_language, 'Auth', cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of buttons [Sign up] on page")
    # @profile(precision=3)
    def test_08_sign_up_on_page_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Buttons [Sign up] on page
        Language: EN, ES. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Educations > Menu item [Spread betting guide]",
                             "08", "Testing buttons [Sign up] on page")

        if cur_language not in ["", "es", "pl", "ru", "cn"]:
            pytest.skip(f"This test not for {cur_language} language")
        if cur_country not in ["gb"]:
            pytest.skip("This test only for FCA licence")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = PageSignUpLogin(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_item_link, cur_language, cur_role)
