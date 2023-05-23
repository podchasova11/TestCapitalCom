"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
import os.path
import pytest
import allure
# import sys
# from memory_profiler import profile
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_02_05_pre
@allure.epic('US_11.02.05 | Find materials pages in "Cryptocurrency trading" menu')
class TestCryptocurrencyTradingPreset:
    page_conditions = None

    def test_cryptocurrency_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        print(f"PATH TO FILE IS: {os.path.abspath(__file__)}")
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.05_00")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                                 cur_role, cur_login, cur_password, prob_run_tc,
                                 "11.02.05", "",
                                 "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")
            return

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_cryptocurrency_trading_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href.txt"
        # name_file = f"tests/US_11_Education/US_11-02-05_Cryptocurrency_trading/list_of_href_{cur_language}.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        print(f"Cryptocurrency trading include {len(list_items)} coins item(s)")
        # print(f"Cryptocurrency trading include {len(list_items)} coins items on selected '{cur_language}' language")
        f = open(name_file, "w")
        try:
            if len(list_items) > 0:
                for i in range(len(list_items)):
                    item = list_items[i]
                    f.write(item.get_property("href") + "\n")
            elif len(list_items) == 0:
                f.write(d.current_url + "\n")
        finally:
            f.close()

        count -= 1

        del page_menu
