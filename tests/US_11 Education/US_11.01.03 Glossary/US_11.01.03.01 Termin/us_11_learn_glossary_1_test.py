"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
import pytest
import random
import allure
# from memory_profiler import profile
from datetime import datetime
from pages.conditions import Conditions
from pages.Menu.menu import BurgerMenu
from src.src import (
    CapitalComPageSrc,
)
from pages.Education.glossary_locators import (
    FinancialDictionary,
)

@pytest.fixture()
# @pytest.fixture(scope="class")
def prob_run_tc():
    """Fixture"""
    prob = 100
    if random.randint(1, 100) <= prob:
        return ""
    else:
        return f"{datetime.now()}   Тест не попал в {prob}% выполняемых тестов.≠"


@pytest.fixture(
    scope="class",
    params=[
        # "ar",
        "bg",
        # "cn",  # Education to trade present, financial glossary not present
        "cs",
        "da",
        "de",
        "el",
        "",  # "en"
        "es",
        "et",
        "fi",
        "fr",
        "hr",
        "hu",
        # "id",
        "it",
        "lt",
        "lv",
        "nl",
        "pl",
        "pt",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        # "th",
        # "vi",
        "zh",
    ],
)
def cur_language(request):
    """Fixture"""
    print(f"Current test language - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "ASIC",
        # "FCA",
        # "CYSEC",
        # "NBRB",
        # "CCSTV",
        # "SEY",
        # "BAH",
    ],
)
def cur_license(request):
    """Fixture"""
    print(f"Current test license - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        # "Reg/NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    """Fixture"""
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())


@pytest.mark.us_11_glossary_pre
@allure.epic('US_05. Testing Glossary Item page in "Education to trade" menu')
class TestGlossaryItemsPreset:

    @allure.feature("TS_05 | Test menu [Education to Trade] / [Glossary] / [item]")
    @allure.story("TC_05.00 | Education Glossary > Pretest")
    @allure.step("Start pretest")
    @allure.title("TC_05.01.01 Pretest with parameters: {cur_language}, {cur_license}, {cur_role}")
    # @profile(precision=3)
    def test_glossary_item_pretest(
            # self, worker_id, d, cur_login, cur_password, cur_language, cur_license, cur_role, prob_run_tc):
            self, worker_id, d, cur_language, cur_role, prob_run_tc):

        page = Conditions(d, "")
        link = page.preconditions(
            d, CapitalComPageSrc.URL, "", "", "", cur_role, cur_language, ""
        )

        page_menu = BurgerMenu(d, link)
        page_menu.menu_education_move_focus(d, cur_language)
        page_menu.sub_menu_glossary_move_focus_click(d, cur_language)

        # Записываем ссылки в файл
        name_file = "tests/US_11 Education/US_11.01.03 Glossary/list_of_href"
        name_file += "_" + cur_language
        name_file += ".txt"
        # list_letters = d.browser.find_elements(*FinancialDictionary.ALPHABET_LIST)
        list_items = d.find_elements(*FinancialDictionary.ITEM_LIST)
        print(f"Glossary include {len(list_items)} financial item(s)")
        f = open(name_file, "w")
        try:
            for i in range(len(list_items)):
                item = list_items[i]
                # list_href.append(item.get_property("href"))
                f.write(item.get_property("href") + "\n")
        finally:
            f.close()

# d.browser.execute_script(
#     'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
#     letter
# )
