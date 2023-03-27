

import random
from datetime import datetime
import allure
import pytest

from pages.Header.header import Header
from pages.Learn.learn_to_trade import LearnToTrade
from pages.Menu.menu import BurgerMenu
from pages.Signup_login.signup_login import SignupLogin
from pages.conditions import Conditions
from src.src import (
    CapitalComPageSrc,
    # TradingViewPageSrc,
    # ESGPageSrc,
    # LearnToTradePageSrc,
    # ProfessionalClientsAu,
)


# Процент проведения тестов
@pytest.fixture()
def prob_run_tc():
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.mark.us_03
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
@pytest.mark.us_03
class Test_US_03:

    @allure.feature("F_03.01 | Testing 'Log In' button on the header")
    @allure.story("S_01.01 | Testing 'Log In' button on the header")
    @allure.step("Start test 'Log In' button on header.")
    @allure.title("TC_03_01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc,
            datetime_now):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
# Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("03", "01", cur_role, cur_language, cur_license,
                             "Testing 'Log In' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")
        page3 = Conditions(d, "")
        test_link = page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role == "NoReg":
            page3 = Header(d, test_link)
            if not page3.current_page_is(test_link):
                print("")
                page3.open_page()
            page3 = BurgerMenu(d, test_link)
            page3.burger_menu_click(d)
            page3.menu_section_learn_to_trade_click(d, cur_language)
            page3.click_learn_to_trade_item(d, cur_language)
            page3 = LearnToTrade(d, test_link)
            # page3.tc_03_current_url()
            # page3.tc_03_should_be_learn_to_trade_text()
# Act
            print(f"\n{datetime.now()}   Act")
            if not page3.tc_03_01_click_button_login():
                pytest.fail(f"{datetime.now()}   Checking element is not on this page!")
# Assert
            print(f"\n{datetime.now()}   Assert")
            page3 = SignupLogin(d, test_link)
            page3.should_be_login_form()
            page3.close_login_form()
        else:
            pytest.mark.skip(f"This test not for 'Auth' role")

    @allure.feature("F_03_02 | Testing 'Trade_Now' button on the header")
    @allure.story("S_01.02 | Testing 'Trade_Now' button on the header")
    @allure.step("Start test button 'Trade_Now' on header.")
    @allure.title("TC_03_02 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc,
            datetime_now):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
    # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("03", "02", cur_role, cur_language, cur_license,
                             "Testing 'Trade Now' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page3 = Conditions(d, "")
        test_link = page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role == "NoReg":
            page3 = Header(d, test_link)
            if not page3.current_page_is(test_link):
                page3.open_page()
            page3 = BurgerMenu(d, test_link)
            page3.burger_menu_click(d)
            page3.menu_section_learn_to_trade_click(d, cur_language)
            page3.click_learn_to_trade_item(d, cur_language)
            page3 = LearnToTrade(d, test_link)
            # page3.tc_03_current_url()
            # page3.tc_03_should_be_learn_to_trade_text()
    # Act
            if not page3.tc_03_02_click_button_trade_now():
                pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

    # Assert
        if cur_role == "NoReg":
            page3 = SignupLogin(d, test_link)
            if page3.should_be_signup_form(cur_language):
                page3.close_signup_form()
            elif page3.should_be_signup_page(cur_language):
                page3.close_signup_page()
            else:
                pytest.fail(f"{datetime.now()}   Unknown registration method!")

        else:
            pytest.mark.xfail(f"This test for 'NoReg' role")

    @allure.feature("F_03_03 | Testing 'Create_verify_your_account' button on the header")
    @allure.story("S_01.03 | Testing 'Create_verify_your_account' button on the header")
    @allure.step("Start test button 'Create_verify_your_account' on header.")
    @allure.title("TC_03_03 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_03_03_create_verify_your_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc,
            datetime_now):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
# Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("03", "03", cur_role, cur_language, cur_license,
                             "Testing 'Create_verify_your_account' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page3 = Conditions(d, "")
        test_link = page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )

        if cur_role == "NoReg":
            page3 = Header(d, test_link)
            if not page3.current_page_is(test_link):
                page3.open_page()
            page3 = BurgerMenu(d, test_link)
            page3.burger_menu_click(d)
            page3.menu_section_learn_to_trade_click(d, cur_language)
            page3.click_learn_to_trade_item(d, cur_language)
            page3 = LearnToTrade(d, test_link)
            # page3.tc_03_current_url()
            # page3.tc_03_should_be_learn_to_trade_text()
    # Act
            if not page3.tc_03_03_click_button_1_create_verify_your_account_button():
                pytest.fail(f"{datetime.now()}   Checking element is not on this page!")
    # Assert
            if cur_role == "NoReg":
                page3 = SignupLogin(d, test_link)
            if page3.should_be_signup_form(cur_language):
                page3.close_signup_form()
            elif page3.should_be_signup_page(cur_language):
                page3.close_signup_page()
            else:
                pytest.fail(f"{datetime.now()}   Unknown registration method!")
        else:
            pytest.mark.xfail(f"This test for 'NoReg' role")


def bild_dynamic_arg(num1, num2, cur_role, cur_language, cur_license, desc_story):
    """
    function for dinamic bild names pf epic, feature and story
    """
    dynamic_epic = \
        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Learn to trade'" + " / " + cur_role
#        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Learn to trade'" + " / {" + cur_role + "}"
    dynamic_feature = \
        "TS_" + num1 + " | " + "Test menu 'Learn to Trade' > 'Glossary page' > 'Termin page'" + " / " + cur_language
#         "TS_" + num1 + " | " + "Test menu 'Learn to Trade' > 'Glossary page' > 'Termin page'" + " / {" +
    # cur_language + "}"
    dynamic_story = \
        cur_license + " / " + "TC_" + num1 + "." + num2 + " | " + desc_story
#       "{" + cur_license + "} / " + "TC_" + num1 + "." + num2 + " | " + desc_story
    return dynamic_epic, dynamic_feature, dynamic_story,
