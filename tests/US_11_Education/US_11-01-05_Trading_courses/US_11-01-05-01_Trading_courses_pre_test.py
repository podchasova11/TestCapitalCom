"""
-*- coding: utf-8 -*-
@Time    : 2023/05/25 22:00 GMT+3
@Author  : Liudmila Dankevich
"""


import pytest
import allure
from datetime import datetime
from pages.Menu.menu import MenuSection
from pages.Elements.testing_elements_locators import CoursesPage
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc

count = 1


@pytest.mark.us_11_01_05_pre
@allure.epic('US_11.01.05 | Find materials pages in "Trading_courses" menu')
class TestCoursesItemsPreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_trading_courses_item_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count
        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.05.01_00")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country,
                                    cur_role, prob_run_tc,
                                   "11.01.05.01", "",
                                   "00", "Pretest")
        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        if count == 0:
            pytest.skip("Так надо")
            return

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_trading_courses_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/US_11_Education/US_11-01-05_Trading_courses/list_of_href.txt"
        list_items = d.find_elements(*CoursesPage.COURSES_PAGES_LIST)
        print(f"Trading courses include {len(list_items)} courses item(s) on page")
        f = open(name_file, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

        count -= 1

        del page_menu
