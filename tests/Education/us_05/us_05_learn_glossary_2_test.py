"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import allure
import random
# from memory_profiler import profile
from datetime import datetime
from pages.conditions import Conditions
from pages.Header.header import Header
from pages.Education.learn_glossary import ItemPage
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
    """
    Fixture for реализации вероятности выполнения теста
    """
    prob = 25
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов."


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        cur_language = "pt"
        name_file = "tests/Education/us_05/list_of_href"
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


@pytest.fixture(
    scope="class",
    params=[
        # "ar",
        # "bg",
        # "cn",  # Education to trade present, financial glossary not present
        # "cs",
        # "da",
        # "de",
        # "el",
        # "",  # "en"
        # "es",
        # "et",
        # "fi",
        # "fr",
        # "hr",
        # "hu",
        # "id",
        # "it",
        # "lt",
        # "lv",
        # "nl",
        # "pl",
        "pt",
        # "ro",
        # "ru",
        # "sk",
        # "sl",
        # "sv",
        # "th",
        # "vi",
        # "zh",
    ],
)
def cur_language(request):
    """Fixture"""
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "ASIC",
        "FCA",
        # "CYSEC",
        # "NBRB",
        # "CCSTV",
        # "SEY",
        # "BAH",
    ],
)
def cur_license(request):
    """Fixture"""
    print(f"Current test license - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        "Reg/NoAuth",
        "Auth",
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
        "aqa.tomelo.an@gmail.com",
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
        "iT9Vgqi6d$fiZ*Z",
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


@pytest.mark.us_05
class TestGlossaryItems:
    # def __init__(self):
    #     self.page_conditions = None
    #     print(f"{datetime.now()}   Init object TestGlossaryItem")

    #
    #
    #
    @allure.step("Start test button 'Log In' on header")
    @allure.title("TC_05.01 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_01_header_button_login(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Header -> button [Log In]
        Language: All. License: All.
        """

        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "01", cur_role, cur_language, cur_license,
                             "Testing 'Log In' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = Header(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.header_button_login_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.header_button_login_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        page_ = SignupLogin(d, cur_item_link)
        if page_.should_be_login_form():
            page_.close_login_form()
        elif page_.should_be_login_page():
            page_.close_login_page()
        else:
            pytest.xfail(f"{datetime.now()}   Unknown registration method!")

    #
    #
    #
    @allure.step("Start test button 'Trade Now' on header")
    @allure.title("TC_05.02 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_02_header_button_trade_now(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Header -> button [Trade Now]
        Language: All. License: All.
        """
        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "02", cur_role, cur_language, cur_license,
                             "Testing 'Trade Now' button on the header page")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = Header(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.header_button_signup_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.header_button_signup_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        page_ = SignupLogin(d, cur_item_link)
        if page_.should_be_signup_form(cur_language):
            page_.close_signup_form()
        elif page_.should_be_signup_page(cur_language):
            page_.close_signup_page()
        else:
            pytest.fail(f"{datetime.now()}   Unknown registration method!")

    #
    #
    #
    @allure.step("Start tests of video banner [Capital,com]")
    @allure.title("TC_05.03 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_03_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Video banner [Capital.com]
        Language: All. License: All.
        """
        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "03", cur_role, cur_language, cur_license,
                             "Testing video banner [Capital.com]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = ItemPage(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.tc_05_03_video_banner_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.tc_05_03_video_in_frame_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page_ = SignupLogin(d, cur_item_link)
                if page_.should_be_signup_form(cur_language):
                    page_.close_signup_form()
                elif page_.should_be_signup_page(cur_language):
                    page_.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method!")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page_ = ItemPage(d, platform_url)
                page_.should_be_trading_platform_page(d)

    #
    #
    #
    @allure.step("Start tests of button under video banner [Capital.com]")
    @allure.title("TC_05.04 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_04_button_trade_now_under_video_banner(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button [Trade now] or [Create account] under video banner [Capital.com]
        Language: All. License: All.
        """

        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "04", cur_role, cur_language, cur_license,
                             "Testing button under video banner [Capital.com]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = ItemPage(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.tc_05_04_button_trade_now_under_video_banner_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.tc_05_04_button_trade_now_under_video_banner_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page_ = SignupLogin(d, cur_item_link)
                if page_.should_be_signup_form(cur_language):
                    page_.close_signup_form()
                elif page_.should_be_signup_page(cur_language):
                    page_.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method!")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page_ = ItemPage(d, platform_url)
                page_.should_be_trading_platform_page(d)

    #
    #
    #
    @allure.step("Start tests of button on vertical or horizontal banner.")
    @allure.title("TC_05.05 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_05_vert_hor_banner_button_create_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button on vertical or horizontal banner
        Language: All. License: All.
        """

        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "05", cur_role, cur_language, cur_license,
                             "Testing buttons on vertical or horizontal banner")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = ItemPage(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.tc_05_05_vert_hor_banner_button_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.tc_05_05_vert_hor_banner_button_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page_ = SignupLogin(d, cur_item_link)
                if page_.should_be_signup_form(cur_language):
                    page_.close_signup_form()
                elif page_.should_be_signup_page(cur_language):
                    page_.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page_ = ItemPage(d, platform_url)
                page_.should_be_trading_platform_page(d)

    #
    #
    #
    @allure.step("Start tests of '1. Create your account' button in 'Steps trading' block")
    @allure.title("TC_05.06 with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_05_06_block_steps_trading_button_1_create_your_account(
            self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role,
            cur_item_link, prob_run_tc, cur_time
    ):
        """
        Check: Button [1. Create your account] in block [Steps trading]
        Language: All. License: All.
        """

        # Arrange
        print(f"worker_id = {worker_id}")
        print(f"\n{datetime.now()}   Start TC")
        print(f"\n{datetime.now()}   Arrange")
        dynamic_epic, dynamic_feature, dynamic_story = \
            bild_dynamic_arg("05", "06", cur_role, cur_language, cur_license,
                             "Testing button [Create your account] in block [Steps trading]")
        allure.dynamic.epic(dynamic_epic)
        allure.dynamic.feature(dynamic_feature)
        allure.dynamic.story(dynamic_story)

        if prob_run_tc != "":
            pytest.skip(f"{prob_run_tc}")

        self.page_conditions = Conditions(d, "")
        self.page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_login, cur_password, cur_role, cur_language, cur_license
        )
        page_ = ItemPage(d, cur_item_link)
        if not page_.current_page_is(cur_item_link):
            print("")
            page_.open_page()
        if not page_.tc_05_06_button_create_your_account_is_visible():
            pytest.fail(f"{datetime.now()}   Checking element is not on this page!")

        # Act
        print(f"\n{datetime.now()}   Act")
        page_.tc_05_06_button_create_your_account_click()

        # Assert
        print(f"\n{datetime.now()}   Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                page_ = SignupLogin(d, cur_item_link)
                if page_.should_be_signup_form(cur_language):
                    page_.close_signup_form()
                elif page_.should_be_signup_page(cur_language):
                    page_.close_signup_page()
                else:
                    pytest.fail(f"{datetime.now()}   Unknown registration method")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                page_ = ItemPage(d, platform_url)
                page_.should_be_trading_platform_page(d)


# @profile(precision=3)
def bild_dynamic_arg(num1, num2, cur_role, cur_language, cur_license, desc_story):
    """
    function for dynamic bild names pf epic, feature and story
    """
    dynamic_epic = \
        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / " + cur_role
    #        "US_" + num1 + " | " + "Testing Glossary Item page in menu 'Education to trade'" + " / {" + cur_role + "}"
    dynamic_feature = \
        "TS_" + num1 + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Item page'" + " / " + cur_language
    #         "TS_" + num1 + " | " + "Test menu 'Education to Trade' > 'Glossary page' > 'Item page'" + " / {" +
    # cur_language + "}"
    dynamic_story = \
        cur_license + " / " + "TC_" + num1 + "." + num2 + " | " + desc_story
    #       "{" + cur_license + "} / " + "TC_" + num1 + "." + num2 + " | " + desc_story
    return dynamic_epic, dynamic_feature, dynamic_story
