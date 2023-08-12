"""
-*- coding: utf-8 -*-
@Time    : 2023/06/25 18:30 GMT+3
@Author  : Andrey Bozhko
"""
import random
import pytest
import allure
from datetime import datetime
from pages.Menu.menu import MenuSection
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.Elements.testing_elements_locators import SubPages

first_run_pretest = True


@pytest.mark.us_11_02_06_pre
# @allure.epic('US_11.02.06 | Find links pages in "Indices Trading Guide" menu')
class TestIndicesTradingGuidePreset:
    page_conditions = None

    @allure.step("Start pretest")
    def test_indices_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global first_run_pretest

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.02.06_00")

        link = build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                                    "11.02.06", "Educations > Menu item [Indices Trading]",
                                    "00", "Pretest")

        if not first_run_pretest:
            pytest.skip("Пропускаем претест, так как ранее его уже прошли")

        page_conditions = Conditions(d, "")
        page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_indices_trading_move_focus_click(d, cur_language)

        name_file = "tests/US_11_Education/US_11-02-06_Indices_trading/list_of_href.txt"

        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        href_list = list()
        if len(list_items) > 0:
            href_list = list(map(lambda element: element.get_property("href"), list_items))
        else:
            href_list.append(d.current_url)

        count_all = len(href_list)
        print(f"Indices Trading Guide include {count_all} items on selected '{cur_language}' language")
        # выбираем не более 3-х случайных элементов
        random_list = random.sample(href_list, 3 if count_all >= 3 else count_all)
        with open(name_file, "w", encoding='UTF-8') as f:
            for val in random_list:
                f.write(val + "\n")
        print(f"{datetime.now()}   Test data include {len(random_list)} Indices Trading Guide item(s)")
        print(f"{datetime.now()}   The probability of test coverage = {len(random_list) / count_all * 100} %")
        first_run_pretest = False
