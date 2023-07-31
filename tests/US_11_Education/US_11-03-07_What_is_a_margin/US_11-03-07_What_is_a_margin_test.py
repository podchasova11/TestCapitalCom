import pytest
import allure
from datetime import datetime

from pages.Elements.BlockStepTrading import BlockStepTrading
from pages.Elements.ButtonFreeDemoOnHorizontalBanner import ButtonFreeDemoOnHorizontalBanner
from pages.Elements.ButtonInBanner import ButtonInBanner
from pages.Elements.ButtonStartTradingMainBanner import MainBannerStartTrading
from pages.Elements.ButtonTradeOnWidgetMostTraded import ButtonTradeOnWidgetMostTraded
from pages.Elements.ButtonTryDemoMainBanner import MainBannerTryDemo
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.AssertClass import AssertClass


@pytest.mark.us_11_03_07
class TestWhatIsMargin:
    page_conditions = None

    @allure.step("Start test of button [Start trading] on Main banner")
    def test_01_main_banner_start_trading_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Start Trading] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_01")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]",
                             "01", "Testing button [Start Trading] on Main banner")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = MainBannerStartTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test of button [Try demo] on Main banner")
    def test_02_main_banner_try_demo_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try demo] on Main banner
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_02")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]",
                             "02", "Testing button [Try demo] on Main banner")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = MainBannerTryDemo(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link, demo=True)

    @allure.step("Start test of buttons [Trade] in Most traded block")
    def test_03_most_traded_trade_button(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Trade] in Most traded block
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_03")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]",
                             "03", "Testing button [Trade] in Most traded block")

        if cur_country == 'gb':
            pytest.skip("This test is not supported on UK location")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = ButtonTradeOnWidgetMostTraded(d, link)
        test_elements_list = test_element.arrange_v2_()
        for index, element in enumerate(test_elements_list):
            print(f"\n{datetime.now()}   Testing element #{index + 1}")
            if not test_element.element_click_v2(element):
                pytest.fail("Testing element is not clicked")
            check_element = AssertClass(d, link)
            match cur_role:
                case "NoReg":
                    check_element.assert_signup(d, cur_language, link)
                case "Reg/NoAuth":
                    check_element.assert_login(d, cur_language, link)
                case "Auth":
                    check_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test of button [1. Create & verify your account] in Block 'Steps trading'")
    def test_04_create_and_verify_your_account_button_in_block_steps_trading(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [1. Create & verify your account] in block 'Steps trading'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_04")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]",
                             "04", "Testing button [1. Create & verify your account] in Block 'Steps trading'")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = BlockStepTrading(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case ("NoReg" | "Reg/NoAuth"):
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test of button [Create account] in Block 'Open a trading account in less than 3 minutes'")
    def test_05_create_account_in_block_open_trading_account_3_minutes(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Create account] in Block 'Open a trading account in less than 3 minutes'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_05")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]", "05",
                             "Testing button [Create account] in Block 'Open a trading account in less than 3 minutes'")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = ButtonInBanner(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case ("NoReg" | "Reg/NoAuth"):
                test_element.assert_signup(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)

    @allure.step("Start test of button [Try Free Demo] in Block 'Want a test drive?'")
    def test_06_try_free_demo_in_block_want_test_drive(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        """
        Check: Button [Try Free Demo] in Block 'Want a test drive?'
        Language: All. License: All.
        """
        print(f"\n{datetime.now()}   Работает obj {self} с именем TC_11.03.07_06")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.03.07", "Educations > Menu item [What is a margin?]", "06",
                             "Testing button [Try Free Demo] in Block 'Want a test drive?'")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        link = page_menu.sub_menu_what_is_a_margin_move_focus_click(d, cur_language)

        test_element = ButtonFreeDemoOnHorizontalBanner(d, link)
        test_element.arrange_(d, link)

        if not test_element.element_click():
            pytest.fail("Testing element is not clicked")

        test_element = AssertClass(d, link)
        match cur_role:
            case "NoReg":
                test_element.assert_signup(d, cur_language, link)
            case "Reg/NoAuth":
                test_element.assert_login(d, cur_language, link)
            case "Auth":
                test_element.assert_trading_platform_v2(d, link)
