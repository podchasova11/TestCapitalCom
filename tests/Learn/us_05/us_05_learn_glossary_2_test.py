"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random
from datetime import datetime
from pages.conditions import Conditions
from pages.Header.header import Header
from pages.Learn.learn_glossary import ItemPage
# from pages.menu import MenuBurger
from pages.Signup_login.signup_login import SignupLogin
from src.src import (
    CapitalComPageSrc,
)
# from pages.learn.learn_glossary_locators import (
#     FinancialDictionary,
# )

list_href = list()


@pytest.fixture()
def prob_run_tc():
    prob = 25
    if random.\
            randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


def pytest_generate_tests(metafunc):
    
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "lt"
        name_file = "tests/Learn/us_05/list_of_href"
        name_file += "_" + cur_language
        name_file += ".txt"

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


@pytest.mark.us_05
class TestGlossaryItems:
    
    #
    #
    #
    @allure.step("Start test button 'Log In' on header")
    @allure.title("TC_05.01 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """
# Arrange
        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "01", cur_role, cur_language,
                             "Testing 'Log In' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page1 = Conditions(d, "")
        page1.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page1 = Header(d, cur_item_link)
        if not page1.current_page_is(cur_item_link):
            print("")
            page1.open_page()
        if not page1.header_button_login_is_visible():
            pytest.xfail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page1.header_button_login_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        page1 = SignupLogin(d, cur_item_link)
        if page1.should_be_login_form():
            page1.close_login_form()
        elif page1.should_be_login_page():
            page1.close_login_page()
        else:
            pytest.xfail(f"{datetime.now()}   Unknown registration method!")

    #
    #
    #
    @allure.step("Start test button 'Trade Now' on header")
    @allure.title("TC_05.02 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
# Arrange
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "02", cur_role, cur_language,
                             "Testing 'Trade Now' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page2 = Conditions(d, "")
        page2.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page2 = Header(d, cur_item_link)
        if not page2.current_page_is(cur_item_link):
            print("")
            page2.open_page()
        if not page2.header_button_signup_is_visible():
            pytest.xfail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page2.header_button_signup_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        page2 = SignupLogin(d, cur_item_link)
        if page2.should_be_signup_form(cur_language):
            page2.close_signup_form()
        elif page2.should_be_signup_page(cur_language):
            page2.close_signup_page()
        else:
            pytest.fail(f"{datetime.now()}   Unknown registration method!")

#
#
#
    @allure.step("Start tests of video banner [Capital,com]")
    @allure.title("TC_05.03 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_03_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
# Arrange
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "03", cur_role, cur_language,
                             "Testing video banner [Capital.com]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page3 = Conditions(d, "")
        page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page3 = ItemPage(d, cur_item_link)
        if not page3.current_page_is(cur_item_link):
            print("")
            page3.open_page()
        if not page3.tc_05_03_video_in_frame_is_present():
            pytest.xfail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page3.tc_05_03_video_in_frame_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page3 = SignupLogin(d, cur_item_link)
                if page3.should_be_signup_form(cur_language):
                    page3.close_signup_form()
                elif page3.should_be_signup_page(cur_language):
                    page3.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method!")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page3 = ItemPage(d, platform_url)
                page3.should_be_trading_platform_page(d)

    #
    #
    #
    @allure.step("Start tests of button under video banner [Capital.com]")
    @allure.title("TC_05.04 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_04_button_trade_now_under_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [Trade now] or [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """
# Arrange
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "04", cur_role, cur_language,
                             "Testing button under video banner [Capital.com]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page4 = Conditions(d, "")
        page4.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page4 = ItemPage(d, cur_item_link)
        if not page4.current_page_is(cur_item_link):
            print("")
            page4.open_page()
        if not page4.tc_05_04_button_trade_now_under_video_banner_is_present():
            pytest.xfail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page4.tc_05_04_button_trade_now_under_video_banner_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page4 = SignupLogin(d, cur_item_link)
                if page4.should_be_signup_form(cur_language):
                    page4.close_signup_form()
                elif page4.should_be_signup_page(cur_language):
                    page4.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method!")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page4 = ItemPage(d, platform_url)
                page4.should_be_trading_platform_page(d)

#
#
#
    @allure.step("Start tests of button on vertical or horisontal banner.")
    @allure.title("TC_05.05 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_05_vert_hor_banner_button_create_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button on vertical or horisontal banner
        Language: All. License: All.
        """
# Arrange
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "05", cur_role, cur_language,
                             "Testing buttons on vertical or horisontal banner")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page5 = Conditions(d, "")
        page5.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page5 = ItemPage(d, cur_item_link)
        if not page5.current_page_is(cur_item_link):
            print("")
            page5.open_page()
        if not page5.tc_05_05_vert_hor_banner_button_is_present():
            pytest.xfail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page5.tc_05_05_vert_hor_banner_button_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page5 = SignupLogin(d, cur_item_link)
                if page5.should_be_signup_form(cur_language):
                    page5.close_signup_form()
                elif page5.should_be_signup_page(cur_language):
                    page5.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page5 = ItemPage(d, platform_url)
                page5.should_be_trading_platform_page(d)

    #
    #
    #
    @allure.step("Start tests of '1. Create your accaunt' button in 'Steps trading' block")
    @allure.title("TC_05.06 with parameters: {cur_language}, {cur_license}, {cur_role}")
    def test_05_06_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc
    ):
        """
        Check: Button [1. Create your accaunt] in block [Steps trading]
        Language: All. License: All.
        """
# Arrange
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "06", cur_role, cur_language,
                             "Testing button [Create your accaunt] in block [Steps trading]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        print(f"\n{datetime.now()}   Arrange")
        print(f"worker_id = {worker_id}")
        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
        page6 = Conditions(d, "")
        page6.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page6 = ItemPage(d, cur_item_link)
        if not page6.current_page_is(cur_item_link):
            print("")
            page6.open_page()
        if not page6.tc_05_06_button_create_your_account_is_present():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")
# Act
        print(f"\n{datetime.now()}   Act")
        page6.tc_05_06_button_create_your_account_click()
# Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page6 = SignupLogin(d, cur_item_link)
                if page6.should_be_signup_form(cur_language):
                    page6.close_signup_form()
                elif page6.should_be_signup_page(cur_language):
                    page6.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page6 = ItemPage(d, platform_url)
                page6.should_be_trading_platform_page(d)


def bild_dynamic_arg(num1, num2, cur_role, cur_language, desc_story):
    dynamic_epic = "US_" + num1 + " | " + "Testing Glossary Item page in menu [Learn to trade]" + " / " + cur_role
    dynamic_feature = "TS_" + num1 + " | " + "Test menu [Learn to Trade] / [Glossary] / [item]" + " / " + cur_language
    dynamic_story = "TS_" + num1 + "." + num2 + " | " + desc_story
    return dynamic_epic, dynamic_feature, dynamic_story,
