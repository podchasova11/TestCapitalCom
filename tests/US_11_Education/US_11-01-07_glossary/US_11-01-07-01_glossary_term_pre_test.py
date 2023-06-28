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
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Education.Glossary_locators import (
    FinancialDictionary,
)

count = 1

# Процент выборки href = const / k
# !!! Не изменяемый параметр "const"
const = 100
# изменяемый параметр "k":
# 100% > k=1; 50% > k=2; 25% > k=4; 20% > k=5; 10% > k=10;
# 5% > k=20; 4% > k=25; 3% > k=33; 2% > k=50; 1% > k=100;
# 0,5% > k=200
k = 200  # > 0,5%


# @pytest.mark.us_11_01_07_pre
class TestGlossaryItemsPretest:
    page_conditions = None

    @allure.step("Start pretest")
    def test_glossary_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        global const
        global k

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

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-07_glossary/list_of_href.txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)
        count_all = len(list_items)
        print(f"Glossary include {count_all} financial item(s)")
        f = open(name_file, "w")
        try:
            j = 0
            for i in range(len(list_items)):
                item = list_items[i]
                if random.randint(1, int(100 * k)) <= const:
                    f.write(item.get_property("href") + "\n")
                    j += 1
        finally:
            f.close()
        print(f"Test data include {j} financial item(s)")
        print(f"The probability of test coverage = {j/count_all*100} %")

        count -= 1

        del page_menu
