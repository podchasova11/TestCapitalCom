"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
# import os
import sys
# import psutil
# import subprocess
# from memory_profiler import profile
from datetime import datetime
# from pages.conditions import Conditions
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.ButtonInBanner import ButtonInBanner
from pages.Elements.VideoBanner import VideoBanner
from pages.Elements.ButtonUnderVideoBanner import ButtonUnderVideoBanner
from pages.Elements.ButtonOnVerOrHorBanner import ButtonOnVerOrHorBanner
from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.AssertClass import AssertClass


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """

    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-01-07_glossary/list_of_href.txt"

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


# @pytest.mark.us_11_01_07_01
class TestGlossaryItems:

    page_conditions = None

    # def __init__(self, *args, **kwargs):
    #     global count_init
    #     print(f"{datetime.now()}   В классе TestGlossaryItems вызван метод __init__ {self}")
    #     count_init += 1
    # super().__init__(*args, **kwargs)

    #
    @allure.step("Start test of button [Log in] on Header")
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                          cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "01", "Testing button [Log In] on Header")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_item_link)

    #
    @allure.step("Start test of button [Trade] on Header")
    def test_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_02")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "02", "Testing button [Trade] on Header")

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_item_link)

    #
    @allure.step("Start test of button [Start Trading]/[Trade now] on inBanner")
    def test_03_button_(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button on inBanner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_03")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "03", "Testing button on inBanner")

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

    @allure.step("Start test of button [Create a demo account]/[Try demo] on inBanner")
    def test_04_button_demo(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button '... demo ...' on inBanner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_04")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "04", "Testing button '... demo ...' on inBanner")

        test_element = ButtonInBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_demo(d)

    #
    @allure.step("Start test of video banner [Capital.com]")
    # @profile(precision=3)
    def test_05_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_05")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "05", "Testing video banner [Capital.com]")

        test_element = VideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

    #
    @allure.step("Start test of button under video banner [Capital.com]")
    # @profile(precision=3)
    def test_06_button_trade_now_under_video_banner(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Trade now] or [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_06")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "06", "Testing button under video banner [Capital.com]")

        test_element = ButtonUnderVideoBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

    #
    @allure.step("Start test of button on vertical or horizontal banner.")
    # @profile(precision=3)
    def test_07_vert_hor_banner_button_create_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button on vertical or horizontal banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_07")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "07", "Testing buttons on vertical or horizontal banner")

        test_element = ButtonOnVerOrHorBanner(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_demo(d)

    #
    @allure.step("Start test of button 'Create your account' in 'Steps trading' block")
    # @profile(precision=3)
    def test_08_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """

        sys.stderr.writelines("Running AT_11-01-07-01_08")

        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_08")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                          "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                          "08", "Testing button [Create your account] in block [Steps trading]")

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform(d)

#
# class Tools:
#     @staticmethod
#     def clear_console():
#         if psutil.WINDOWS:
#             return os.system("cls")
#         else:
#             return os.system("clear")
#
#     @staticmethod
#     def check_output(command: str):
#         try:
#             return subprocess.check_output(command, shell=True,
#                                            universal_newlines=True,
#                                            stderr=subprocess.DEVNULL)
#
#         except subprocess.CalledProcessError:
#             return False
#
#
# def _swap():
#     used = round(psutil.swap_memory().used / 1e+6)
#     all_ = round(psutil.swap_memory().total / 1e+6)
#
#     return f'{used}MiB / {all_}MiB '
#
#
# def _storage():
#     all_ = round(psutil.disk_usage('/.').total / 1e+9)
#     used = round(psutil.disk_usage('/.').used / 1e+9)
#
#     return f'{used}GiB / {all_}GiB '
