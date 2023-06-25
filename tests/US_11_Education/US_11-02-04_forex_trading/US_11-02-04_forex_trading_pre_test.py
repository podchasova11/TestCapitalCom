"""
-*- coding: utf-8 -*-
@Time    : 2023/05/24 13:40
@Author  : Alexander Tomelo
"""
import pytest
import allure
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from pages.Education.forex_trading_locators import ForexTradingItem
from src.src import CapitalComPageSrc

count = 1


# @pytest.mark.us_11_02_04_pre
class TestForexTradingPretest:

    page_conditions = None

    @allure.step("Start pretest")
    def test_forex_trading_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.04_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.04", "",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_forex_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        file_name = "tests/US_11_Education/US_11-02-04_forex_trading/list_of_href.txt"
        list_items = d.find_elements(*ForexTradingItem.ITEM_LIST)
        print(f"Forex trading include {len(list_items)} item(s) on page")
        f = open(file_name, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

        count -= 1

