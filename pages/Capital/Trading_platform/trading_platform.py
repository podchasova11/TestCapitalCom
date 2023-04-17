"""
-*- coding: utf-8 -*-
@Time    : 2023/04/14 11:00
@Author  : Alexander Tomelo
"""
import allure
from pages.Capital.Trading_platform.Topbar.topbar import TopBar
from pages.base_page import BasePage


class TradingPlatform(BasePage):
    @allure.step("Checking that the trading platform page has opened")
    # @profile(precision=3)
    def should_be_trading_platform_page(self, d, link):
        """Check if the page is open"""
        page_ = TopBar(d, link)
        if page_.trading_platform_logo_is_present():
            d.back()
            del page_
            assert True
        else:
            d.back()
            del page_
            assert False, 'Page with title "Trading Platform | Capital.com" not loaded'
