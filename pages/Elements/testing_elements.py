import pytest
from datetime import datetime
from pages.base_page import BasePage
from pages.Header.header import Header
from pages.Signup_login.signup_login import SignupLogin
from pages.Education.glossary import GlossaryPage


class AssertClass(BasePage):
    page_signup_login = None
    page_glossary = None

    def assert_signup(self, d, cur_language, cur_role, cur_item_link):
        print(f"\n{datetime.now()}   3. Assert")
        match cur_role:
            case "NoReg" | "Reg/NoAuth":
                self.page_signup_login = SignupLogin(d, cur_item_link)
                if self.page_signup_login.should_be_signup_form(cur_language):
                    self.page_signup_login.close_signup_form()
                elif self.page_signup_login.should_be_signup_page(cur_language):
                    self.page_signup_login.close_signup_page()
                else:
                    pytest.fail("Unknown registration method")
            case "Auth":
                platform_url = "https://capital.com/trading/platform"
                self.page_glossary = GlossaryPage(d)
                self.page_glossary.should_be_trading_platform_page(d, platform_url)

        self.page_glossary = ""
        self.page_signup_login = ""

    def assert_login(self, d, cur_item_link):
        """Method Assert"""
        print(f"\n{datetime.now()}   3. Assert")
        self.page_signup_login = SignupLogin(d, cur_item_link)
        if self.page_signup_login.should_be_login_form():
            self.page_signup_login.close_login_form()
        elif self.page_signup_login.should_be_login_page():
            self.page_signup_login.close_login_page()
        else:
            pytest.xfail("Unknown registration method")

        self.page_signup_login = ""


class HeaderButtonLogin(BasePage):

    page_header = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        self.page_header = Header(d, cur_item_link)
        if not self.page_header.current_page_is(cur_item_link):
            self.page_header.open_page()
        if not self.page_header.header_button_login_is_visible():
            pytest.fail("Checking element is not on this page")

    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_header.header_button_login_click()

        self.page_header = ""


class HeaderButtonSignup(BasePage):
    page_header = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")

        self.page_header = Header(d, cur_item_link)
        if not self.page_header.current_page_is(cur_item_link):
            print("")
            self.page_header.open_page()
        if not self.page_header.header_button_signup_is_visible():
            pytest.fail("Checking element is not on this page")

    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_header.header_button_signup_click()

        self.page_header = ""


class VideoBanner(BasePage):
    page_glossary = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        self.page_glossary = GlossaryPage(d, cur_item_link)
        if not self.page_glossary.current_page_is(cur_item_link):
            print("")
            self.page_glossary.open_page()
        if not self.page_glossary.tc_05_03_video_banner_is_visible():
            pytest.fail("Checking element is not on this page")

        # Act
    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_glossary.tc_05_03_video_in_frame_click()

        self.page_glossary = ""


class ButtonUnderVideoBanner(BasePage):
    page_glossary = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        self.page_glossary = GlossaryPage(d, cur_item_link)
        if not self.page_glossary.current_page_is(cur_item_link):
            print("")
            self.page_glossary.open_page()
        if not self.page_glossary.tc_05_04_button_trade_now_under_video_banner_is_visible():
            pytest.fail("Checking element is not on this page")

        # Act
    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_glossary.tc_05_04_button_trade_now_under_video_banner_click()

        self.page_glossary = ""


class ButtonOnVerticalOrHorizontalBanner(BasePage):
    page_glossary = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        self.page_glossary = GlossaryPage(d, cur_item_link)
        if not self.page_glossary.current_page_is(cur_item_link):
            print(f"Current page is not {cur_item_link}")
            self.page_glossary.open_page()
        if not self.page_glossary.tc_05_05_vert_hor_banner_button_is_visible():
            pytest.fail("Checking element is not on this page")

    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_glossary.tc_05_05_vert_hor_banner_button_click()

        self.page_glossary = ""


class BlockStillLookingForButtonCreateYouAccount(BasePage):
    page_glossary = None

    def arrange_(self, d, cur_item_link):
        print(f"\n{datetime.now()}   1. Arrange")
        self.page_glossary = GlossaryPage(d, cur_item_link)
        if not self.page_glossary.current_page_is(cur_item_link):
            self.page_glossary.open_page()
        if not self.page_glossary.tc_05_06_button_create_your_account_is_visible():
            pytest.fail("Checking element is not on this page")

        # Act
    def act_(self):
        print(f"\n{datetime.now()}   2. Act")
        self.page_glossary.tc_05_06_button_create_your_account_click()

        self.page_glossary = ""
