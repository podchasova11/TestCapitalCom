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

from pages.Elements.ButtonCreateAccountArticle import ArticleCreateAccount
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def prob_run_tc():
    prob = 33
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов."


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
        else:
            for line in file:
                list_item_link.append(line[:-1])
            file.close()

        metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_04
class TestSpreadBettingGuide:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "01", "Testing button [Log In] in header")
        if cur_country == 'gb':
            test_element = HeaderButtonLogin(d, cur_item_link)
            test_element.arrange_(d, cur_role, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_login(d, cur_item_link)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Trade] in Header")
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_02")

        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "02", "Testing button [Trade] in header")
        if cur_country == 'gb':
            test_element = HeaderButtonTrade(d, cur_item_link)
            test_element.arrange_(d, cur_role, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_03")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "03", "Testing button [Start Trading] on Main banner")
        if cur_country == 'gb':
            test_element = MainBannerStartTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_04")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "04", "Testing button [Try demo] on Main banner")
        if cur_country == 'gb':
            test_element = MainBannerTryDemo(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Create your account] in block [Steps trading]")
    def test_05_block_steps_trading_button_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_05")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "05", "Testing button [Create your account] in block [Steps trading]")
        if cur_country == 'gb':
            test_element = BlockStepTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_signup(d, cur_language, cur_role, cur_item_link)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Start trading] in article")
    def test_06_start_trading_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_06")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "06", "Testing button [Start trading] in article")
        if cur_country == 'gb':
            test_element = ArticleStartTrading(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click(cur_item_link, cur_language, cur_role)
        else:
            pytest.skip("This test only for UK")

    @allure.step("Start test of button [Create account] in article")
    def test_07_create_account_in_article_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Create account] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_07")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                          prob_run_tc,
                          "11.01.04", "Educations > Menu item [Spread betting guide]",
                          "07", "Testing button [Create account] in article")
        if cur_country == 'gb':
            test_element = ArticleCreateAccount(d, cur_item_link)
            test_element.arrange_(d, cur_item_link)

            test_element.element_click()

            test_element = AssertClass(d, cur_item_link)
            test_element.assert_signup(d, cur_language, 'Auth', cur_item_link)
        else:
            pytest.skip("This test only for UK")
