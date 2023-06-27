"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
# import os.path
import pytest
import allure
from datetime import datetime
from pages.Menu.menu import MenuSection
# from tests.build_dynamic_arg import build_dynamic_arg
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_01_04_pre
# @allure.epic('US_11.01.04 | Find links pages in "Spread betting guide" menu')
class TestSpreadBettingGuidePreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_spread_betting_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.04_00")

        # link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
        #                          cur_role, cur_login, cur_password, prob_run_tc,
        #                          "11.01.04", "",
        #                          "00", "Pretest")
        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.04", "Pretest",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")

        if cur_country == "gb":

            page_conditions = Conditions(d, "")
            link = page_conditions.preconditions(
                d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

            page_menu = MenuSection(d, link)
            page_menu.menu_education_move_focus(d, cur_language)
            page_menu.sub_menu_spread_betting_guide_move_focus_click(d, cur_language)
            del page_menu

            # Записываем ссылки в файл
            file_name = "tests/US_11_Education/US_11-01-04_spread_betting_guide/list_of_href.txt"
            list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
            print(f"Spread betting guide include {len(list_items)} items on selected '{cur_language}' language")
            f = open(file_name, "w")
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

            # del page_menu
        else:
            pytest.skip("Test section released for FCA licence only.")
            return
