"""
-*- coding: utf-8 -*-
@Time    : 2023/05/22 05:50
@Author  : Alexander Tomelo
"""
import allure
import pytest
import random  # for new method
from datetime import datetime
from pages.base_page import calc_const_and_k  # for new method
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Education.Glossary_locators import (
    FinancialDictionary,
)

count = 1


# @pytest.mark.us_11_01_07_pre
class TestGlossaryItemsPretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_glossary_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             # "11.01.07.01", "Educations > Menu item [Glossary of trading terms] > Trading Term",
                             "11.01.07.01", "Pretest",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-07_glossary/list_of_href.txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)

        count_all = len(list_items)  # for new method
        print(f"{datetime.now()}   Glossary include {count_all} financial item(s)")  # for new method

        if count_all > 0:
            const, k = calc_const_and_k(count_all)  # for new method

            f = open(name_file, "w")
            try:
                j = 0  # for new method
                for i in range(len(list_items)):
                    item = list_items[i]
                    if random.randint(1, k) <= const:  # for new method
                        f.write(item.get_property("href") + "\n")
                        j += 1  # for new method
            finally:
                f.close()
            print(f"{datetime.now()}   Test data include {j} financial item(s)")  # for new method
            print(f"{datetime.now()}   The probability of test coverage = {j/count_all*100} %")  # for new method

        count -= 1
