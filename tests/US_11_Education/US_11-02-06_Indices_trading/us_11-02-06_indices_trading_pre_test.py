"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 18:30 GMT+3
@Author  : Andrey Bozhko
"""
import random
import pytest
import allure
from datetime import datetime
from pages.base_page import calc_const_and_k
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_02_06_pre
# @allure.epic('US_11.02.06 | Find links pages in "Indices Trading Guide" menu')
class TestIndicesTradingGuidePreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_indices_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_00")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.02.06", "",
                                    "00", "Pretest")

        if count == 0:
            pytest.skip("so it is necessary")
            return

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_indices_trading_move_focus_click(d, cur_language)

        # Save links to the file
        name_file = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        count_all = len(list_items)  # for new method
        print(f"Indices Trading Guide include {count_all} items on selected '{cur_language}' language")

        const, k = calc_const_and_k(count_all)
        j = 0
        with open(name_file, "w") as f:
            if count_all > 0:
                for i in range(count_all):
                    if random.randint(1, k) <= const:
                        f.write(list_items[i].get_property("href") + "\n")
                        j += 1
            elif count_all == 0:
                f.write(d.current_url + "\n")

        print(f"{datetime.now()}   Test data include {j} Indices Trading Guide item(s)")  # for new method
        print(f"{datetime.now()}   The probability of test coverage = {j / count_all * 100} %")  # for new method

        count -= 1
