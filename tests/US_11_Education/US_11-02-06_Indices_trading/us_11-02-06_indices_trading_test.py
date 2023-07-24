import pytest
import allure
from datetime import datetime

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonStartTradingInArticle import ArticleStartTrading
from pages.Elements.ButtonBuyInContentBlock import BuyButtonContentBlock
from pages.Elements.ButtonGetStartedOnStickyBar import GetStartedOnStickyBar
from pages.Elements.ButtonSellInContentBlock import SellButtonContentBlock
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Elements.HeaderButtonTrade import HeaderButtonTrade
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.HeaderButtonLogin import HeaderButtonLogin
from pages.Elements.AssertClass import AssertClass

count = 1


def pytest_generate_tests(metafunc):
    """
    Fixture generation test data
    """
    if "cur_item_link" in metafunc.fixturenames:
        name_file = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
        list_item_link = list()
        try:
            with open(name_file, "r") as file:
                for line in file:
                    list_item_link.append(line[:-1])
        except FileNotFoundError:
            print(f"{datetime.now()}   There is no file with name {name_file}!")
        metafunc.parametrize("cur_item_link", list_item_link, scope="class")

        if len(list_item_link) == 0:
            pytest.exit("Отсутствуют тестовые данные: нет списка ссылок на страницы")


@pytest.mark.us_11_02_06
class TestIndicesTrading:
    page_conditions = None

    @allure.step("Start test of button [Log in] on Header")
    def test_01_header_button_login(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Log In]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_01")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "01", "Testing button [Log In] on Header")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = HeaderButtonLogin(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_login(d, cur_language, cur_item_link)

    @allure.step("Start test of button [Trade] on Header")
    def test_02_header_button_trade(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade]
        Language: All. License: All.
        """
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "02", "Testing button [Trade] on Header")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = HeaderButtonTrade(d, cur_item_link)
        test_element.arrange_(d, cur_role, cur_item_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        test_element.assert_signup(d, cur_language, cur_item_link)

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_03_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "03", "Testing button [Start Trading] on Main banner")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerStartTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_04_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "04", "Testing button [Try demo] on Main banner")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = MainBannerTryDemo(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link, demo=True)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_05_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "05", "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ButtonTradeOnWidgetMostTraded(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    def test_06_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "06", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BlockStepTrading(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg", "Reg/NoAuth":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Get started] on Sticky bar")
    def test_07_sticky_bar_button_get_started(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [1. Get started] on Sticky bar
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_07")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "07", "Testing button [Get started] on Sticky bar")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = GetStartedOnStickyBar(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click()

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Start trading] in content block")
    def test_08_start_trading_in_content_block_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, cur_item_link,
            prob_run_tc):
        """
        Check: Button [Start trading] in article
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_08")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "08", "Testing button [Start trading] in Content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = ArticleStartTrading(d, cur_item_link)
        test_elements_list = test_element.arrange_v2_()

        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")

            check_element = AssertClass(d, cur_item_link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, cur_item_link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_item_link)
                case "Auth":
                    check_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Sell] in content block")
    def test_09_content_block_button_sell(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Sell] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_09")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "09", "Testing button [Sell] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = SellButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)

    @allure.step("Start test of button [Buy] in content block")
    def test_10_content_block_button_buy(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password,
            cur_item_link, prob_run_tc):
        """
        Check: Button [Buy] in content block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.02.04_10")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.06", "Educations > Menu item [Indices Trading]",
                             "10", "Testing button [Buy] in content block")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        test_element = BuyButtonContentBlock(d, cur_item_link)
        test_element.arrange_(d, cur_item_link)

        test_element.element_click(cur_role)

        test_element = AssertClass(d, cur_item_link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, cur_item_link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, cur_item_link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, cur_item_link)
