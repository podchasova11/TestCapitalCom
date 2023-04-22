"""
-*- coding: utf-8 -*-
@Time    : 2023/04/19 17:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import pytest
import allure
import random
# import sys
# from memory_profiler import profile
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.bild_dynamic_arg import bild_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
# from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
# from pages.Elements.ButtonsMostTradedWidget import MostTraded
from pages.Elements.AssertClass import AssertClass


@pytest.fixture()
def prob_run_tc():
    """
    Fixture for реализации вероятности выполнения теста
    """
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


@pytest.fixture(
    scope="class",
    params=[
        "ar",
        "bg",
        "cn",  # Education to trade present, financial glossary not present
        "cs",
        "da",
        "de",
        "el",
        "",  # "en"
        "es",
        "et",
        "fi",
        "fr",
        "hr",
        "hu",
        "id",
        "it",
        "lt",
        "lv",
        "nl",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        "th",
        "vi",
        "zh",
    ],
)
def cur_language(request):
    """Fixture"""
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "au",  # Australia - "ASIC" - https://capital.com/?country=au
        "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        "tr",  # Turkey - "SCB" - https://capital.com/?country=tr

        # "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg
        # "NBRB" - пока не проверяем
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    print(f"Current country of trading - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        "Reg/NoAuth",
        "Auth"
    ],
)
def cur_role(request):
    """Fixture"""
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "captest852@yopmail.com",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "Testpass123!",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_02_03
class TestCommoditiesTrading:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    # @profile(precision=3)
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_01")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                cur_login, cur_password, prob_run_tc,
                                "11.02.03", "Educations > Menu item [Commodities trading]",
                                "01", "Testing button [Log In] in header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language)


    @allure.step("Start test of button [Trade] in Header")
    # @profile(precision=3)
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_02")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                cur_login, cur_password, prob_run_tc,
                                "11.02.03", "Educations > Menu item [Commodities trading]",
                                "02", "Testing button [Trade] in header")


        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_03")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                prob_run_tc,
                                "11.02.03", "Educations > Menu item [Commodities trading]",
                                "03", "Testing button [Start Trading] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)


    @allure.step("Start test of button [Try demo] on Main banner")
    # @profile(precision=3)
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_04")
        link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
                                prob_run_tc,
                                "11.02.03", "Educations > Menu item [Commodities trading]",
                                "04", "Testing button [Try demo] on Main banner")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, cur_role, link)

    # @allure.step("Start test of buttons [Most traded] on Widget")
    # # @profile(precision=3)
    # def test_05_widget_most_traded_button(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Buttons [Most traded] on Widget
    #     Language: All. License: All.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.03_05")
    #     link = bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password,
    #                             prob_run_tc,
    #                             "11.02.03", "Educations > Menu item [Commodities trading]",
    #                             "05", "Testing buttons [Most traded] on Widget")
    #
    #     page_menu = MenuSection(d, link)
    #     page_menu.menu_education_move_focus(d, cur_language)
    #     page_menu.sub_menu_commodities_trading_move_focus_click(d, cur_language)
    #
    #     test_element = MostTraded(d, link)
    #     test_element.arrange_(d, cur_role, link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, link)
    #     test_element.assert_login(d, cur_language)

