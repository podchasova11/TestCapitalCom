

import random
from datetime import datetime
import allure
import pytest
import sys

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


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = ""
        name_file = "tests/US_11_Education/US_11.01.01-Basics_of_trading/list_of_href"
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


@pytest.mark.us_11_01_01
@pytest.mark.parametrize(
    "cur_login, cur_password",
    [
        ("Empty", "Empty"),
        # ("aqa.tomelo.an@gmail.com", "iT9Vgqi6d$fiZ*Z"),
    ], scope="class"
)
class TestBasicsOfTrading:
    page_conditions = None

    @allure.step("Start test button 'Create_verify_your_account' on the page.")
    def test_01_01_create_verify_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
# Arrange
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11_01_01 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        self.bild_dynamic_arg(d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                              "11.01.01", "01", "Testing button [Create your account] in block [Steps trading]")

        # if prob_run_tc != "":
        #     pytest.skip(f"{prob_run_tc}   {datetime_now}")

        # page3 = Conditions(d, "")
        # cur_item_link = page3.preconditions(
        #     d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password
        # )

        if cur_role == "NoReg":
            page3 = Header(d, cur_item_link)
            if not page3.current_page_is(cur_item_link):
                page3.open_page()
            page3 = BurgerMenu(d, cur_item_link)
            page3.sub_menu_basics_of_trading_move_focus_click(d, cur_language)
            page3 = TheBasicsOfTrading(d, cur_item_link)
            # page3.tc_03_current_url()
            # page3.tc_03_should_be_learn_to_trade_text()
    # Act
            if not page3.tc_01_01_click_button_1_create_verify_your_account_button():
                pytest.fail(f"{datetime.now()}   Checking element is not on this page!")
    # Assert
            if cur_role == "NoReg":
                page3 = SignupLogin(d, cur_item_link)
            if page3.should_be_signup_form(cur_language):
                page3.close_signup_form()
            elif page3.should_be_signup_page(cur_language):
                page3.close_signup_page()
            else:
                pytest.fail(f"{datetime.now()}   Unknown registration method!")
        else:
            pytest.mark.xfail(f"This test for 'NoReg' role")


def bild_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc,
                     us, num_tc, desc_story):
        """
        function for dynamic bild names pf epic, feature and story
        """
        # global page_conditions
        # global count_init
        tc = "TC_" + us + "_" + num_tc
        print(f"\n{datetime.now()}   worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start {tc}")
        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")
        print(f"\n{datetime.now()}   0. Arrange")

        dynamic_epic = \
            "US_" + us + " | " + "Testing Base of trading Item page in menu 'Education'" + " / " + cur_role
        #        "US_" + us + " | " + "Testing Glossary Item page in menu 'Education to trade'" +
        #        " / {" + cur_role + "}"
        dynamic_feature = \
            "TS_" + us + " | " + "Test menu 'Education to Trade' > 'Base of trading' >" \
                                 " 'Item page'" + " / " + cur_language
        #         "TS_" + us + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Item page'" + " / {" +
        # cur_language + "}"
        dynamic_story = \
            cur_country + " / " + "TC_" + us + "_" + num_tc + " | " + desc_story
        #       "{" + cur_license + "} / " + "TC_" + us + "_" + num_tc + " | " + desc_story

        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)
        allure.dynamic.title(f"TC_{us}_{num_tc} with parameters: {cur_language}, {cur_country}, {cur_role}")
        del dynamic_story
        del dynamic_feature
        del dynamic_epic


        self.page_conditions = Conditions(d, "")
        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")

        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        print(f"\n{datetime.now()}   {self}.{self.page_conditions}")
        print(f"{datetime.now()}   sys.getrefcount(page_conditions) = {sys.getrefcount(self.page_conditions)}")
        del self.page_conditions
        del tc

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")
