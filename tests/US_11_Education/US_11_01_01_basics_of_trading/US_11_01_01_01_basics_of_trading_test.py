

import random
from datetime import datetime
import allure
import pytest

from pages.Header.header import Header
from pages.Education.The_basics_of_trading import TheBasicsOfTrading
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


@pytest.mark.us_11_01_01
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
class TestBasicsOfTrading:

    @allure.feature("F_01.01.01 | Testing 'Create_verify_your_account' button on the page")
    @allure.story("S_01.01.01 | Testing 'Create_verify_your_account' button on the page")
    @allure.step("Start test button 'Create_verify_your_account' on the page.")
    @allure.title("TC_01.01.01 with parameters: {cur_role}, {cur_language}, {cur_license}.   {datetime_now}")
    def test_01_01_create_verify_your_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_country, cur_role, prob_run_tc,
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
            bild_dynamic_arg("01", "01", cur_role, cur_language, cur_country,
                             "Testing 'Create_verify_your_account' button on the page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}   {datetime_now}")

        page3 = Conditions(d, "")
        test_link = page3.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password
        )

        if cur_role == "NoReg":
            page3 = Header(d, test_link)
            if not page3.current_page_is(test_link):
                page3.open_page()
            page3 = BurgerMenu(d, test_link)
            # page3.burger_menu_click(d)
            page3.sub_menu_basics_of_trading_move_focus_click(d, cur_language)
            page3 = TheBasicsOfTrading(d, test_link)
            # page3.tc_03_current_url()
            # page3.tc_03_should_be_learn_to_trade_text()
    # Act
            if not page3.tc_01_01_click_button_1_create_verify_your_account_button():
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


def bild_dynamic_arg(num1, num2, cur_role, cur_language, cur_country, desc_story):
    """
    function for dinamic bild names pf epic, feature and story
    """
    dynamic_epic = \
        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / " + cur_role
#        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / {" + cur_role + "}"
    dynamic_feature = \
        "TS_" + num1 + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Termin page'" + " / " + cur_language
#         "TS_" + num1 + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Termin page'" + " / {" +
    # cur_language + "}"
    dynamic_story = \
        cur_country + " / " + "TC_" + num1 + "." + num2 + " | " + desc_story
#       "{" + cur_license + "} / " + "TC_" + num1 + "." + num2 + " | " + desc_story
    return dynamic_epic, dynamic_feature, dynamic_story,
