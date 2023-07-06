"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 19:30 GMT+3
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
from pages.Elements.AssertClass import AssertClass
from pages.Elements.QRcodeDecoder import QRCodeDecode
from pages.Elements.ButtonExploreWebPlatform import ButtonExploreWebPlatform
from pages.Menu.menu import MenuSection
from pages.Elements.ButtonCounter import CounterButtonSignUp


@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов."


# def pytest_generate_tests(metafunc):
#     """
#     Fixture generation test data
#     """
#     if "cur_item_link" in metafunc.fixturenames:
#         name_file = "tests/US_11_Education/US_11-01-06_investmate_app/list_of_href.txt"
#
#         list_item_link = list()
#         try:
#             file = open(name_file, "r")
#         except FileNotFoundError:
#             print(f"{datetime.now()}   There is no file with name {name_file}!")
#             pytest.skip("File not found")
#         else:
#             for line in file:
#                 list_item_link.append(line[:-1])
#             file.close()
#
#         metafunc.parametrize("cur_item_link", list_item_link, scope="class")


@pytest.mark.us_11_01_06
class TestInvestmateApp:
    page_conditions = None

    @allure.step("Start test of button [Log In] in Header")
    def test_01_button_login_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Button [Log In] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "01", "Testing button [Log In] in header")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, link)

    @allure.step("Start test of button [Trade] in Header")
    def test_02_button_trade_in_header(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Button [Trade] in Header
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_02")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "02", "Testing button [Trade] in header")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        # test_element.assert_signup(d, cur_language, cur_role, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test of QR code in Investmate block")
    def test_03_qr_code_investmate_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):

        """
        Check: QR code in Investmate block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_03")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "03", "Testing QR code in Investmate block")

        # pytest.skip("Тест в разработке")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = QRCodeDecode(d, link)
        test_element.arrange_(d, link, 'investmate')

        test_element.element_decode()

        test_element = AssertClass(d, link)
        test_element.assert_app_store_investmate(d, link)

    @allure.step("Start test of QR code in Easy learning block")
    def test_04_qr_code_easy_learning_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):

        """
        Check: QR code in Easy learning block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_04")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "04", "Testing QR code in Easy learning block")

        # pytest.skip("Тест в разработке")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = QRCodeDecode(d, link)
        test_element.arrange_(d, link, 'easy_learning')

        test_element.element_decode()

        test_element = AssertClass(d, link)
        test_element.assert_app_store_investmate(d, link)

    @allure.step("Start test of button [Explore Web Platform] in Block 'capital.com'")
    def test_05_button_explore_web_platform(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):

        """
        Check: Button [Explore Web Platform] in Block 'capital.com'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "05", "Testing button [Explore Web Platform] in block 'capital.com'")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = ButtonExploreWebPlatform(d, link)
        test_element.arrange_(link)
        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)

        match cur_role:
            case "NoReg":
                test_element.assert_signup_form_on_the_trading_platform(d)
            case "Reg/NoAuth":
                test_element.assert_login_form_on_the_trading_platform(d)
            case "Auth":
                test_element.assert_trading_platform(d)

    @allure.step("Start test of QR code in Capital block")
    def test_06_qr_code_capital_block(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):

        """
        Check: QR code in Capital block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_06")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "06", "Testing QR code in Capital block")

        # pytest.skip("Тест в разработке")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = QRCodeDecode(d, link)
        test_element.arrange_(d, link, 'capital')

        test_element.element_decode()

        test_element = AssertClass(d, link)
        test_element.assert_app_store(d, link)

    @allure.step("Start test of button [Create account] in block \"Why choose Capital?\"")
    def test_07_button_create_account_why_capital(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc, cur_time):
        """
        Check: Button [Create account] in block "Why choose Capital?"
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_07")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Educations > Menu item [Investmate app]",
                             "07", "Testing button [Create account] in block \"Why choose Capital?\"")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)

        test_element = CounterButtonSignUp(d, link)
        test_element.arrange_(link)

        test_element.element_click()

        test_element = AssertClass(d, link)

        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform(d)
