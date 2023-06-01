import random
from datetime import datetime
import allure
import pytest
# import os.path
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Menu.menu import MenuSection
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.Elements.BlockStepTrading import BlockStepTrading
# from pages.Elements.ButtonTryDemoRightBanner import RightBannerTryDemo
from pages.Elements.AssertClass import AssertClass
from pages.Elements.ButtonCreateAccount import ButtonCreateAccountBlockOurCourses
# from pages.Education.trading_courses_locators import CoursesList


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


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
        name_file = "tests/US_11_Education/US_11-01-05_Trading_courses/list_of_href.txt"

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


@pytest.mark.us_11_01_05
class TestTradingCourses:
    page_conditions = None

    @allure.step("Start test_11.01.05_01 of button [Log in] on Header")
    # @profile(precision=3)
    def test_11_01_05_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_01")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.01.05", "Education > Menu Item [Trading courses]",
                                 "01", "Testing button [Log In] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = HeaderButtonLogin(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_login(d, cur_language)

    @allure.step("Start test_11.01.05_02 of button [Trade] on Header")
    def test_11_01_05_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_02")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login,
                                 cur_password, prob_run_tc,
                                 "11.01.05", "Education > Menu Item [Trading courses]",
                                 "02", "Testing button [Trade] on Header")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)
        test_element = HeaderButtonTrade(d, link)
        test_element.arrange_(d, cur_role, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.01.05_03 button [Create account] in the block 'Our courses'.")
    def test_11_01_05_03_create_account_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Header -> button [Log In]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_03 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.01.05", "Education > Menu Item [Trading courses]",
                                 "03", "Testing button [Create account] in block [Our courses]")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = ButtonCreateAccountBlockOurCourses(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.01.05_04 button [Create your account] in block 'Steps trading'.")
    def test_11_01_05_04_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            prob_run_tc, cur_time):
        """
        Check: Steps trading -> button [Create your account]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_04 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                                 cur_login, cur_password, prob_run_tc,
                                 "11.01.05", "Education > Menu Item [Trading courses]",
                                 "04", "Testing button [Create your account] in block [Steps trading]")
        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)
        link = page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        test_element.element_click()

        test_element = AssertClass(d, link)
        test_element.assert_signup(d, cur_language, link)

    @allure.step("Start test_11.01.05.01_01 of button [Log in] on Header")
    # @profile(precision=3)
    def test_11_01_05_01_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05_01")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.01.05.01", "Education > Menu Item [Trading courses]",
                          "01", "Testing button [Log In] on Header")

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_item_link)

    @allure.step("Start test_11.01.05.01_02 of button [Trade] on Header")
    def test_11_01_05_01_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05.01_02")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role, cur_login,
                          cur_password, prob_run_tc,
                          "11.01.05.01", "Education > Menu Item [Trading courses]",
                          "02", "Testing button [Trade] on Header")

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_item_link)

    @allure.step("Start test_11.01.05.01_03 button [Create your account] in block 'Steps trading'.")
    def test_11_01_05_01_03_create_your_account(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc, cur_time):
        """
        Check: Steps trading -> button [Create your account]
        Language: En. License: FCA.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05.01_03 и атрибутами:")
        print(f"\n{datetime.now()}   {self.__dict__}")
        build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
                          cur_login, cur_password, prob_run_tc,
                          "11.01.05.01", "Education > Menu Item [Trading courses]",
                          "03", "Testing button [Create your account] in block [Steps trading]")

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_item_link)

    # @allure.step("Start test_11.01.05.01_04 button [Try demo] in block 'Right banner'.")
    # def test_11_01_05_01_04_try_demo(
    #         self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
    #         prob_run_tc, cur_time):
    #     """
    #     Check: Steps trading -> button [Create your account]
    #     Language: En. License: FCA.
    #     """
    #     print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05.01_04 и атрибутами:")
    #     print(f"\n{datetime.now()}   {self.__dict__}")
    #     build_dynamic_arg(self, d, worker_id, cur_language, cur_country, cur_role,
    #                       cur_login, cur_password, prob_run_tc,
    #                       "11.01.05.01", "Education > Menu Item [Trading courses]",
    #                       "04", "Testing button [Try demo] in block 'Right banner'")
    #
    #     test_element = RightBannerTryDemo(d, cur_item_link)
    #     test_element.arrange_(d, cur_item_link)
    #
    #     test_element.element_click()
    #
    #     test_element = AssertClass(d, cur_item_link)
    #     test_element.assert_signup(d, cur_language, cur_item_link)
