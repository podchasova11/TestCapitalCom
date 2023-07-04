"""
-*- coding: utf-8 -*-
@Time    : 2023/06/19 19:00 GMT+3
@Author  : Suleyman Alirzaev
"""
# import os.path
import pytest
import allure
import random  # for new method
from datetime import datetime
from pages.base_page import calc_const_and_k  # for new method
from pages.Menu.menu import MenuSection
# from tests.build_dynamic_arg import build_dynamic_arg
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_02_07_pre
# @allure.epic('US_11.02.07 | Find materials pages in "ETF trading" menu')
class TestETFTradingPretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_etf_trading_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.07_00")

        # link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
        #                          cur_role, cur_login, cur_password, prob_run_tc,
        #                          "11.02.07", "",
        #                          "00", "Pretest")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.02.07", "Pretest",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_etf_trading_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-02-07_ETF_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        count_all = len(list_items)  # for new method
        print(f"{datetime.now()}   ETF trading include {count_all} sub-pages")
        const, k = calc_const_and_k(count_all)  # for new method

        f = open(name_file, "w")
        try:
            j = 0  # for new method
            if count_all > 0:  # for new method
                for i in range(count_all):  # for new method
                    if random.randint(1, k) <= const:  # for new method
                        f.write(list_items[i].get_property("href") + "\n")
                        j += 1  # for new method
            else:
                f.write(d.current_url + "\n")
                j += 1  # for fixed bug
                count_all = 1  # for fixed bug
        finally:
            f.close()

        print(f"{datetime.now()}   Test data include {j} ETF trading sub-pages")  # for new method
        print(f"{datetime.now()}   The probability of test coverage = {j / count_all * 100} %")  # for new method

        count -= 1
