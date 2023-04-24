"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pages.base_page import BasePage
from pages.Capital.Trading_platform.Topbar.topbar_locators import TopBarLocators


class TopBar(BasePage):

    @allure.step("Check if the Logo element is present on the page")
    def trading_platform_logo_is_present(self):
        """Check that the Capital.com Logo is present"""
        # Setup wait for later
        print(f"{datetime.now()}   Start check that the Trading platform page is loaded and LOGO is present on it =>")
        timeout = 30
        print(f"{datetime.now()}   Set timeout = {timeout}")
        wait = WebDriverWait(self.browser, timeout)

        # Wait for the new tab to finish loading content
        print(f"{datetime.now()}   Wait until load title =>")
        assert wait.until(EC.title_is("Trading Platform | Capital.com")), \
            'Page with title "Trading Platform | Capital.com" not loaded'
        print(f'{datetime.now()}   => Page with title "Trading Platform | Capital.com" loaded')

        print(f"{datetime.now()}   Is present LOGO on the page? =>")
        if self.element_is_present(*TopBarLocators.LOGO) and self.element_is_visible(TopBarLocators.LOGO, timeout):
            print(f"{datetime.now()}   => LOGO is present on the page!")
            return True
        else:
            print(f"{datetime.now()}   => LOGO is not present on the page!")
            return False
