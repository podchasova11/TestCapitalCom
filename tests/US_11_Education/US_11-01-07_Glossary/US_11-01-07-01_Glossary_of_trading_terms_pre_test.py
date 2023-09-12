"""
-*- coding: utf-8 -*-
@Time    : 2023/05/22 05:50
@Author  : Alexander Tomelo
"""
import allure
import pytest
import random  # for new method
from datetime import datetime
import conf
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

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.07_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.07",
                             "Educations > Menu item [Glossary of trading terms]",
                             "00",
                             "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        if cur_language not in ["", "de", "el", "es", "fr", "it", "hu", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test-case is not for {cur_language} language")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-07_Glossary/list_of_href.txt"
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   Glossary include {count_in} financial item(s)")
        file = None

        try:
            file = open(name_file, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1
            # file.write(d.current_url + "\n")
            # count_in += 1
            # count_out += 1  # for new method
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
        count -= 1
