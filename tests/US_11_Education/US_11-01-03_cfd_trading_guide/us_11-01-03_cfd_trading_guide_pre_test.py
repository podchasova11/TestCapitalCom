"""
-*- coding: utf-8 -*-
@Time    : 2023/05/23 18:30 GMT+3
@Author  : Suleyman Alirzaev
"""
import conf
import pytest
import allure
import random  # for new method
from datetime import datetime
from pages.Menu.menu import MenuSection
from tests.build_dynamic_arg import build_dynamic_arg_v2
from pages.conditions import Conditions
from src.src import CapitalComPageSrc
from pages.Elements.testing_elements_locators import SubPages

count = 1


@pytest.mark.us_11_01_03_pre
# @allure.epic('US_11.01.03 | Find links pages in "CFD trading guide" menu')
class TestCFDTradingGuidePretest:
    page_conditions = None

    def check_language(self, cur_language):
        if cur_language not in ["", "de", "el", "es", "fr", "it", "nl", "pl", "ro", "ru", "zh"]:
            pytest.skip(f"This test is not for {cur_language} language")

    # def check_country(self, cur_country):
    #     if cur_country in ["gb"]:
    #         pytest.skip(f"This test is not for {cur_country} country")
    #
    @allure.step("Start pretest")
    def test_cfd_trading_guide_pretest(
            self, worker_id, d, cur_language, cur_country, cur_role, cur_login, cur_password, prob_run_tc):
        global count

        print(f"\n\n{datetime.now()}   Работает obj {self} с именем TC_11.01.03_00")

        build_dynamic_arg_v2(self, d, worker_id, cur_language, cur_country, cur_role, prob_run_tc,
                             "11.01.03", "Educations > Menu item [CFD trading guide]",
                             "00", "Pretest")

        self.check_language(cur_language)
        # self.check_country(cur_country)

        if count == 0:
            pytest.skip("Так надо")

        page_conditions = Conditions(d, "")
        link = page_conditions.preconditions(
            d, CapitalComPageSrc.URL, "", cur_language, cur_country, cur_role, cur_login, cur_password)

        page_menu = MenuSection(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_cfd_trading_guide_move_focus_click(d, cur_language)
        del page_menu

        file_name = "tests/US_11_Education/US_11-01-03_cfd_trading_guide/list_of_href.txt"
        list_items = d.find_elements(*SubPages.SUB_PAGES_LIST)

        count_in = len(list_items)
        print(f"{datetime.now()}   CFD Trading include {count_in} items on selected '{cur_language}' language")
        file = None

        try:
            file = open(file_name, "w")
            count_out = 0
            if count_in > 0:
                for i in range(conf.QTY_LINKS):
                    if i < count_in:
                        k = random.randint(1, count_in)
                        item = list_items[k - 1]
                        file.write(item.get_property("href") + "\n")
                        count_out += 1

            file.write(d.current_url + "\n")    # для добавления головной страницы
            count_in += 1    # для добавления головной страницы
            count_out += 1    # для добавления головной страницы
            print(f"{datetime.now()}   Plus 1 main page CFD Trading. Total: {count_in} for testing")
        finally:
            file.close()
            del file

        print(f"{datetime.now()}   Test data include {count_out} item(s)")
        if count_in != 0:
            print(f"{datetime.now()}   The test coverage = {count_out/count_in*100} %")
        else:
            print(f"{datetime.now()}   The test coverage = 0 %")
        count -= 1
