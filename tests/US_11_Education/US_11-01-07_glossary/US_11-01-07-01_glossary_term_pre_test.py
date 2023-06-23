"""
-*- coding: utf-8 -*-
@Time    : 2023/05/22 05:50
@Author  : Alexander Tomelo
"""
import allure
import pytest
import random
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg
from pages.Education.Glossary_locators import (
    FinancialDictionary,
)

count = 1
prob = 10   # prob / k = Процент выборки href
k = 10   #


# @pytest.mark.us_11_01_07_pre
class TestGlossaryItemsPretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_glossary_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        global prob
        global k

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07.01_00")

        link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
                                 cur_role, cur_login, cur_password, prob_run_tc,
                                 "11.01.07.01", "",
                                 "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-07_glossary/list_of_href.txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)
        print(f"Glossary include {len(list_items)} financial item(s)")
        f = open(name_file, "w")
        try:
            j = 0
            for i in range(len(list_items)):
                item = list_items[i]
                if random.randint(1, int(100 * k)) <= prob:
                    f.write(item.get_property("href") + "\n")
                    j += 1
        finally:
            f.close()
        print(f"The probability of test coverage is {int(prob/k)} percents")
        print(f"Test data include {j} financial item(s)")

        count -= 1

        del page_menu
