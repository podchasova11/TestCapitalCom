"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 18:30 GMT+3
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


@pytest.mark.us_11_01_06_pre
# @allure.epic('US_11.01.06 | Find links pages in "Investmate app" menu')
class TestInvestmateAppPreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_investmate_app_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.06_00")

        # link = build_dynamic_arg(self, d, worker_id, cur_language, cur_country,
        #                          cur_role, cur_login, cur_password, prob_run_tc,
        #                          "11.01.06", "",
        #                          "00", "Pretest")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.06", "Pretest",
                             "00", "Pretest")

        if count == 0:
            pytest.skip("Так надо")
            return

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_investmate_app_move_focus_click(d, cur_language)
        del page_menu

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-06_investmate_app/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)
        print(f"Investmate app include {len(list_items)} coins items on selected '{cur_language}' language")
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