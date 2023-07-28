"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import time

import allure
from datetime import datetime
import pytest
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.Menu.menu_locators import (
    Menu1101,
    MenuUS11Education,
    MenuUS11LearningHub,
    MenuUS11TradingCourses,
    MenuUS11Glossary,
    MenuUS11MarketGuides,
    MenuUS11CommoditiesTrading,
    MenuUS11ForexTrading,
    MenuUS11CryptocurrencyTrading,
    MenuUS11CFDTradingGuide,
    MenuUS11SpreadBettingGuide,
    MenuUS11ETFTrading,
    MenuUS11TradingStrategiesGuide,
    MenuUS11DayTrading,
    MenuUS11IndicesTrading,
    MenuUS11InvestmateApp,
    MenuUS11TrendTrading,
    MenuUS11WhatIsMargin,
    MenuUS11TradingPsychologyGuide
)


class MenuSection(BasePage):

    @allure.step(f"{datetime.now()}.   Click 'Education' menu section.")
    def menu_education_move_focus(self, d, test_language):
        menu1 = None
        match test_language:
            case "ar": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_AR_LEARN_TO_TRADE)  # not Glossary
            case "bg": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_BG_LEARN_TO_TRADE)
            case "cn": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_CN_LEARN_TO_TRADE)  # not Glossary
            case "cs": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_CS_LEARN_TO_TRADE)
            case "da": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_DA_LEARN_TO_TRADE)
            case "de": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_DE_LEARN_TO_TRADE)
            case "el": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_EL_LEARN_TO_TRADE)
            case "": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_EN_LEARN_TO_TRADE)
            case "es": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_ES_LEARN_TO_TRADE)
            case "et": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_ET_LEARN_TO_TRADE)
            case "fi": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_FI_LEARN_TO_TRADE)
            case "fr": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_FR_LEARN_TO_TRADE)
            case "hr": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_HR_LEARN_TO_TRADE)
            case "hu": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_HU_LEARN_TO_TRADE)
            case "id": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_ID_LEARN_TO_TRADE)  # not Education
            case "it": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_IT_LEARN_TO_TRADE)
            case "lt": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_LT_LEARN_TO_TRADE)
            case "lv": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_LV_LEARN_TO_TRADE)
            case "nl": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_NL_LEARN_TO_TRADE)
            case "pl": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_PL_LEARN_TO_TRADE)
            case "pt": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_PT_LEARN_TO_TRADE)
            case "ro": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_RO_LEARN_TO_TRADE)
            case "ru": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_RU_LEARN_TO_TRADE)
            case "sk": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_SK_LEARN_TO_TRADE)
            case "sl": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_SL_LEARN_TO_TRADE)
            case "sv": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_SV_LEARN_TO_TRADE)
            case "zh": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_ZH_LEARN_TO_TRADE)
            case "th": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_TH_LEARN_TO_TRADE)  # not Education
            case "vi": menu1 = d.find_elements(*MenuUS11Education.SUB_MENU_VI_LEARN_TO_TRADE)  # not Glossary

        if len(menu1) == 0:
            pytest.skip(f"For '{test_language}' language menu [Education] not present")

        ActionChains(d)\
            .move_to_element(menu1[0])\
            .perform()
        del menu1

        print(f"\n\n{datetime.now()}   => Education menu focus moved")

    @allure.step(f"{datetime.now()}.   Click 'learning hub' menu section.")
    def sub_menu_learning_hub_move_focus_click(self, d, test_language):
        menu2 = None
        match test_language:
            case "ar": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_AR_ITEM_LEARNING_HUB)
            case "bg": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_BG_ITEM_LEARNING_HUB)
            case "cn": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CN_ITEM_LEARNING_HUB)
            case "cs": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CS_ITEM_LEARNING_HUB)
            case "da": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DA_ITEM_LEARNING_HUB)
            case "de": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DE_ITEM_LEARNING_HUB)
            case "el": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EL_ITEM_LEARNING_HUB)
            case "": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EN_ITEM_LEARNING_HUB)
            case "es": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ES_ITEM_LEARNING_HUB)
            case "et": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ET_ITEM_LEARNING_HUB)
            case "fi": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FI_ITEM_LEARNING_HUB)
            case "fr": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FR_ITEM_LEARNING_HUB)
            case "hr": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HR_ITEM_LEARNING_HUB)
            case "hu": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HU_ITEM_LEARNING_HUB)
            case "id": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ID_ITEM_LEARNING_HUB)  # not Education
            case "it": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_IT_ITEM_LEARNING_HUB)
            case "lt": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_LT_ITEM_LEARNING_HUB)
            case "lv": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_LV_ITEM_LEARNING_HUB)
            case "nl": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_NL_ITEM_LEARNING_HUB)
            case "pl": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PL_ITEM_LEARNING_HUB)
            case "pt": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PT_ITEM_LEARNING_HUB)
            case "ro": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RO_ITEM_LEARNING_HUB)
            case "ru": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RU_ITEM_LEARNING_HUB)
            case "sk": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SK_ITEM_LEARNING_HUB)
            case "sl": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SL_ITEM_LEARNING_HUB)
            case "sv": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SV_ITEM_LEARNING_HUB)
            case "zh": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ZH_ITEM_LEARNING_HUB)
            case "th": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_TH_ITEM_LEARNING_HUB)  # not Education
            case "vi": menu2 = d.find_elements(*MenuUS11LearningHub.SUB_MENU_VI_ITEM_LEARNING_HUB)

        if len(menu2) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Learning hub\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(menu2[0]) \
            .click() \
            .perform()
        del menu2

        # ActionChains(d) \
        #     .pause(1) \
        #     .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Glossary' hyperlink.")
    def sub_menu_glossary_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_EN_GLOSSARY)
            case "ar": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_AR_GLOSSARY)
            case "id": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_ID_GLOSSARY)
            case "bg": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_BG_GLOSSARY)
            case "cn": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_CN_GLOSSARY)
            case "cs": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_CS_GLOSSARY)
            case "da": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_DA_GLOSSARY)
            case "de": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_DE_GLOSSARY)
            case "el": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_EL_GLOSSARY)
            case "es": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_ES_GLOSSARY)
            case "et": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_ET_GLOSSARY)
            case "fi": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_FI_GLOSSARY)
            case "fr": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_FR_GLOSSARY)
            case "hr": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_HR_GLOSSARY)
            case "hu": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_HU_GLOSSARY)
            case "it": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_IT_GLOSSARY)
            case "lt": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_LT_GLOSSARY)
            case "lv": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_LV_GLOSSARY)
            case "nl": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_NL_GLOSSARY)
            case "pl": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_PL_GLOSSARY)
            case "pt": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_PT_GLOSSARY)
            case "ro": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_RO_GLOSSARY)
            case "ru": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_RU_GLOSSARY)
            case "sk": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_SK_GLOSSARY)
            case "sl": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_SL_GLOSSARY)
            case "sv": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_SV_GLOSSARY)
            case "th": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_TH_GLOSSARY)
            case "vi": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_VI_GLOSSARY)
            case "zh": menu1 = d.find_elements(*MenuUS11Glossary.SUB_MENU_ZH_GLOSSARY)

        if len(menu1) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Glossary of trading terms\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Glossary sub-menu clicked")

        del menu1
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Forex trading' submenu.")
    def sub_menu_forex_trading_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EN_FOREX_TRADING)
            case "ar": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_AR_FOREX_TRADING)
            case "id": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ID_FOREX_TRADING)
            case "bg": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_BG_FOREX_TRADING)
            case "cn": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CN_FOREX_TRADING)  # одна страница
            case "cs": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CS_FOREX_TRADING)
            case "da": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DA_FOREX_TRADING)
            case "de": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DE_FOREX_TRADING)
            case "el": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EL_FOREX_TRADING)
            case "es": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ES_FOREX_TRADING)
            case "et": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ET_FOREX_TRADING)
            case "fi": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FI_FOREX_TRADING)
            case "fr": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FR_FOREX_TRADING)  # одна страница
            case "hr": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_HR_FOREX_TRADING)
            case "hu": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_HU_FOREX_TRADING)
            case "it": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_IT_FOREX_TRADING)
            case "lt": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_LT_FOREX_TRADING)
            case "lv": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_LV_FOREX_TRADING)
            case "nl": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_NL_FOREX_TRADING)
            case "pl": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_PL_FOREX_TRADING)
            case "pt": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_PT_FOREX_TRADING)
            case "ro": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RO_FOREX_TRADING)
            case "ru": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RU_FOREX_TRADING)  # одна страница
            case "sk": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SK_FOREX_TRADING)
            case "sl": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SL_FOREX_TRADING)
            case "sv": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SV_FOREX_TRADING)
            # для th Контекст есть, но нет подпункта меню
            case "th": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_TH_FOREX_TRADING)
            case "vi": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_VI_FOREX_TRADING)  # одна страница
            case "zh": menu1 = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ZH_FOREX_TRADING)  # одна страница

        if len(menu1) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Forex Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Forex trading sub-menu clicked")
        # time.sleep(1)
        del menu1
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Basics_of_trading' hyperlink.")
    def sub_menu_basics_of_trading_move_focus_click(self, d, test_language):
        menu2 = None
        match test_language:
            case "": menu2 = d.find_element(*Menu1101.SUB_MENU_EN_ITEM_BASICS_OF_TRADING)
            case "de": menu2 = d.find_element(*Menu1101.SUB_MENU_DE_ITEM_BASICS_OF_TRADING)
            case "ru": menu2 = d.find_element(*Menu1101.SUB_MENU_RU_ITEM_BASICS_OF_TRADING)
            case "bg": menu2 = d.find_element(*Menu1101.SUB_MENU_BG_ITEM_BASICS_OF_TRADING)
            case "cs": menu2 = d.find_element(*Menu1101.SUB_MENU_CS_ITEM_BASICS_OF_TRADING)
            case "fr": menu2 = d.find_element(*Menu1101.SUB_MENU_FR_ITEM_BASICS_OF_TRADING)
            case "ar": menu2 = d.find_element(*Menu1101.SUB_MENU_AR_ITEM_BASICS_OF_TRADING)
            case "et": menu2 = d.find_element(*Menu1101.SUB_MENU_ET_ITEM_BASICS_OF_TRADING)
            case "da": menu2 = d.find_element(*Menu1101.SUB_MENU_DA_ITEM_BASICS_OF_TRADING)
            case "el": menu2 = d.find_element(*Menu1101.SUB_MENU_EL_ITEM_BASICS_OF_TRADING)
            case "es": menu2 = d.find_element(*Menu1101.SUB_MENU_ES_ITEM_BASICS_OF_TRADING)
            case "hr": menu2 = d.find_element(*Menu1101.SUB_MENU_HR_ITEM_BASICS_OF_TRADING)
            case "it": menu2 = d.find_element(*Menu1101.SUB_MENU_IT_ITEM_BASICS_OF_TRADING)
            case "lv": menu2 = d.find_element(*Menu1101.SUB_MENU_LV_ITEM_BASICS_OF_TRADING)
            case "hu": menu2 = d.find_element(*Menu1101.SUB_MENU_HU_ITEM_BASICS_OF_TRADING)
            case "nl": menu2 = d.find_element(*Menu1101.SUB_MENU_NL_ITEM_BASICS_OF_TRADING)
            case "pl": menu2 = d.find_element(*Menu1101.SUB_MENU_PL_ITEM_BASICS_OF_TRADING)
            case "pt": menu2 = d.find_element(*Menu1101.SUB_MENU_PT_ITEM_BASICS_OF_TRADING)
            case "ro": menu2 = d.find_element(*Menu1101.SUB_MENU_RO_ITEM_BASICS_OF_TRADING)
            case "sk": menu2 = d.find_element(*Menu1101.SUB_MENU_SK_ITEM_BASICS_OF_TRADING)
            case "sl": menu2 = d.find_element(*Menu1101.SUB_MENU_SL_ITEM_BASICS_OF_TRADING)
            case "fi": menu2 = d.find_element(*Menu1101.SUB_MENU_FI_ITEM_BASICS_OF_TRADING)
            case "sv": menu2 = d.find_element(*Menu1101.SUB_MENU_SV_ITEM_BASICS_OF_TRADING)
            case "vi": menu2 = d.find_element(*Menu1101.SUB_MENU_VI_ITEM_BASICS_OF_TRADING)
            case "zh": menu2 = d.find_element(*Menu1101.SUB_MENU_ZH_ITEM_BASICS_OF_TRADING)
            case "lt": menu2 = d.find_element(*Menu1101.SUB_MENU_LT_ITEM_BASICS_OF_TRADING)
            case "cn": menu2 = d.find_element(*Menu1101.SUB_MENU_CN_ITEM_BASICS_OF_TRADING)
            # case "id": menu2 = d.find_element(*Menu1101.SUB_MENU_ID_ITEM_BASICS_OF_TRADING)
            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education > Menu item [The basics of trading]\" "
                                f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(menu2) \
            .click() \
            .perform()
        ActionChains(d) \
            .pause(1) \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading courses hyperlink.")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        menu2 = None
        match test_language:
            case "": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "bg": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_BG_ITEM_TRADING_COURSES)
            case "cs": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CS_ITEM_TRADING_COURSES)
            case "fr": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "et": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ET_ITEM_TRADING_COURSES)
            case "da": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DA_ITEM_TRADING_COURSES)
            case "el": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "hr": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HR_ITEM_TRADING_COURSES)
            case "it": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "lv": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LV_ITEM_TRADING_COURSES)
            case "hu": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "pt": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PT_ITEM_TRADING_COURSES)
            case "ro": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "sk": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SK_ITEM_TRADING_COURSES)
            case "sl": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SL_ITEM_TRADING_COURSES)
            case "fi": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FI_ITEM_TRADING_COURSES)
            case "sv": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SV_ITEM_TRADING_COURSES)
            case "vi": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_VI_ITEM_TRADING_COURSES)
            case "zh": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "lt": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LT_ITEM_TRADING_COURSES)
            case "cn": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)
            case "id": menu2 = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ID_ITEM_TRADING_COURSES)
            case _: pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
                                f"doesn't exist on production")

        if len(menu2) == 0:
            # pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
            #             f"doesn't exist on production")
            pytest.exit(f"For '{test_language}' language [Trading courses] submenu item "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(menu2[0]) \
            .click() \
            .perform()
        ActionChains(d) \
            .pause(1) \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Commodities trading' hyperlink.")
    def sub_menu_commodities_trading_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "ar": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_AR_COMMODITIES_TRADING)
            # case "bg":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_BG_COMMODITIES_TRADING) # Нет такой страницы
            # case "cs":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CS_COMMODITIES_TRADING) # Нет такой страницы
            case "cn": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CN_COMMODITIES_TRADING)
            # case "da":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DA_COMMODITIES_TRADING) # Нет такой страницы
            case "de": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DE_COMMODITIES_TRADING)
            # case "el":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EL_COMMODITIES_TRADING) # Нет такой страницы
            case "": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EN_COMMODITIES_TRADING)
            case "es": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ES_COMMODITIES_TRADING)
            # case "et":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ET_COMMODITIES_TRADING) # Нет такой страницы
            # case "fi":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FI_COMMODITIES_TRADING) # Нет такой страницы
            case "fr": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FR_COMMODITIES_TRADING)
            # case "hr":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HR_COMMODITIES_TRADING) # Нет такой страницы
            # case "hu":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HU_COMMODITIES_TRADING) # Нет такой страницы
            # case "id":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ID_COMMODITIES_TRADING) # Нет такой страницы
            case "it": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_IT_COMMODITIES_TRADING)
            # case "lt":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LT_COMMODITIES_TRADING) # Нет такой страницы
            # case "lv":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LV_COMMODITIES_TRADING) # Нет такой страницы
            case "nl": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_NL_COMMODITIES_TRADING)
            case "pl": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PL_COMMODITIES_TRADING)
            # case "pt":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PT_COMMODITIES_TRADING) # Нет такой страницы
            case "ro": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_RO_COMMODITIES_TRADING)
            case "ru": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_RU_COMMODITIES_TRADING)
            # case "sk":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SK_COMMODITIES_TRADING) # Нет такой страницы
            # case "sl":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SL_COMMODITIES_TRADING) # Нет такой страницы
            # case "sv":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SV_COMMODITIES_TRADING) # Нет такой страницы
            case "zh": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ZH_COMMODITIES_TRADING)
            # case "th":
            # menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_TH_COMMODITIES_TRADING)  # Нет такой страницы
            case "vi": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_VI_COMMODITIES_TRADING)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->Commodities Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Market guides hyperlink.")
    def sub_menu_market_guides_move_focus_click(self, d, test_language):
        menu2 = None
        match test_language:
            case "": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_EN_ITEM_MARKET_GUIDES)
            case "de": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_DE_ITEM_MARKET_GUIDES)
            case "ru": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_RU_ITEM_MARKET_GUIDES)
            case "bg": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_BG_ITEM_MARKET_GUIDES)
            case "cs": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_CS_ITEM_MARKET_GUIDES)
            case "fr": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_FR_ITEM_MARKET_GUIDES)
            case "ar": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_AR_ITEM_MARKET_GUIDES)
            case "et": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_ET_ITEM_MARKET_GUIDES)
            case "da": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_DA_ITEM_MARKET_GUIDES)
            case "el": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_EL_ITEM_MARKET_GUIDES)
            case "es": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_ES_ITEM_MARKET_GUIDES)
            case "hr": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_HR_ITEM_MARKET_GUIDES)
            case "it": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_IT_ITEM_MARKET_GUIDES)
            case "lv": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_LV_ITEM_MARKET_GUIDES)
            case "hu": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_HU_ITEM_MARKET_GUIDES)
            case "nl": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_NL_ITEM_MARKET_GUIDES)
            case "pl": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_PL_ITEM_MARKET_GUIDES)
            case "pt": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_PT_ITEM_MARKET_GUIDES)
            case "ro": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_RO_ITEM_MARKET_GUIDES)
            case "sk": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_SK_ITEM_MARKET_GUIDES)
            case "sl": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_SL_ITEM_MARKET_GUIDES)
            case "fi": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_FI_ITEM_MARKET_GUIDES)
            case "sv": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_SV_ITEM_MARKET_GUIDES)
            case "vi": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_VI_ITEM_MARKET_GUIDES)
            case "zh": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_ZH_ITEM_MARKET_GUIDES)
            case "lt": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_LT_ITEM_MARKET_GUIDES)
            case "cn": menu2 = d.find_element(*MenuUS11MarketGuides.SUB_MENU_CN_ITEM_MARKET_GUIDES)
            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education > Menu title [Market Guides]\" doesn't exist on production")
        ActionChains(d) \
            .move_to_element(menu2) \
            .click() \
            .perform()
        ActionChains(d) \
            .pause(1) \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Cryptocurrency trading' hyperlink.")
    def sub_menu_cryptocurrency_trading_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            # case "ar":  menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_AR_CRYPTOCURRENCY_TRADING)
            # case "bg": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_BG_CRYPTOCURRENCY_TRADING)
            # case "cs": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_CS_CRYPTOCURRENCY_TRADING)
            case "cn": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_CN_CRYPTOCURRENCY_TRADING)
            # case "da": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_DA_CRYPTOCURRENCY_TRADING)
            case "de": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_DE_CRYPTOCURRENCY_TRADING)
            # case "el": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_EL_CRYPTOCURRENCY_TRADING)
            case "": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_EN_CRYPTOCURRENCY_TRADING)
            case "es": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_ES_CRYPTOCURRENCY_TRADING)
            # case "et": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_ET_CRYPTOCURRENCY_TRADING)
            # case "fi": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_FI_CRYPTOCURRENCY_TRADING)
            case "fr": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_FR_CRYPTOCURRENCY_TRADING)
            # case "hr": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_HR_CRYPTOCURRENCY_TRADING)
            # case "hu": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_HU_CRYPTOCURRENCY_TRADING)
            case "it": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_IT_CRYPTOCURRENCY_TRADING)
            # case "id": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_ID_CRYPTOCURRENCY_TRADING)
            # case "lt": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_LT_CRYPTOCURRENCY_TRADING)
            # case "lv": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_LV_CRYPTOCURRENCY_TRADING)
            # case "nl":  menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_NL_CRYPTOCURRENCY_TRADING)
            case "pl": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_PL_CRYPTOCURRENCY_TRADING)
            # case "pt": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_PT_CRYPTOCURRENCY_TRADING)
            case "ro": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_RO_CRYPTOCURRENCY_TRADING)
            case "ru": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_RU_CRYPTOCURRENCY_TRADING)
            # case "sk": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_SK_CRYPTOCURRENCY_TRADING)
            # case "sl": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_SL_CRYPTOCURRENCY_TRADING)
            # case "sv": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_SV_CRYPTOCURRENCY_TRADING)
            # case "th": \
            # menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_TH_CRYPTOCURRENCY_TRADING)
            case "vi": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_VI_CRYPTOCURRENCY_TRADING)
            case "zh": menu1 = d.find_element(*MenuUS11CryptocurrencyTrading.SUB_MENU_ZH_CRYPTOCURRENCY_TRADING)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->Cryptocurrency trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'CFD trading guide' hyperlink.")
    def sub_menu_cfd_trading_guide_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            # case "ar":  menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_AR_CFD_TRADING_GUIDE)
            case "bg": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_BG_CFD_TRADING_GUIDE)
            # case "cn": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_CN_CFD_TRADING_GUIDE)
            case "cs": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_CS_CFD_TRADING_GUIDE)
            # case "da": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_DA_CFD_TRADING_GUIDE)
            case "de": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_DE_CFD_TRADING_GUIDE)
            # case "el": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_EL_CFD_TRADING_GUIDE)
            case "": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_EN_CFD_TRADING_GUIDE)
            case "es": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_ES_CFD_TRADING_GUIDE)
            # case "et": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_ET_CFD_TRADING_GUIDE)
            # case "fi": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_FI_CFD_TRADING_GUIDE)
            case "fr": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_FR_CFD_TRADING_GUIDE)
            # case "hr": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_HR_CFD_TRADING_GUIDE)
            # case "hu": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_HU_CFD_TRADING_GUIDE)
            # case "id": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_ID_CFD_TRADING_GUIDE)
            case "it": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_IT_CFD_TRADING_GUIDE)
            # case "lt": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_LT_CFD_TRADING_GUIDE)
            # case "lv": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_LV_CFD_TRADING_GUIDE)
            case "nl": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_NL_CFD_TRADING_GUIDE)
            case "pl": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_PL_CFD_TRADING_GUIDE)
            # case "pt": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_PT_CFD_TRADING_GUIDE)
            case "ro": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_RO_CFD_TRADING_GUIDE)
            case "ru": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_RU_CFD_TRADING_GUIDE)
            # case "sk": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_SK_CFD_TRADING_GUIDE)
            # case "sl": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_SL_CFD_TRADING_GUIDE)
            case "sv": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_SV_CFD_TRADING_GUIDE)
            # case "th": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_TH_CFD_TRADING_GUIDE)
            case "vi": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_VI_CFD_TRADING_GUIDE)
            case "zh": menu1 = d.find_element(*MenuUS11CFDTradingGuide.SUB_MENU_ZH_CFD_TRADING_GUIDE)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->CFD trading guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Spread betting guide' hyperlink.")
    def sub_menu_spread_betting_guide_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "": menu1 = d.find_element(*MenuUS11SpreadBettingGuide.SUB_MENU_EN_SPREAD_BETTING_GUIDE)
            case "es": menu1 = d.find_element(*MenuUS11SpreadBettingGuide.SUB_MENU_ES_SPREAD_BETTING_GUIDE)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->Spread betting guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'ETF trading' hyperlink.")
    def sub_menu_etf_trading_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "ar": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_AR_ETF_TRADING)
            # case "bg": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_BG_ETF_TRADING)
            # case "cs": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_CS_ETF_TRADING)
            case "cn": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_CN_ETF_TRADING)
            # case "da": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_DA_ETF_TRADING)
            case "de": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_DE_ETF_TRADING)
            # case "el": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_EL_ETF_TRADING)
            case "": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_EN_ETF_TRADING)
            case "es": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_ES_ETF_TRADING)
            # case "et": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_ET_ETF_TRADING)
            # case "fi": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_FI_ETF_TRADING)
            # case "fr": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_FR_ETF_TRADING)
            # case "hr": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_HR_ETF_TRADING)
            # case "hu": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_HU_ETF_TRADING)
            case "it": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_IT_ETF_TRADING)
            # case "id": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_ID_ETF_TRADING)
            # case "lt": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_LT_ETF_TRADING)
            # case "lv": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_LV_ETF_TRADING)
            # case "nl": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_NL_ETF_TRADING)
            # case "pl": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_PL_ETF_TRADING)
            # case "pt": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_PT_ETF_TRADING)
            # case "ro": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_RO_ETF_TRADING)
            case "ru": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_RU_ETF_TRADING)
            # case "sk": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_SK_ETF_TRADING)
            # case "sl": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_SL_ETF_TRADING)
            # case "sv": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_SV_ETF_TRADING)
            # case "th": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_TH_ETF_TRADING)
            case "vi": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_VI_ETF_TRADING)
            # case "zh": menu1 = d.find_element(*MenuUS11ETFTrading.SUB_MENU_ZH_ETF_TRADING)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->ETF trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(menu1) \
            .click() \
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Strategies Guide' hyperlink.")
    def sub_menu_trading_strategies_guide_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EN_TRADING_STRATEGIES_GUIDE)
            case "ar": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_AR_TRADING_STRATEGIES_GUIDE)
            case "bg": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_BG_TRADING_STRATEGIES_GUIDE)
            case "cn": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CN_TRADING_STRATEGIES_GUIDE)
            case "cs": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CS_TRADING_STRATEGIES_GUIDE)
            case "da": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DA_TRADING_STRATEGIES_GUIDE)
            case "de": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DE_TRADING_STRATEGIES_GUIDE)
            case "el": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EL_TRADING_STRATEGIES_GUIDE)
            case "es": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ES_TRADING_STRATEGIES_GUIDE)
            case "et": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ET_TRADING_STRATEGIES_GUIDE)
            case "fi": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FI_TRADING_STRATEGIES_GUIDE)
            case "fr": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FR_TRADING_STRATEGIES_GUIDE)
            case "hr": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HR_TRADING_STRATEGIES_GUIDE)
            case "hu": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HU_TRADING_STRATEGIES_GUIDE)
            case "id": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ID_TRADING_STRATEGIES_GUIDE)
            case "it": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_IT_TRADING_STRATEGIES_GUIDE)
            case "lt": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LT_TRADING_STRATEGIES_GUIDE)
            case "lv": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LV_TRADING_STRATEGIES_GUIDE)
            case "nl": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_NL_TRADING_STRATEGIES_GUIDE)
            case "pl": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PL_TRADING_STRATEGIES_GUIDE)
            case "pt": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PT_TRADING_STRATEGIES_GUIDE)
            case "ro": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RO_TRADING_STRATEGIES_GUIDE)
            case "ru": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RU_TRADING_STRATEGIES_GUIDE)
            case "sk": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SK_TRADING_STRATEGIES_GUIDE)
            case "sl": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SL_TRADING_STRATEGIES_GUIDE)
            case "sv": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SV_TRADING_STRATEGIES_GUIDE)
            case "zh": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ZH_TRADING_STRATEGIES_GUIDE)
            case "th": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_TH_TRADING_STRATEGIES_GUIDE)
            case "vi": menu1 = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_VI_TRADING_STRATEGIES_GUIDE)

        if len(menu1) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Strategies Guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1[0])\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Day Trading' hyperlink.")
    def sub_menu_day_trading_move_focus_click(self, d, test_language):
        match test_language:
            case "de":
                menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_DE_DAY_TRADING)
            case "es":
                menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ES_DAY_TRADING)
            case _:
                menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ALL_DAY_TRADING)

        if len(menu) > 0:
            ActionChains(d) \
                .move_to_element(menu[0]) \
                .click() \
                .perform()
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Day Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Indices Trading' hyperlink.")
    def sub_menu_indices_trading_move_focus_click(self, d, test_language):
        match test_language:
            case "id":
                menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ID_INDICES_TRADING)
            case "de":
                menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_DE_INDICES_TRADING)
            case "ru":
                menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_RU_INDICES_TRADING)
            case _:
                menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ALL_INDICES_TRADING)

        if len(menu) > 0:
            ActionChains(d) \
                .move_to_element(menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Indices Trading menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Indices Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Investmate app' hyperlink.")
    def sub_menu_investmate_app_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            # case "ar": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_AR_INVESTMATE_APP)
            # case "bg": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_BG_INVESTMATE_APP)
            # case "cs": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_CS_INVESTMATE_APP)
            case "cn": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_CN_INVESTMATE_APP)
            # case "da": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_DA_INVESTMATE_APP)
            case "de": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_DE_INVESTMATE_APP)
            case "el": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_EL_INVESTMATE_APP)
            case "": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_EN_INVESTMATE_APP)
            case "es": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_ES_INVESTMATE_APP)
            # case "et": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_ET_INVESTMATE_APP)
            # case "fi": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_FI_INVESTMATE_APP)
            case "fr": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_FR_INVESTMATE_APP)
            # case "hr": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_HR_INVESTMATE_APP)
            # case "hu": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_HU_INVESTMATE_APP)
            case "it": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_IT_INVESTMATE_APP)
            # case "id": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_ID_INVESTMATE_APP)
            # case "lt": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_LT_INVESTMATE_APP)
            # case "lv": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_LV_INVESTMATE_APP)
            case "nl": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_NL_INVESTMATE_APP)
            case "pl": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_PL_INVESTMATE_APP)
            case "pt": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_PT_INVESTMATE_APP)
            case "ro": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_RO_INVESTMATE_APP)
            case "ru": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_RU_INVESTMATE_APP)
            # case "sk": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_SK_INVESTMATE_APP)
            # case "sl": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_SL_INVESTMATE_APP)
            # case "sv": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_SV_INVESTMATE_APP)
            # case "th": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_TH_INVESTMATE_APP)
            case "vi": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_VI_INVESTMATE_APP)
            case "zh": menu1 = d.find_element(*MenuUS11InvestmateApp.SUB_MENU_ZH_INVESTMATE_APP)

            case _: pytest.skip(f"For test language '{test_language}' "
                                f"the page \"Education->Investmate app\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(menu1) \
            .click() \
            .perform()

        time.sleep(1)
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trend Trading' menu item.")
    def sub_menu_trend_trading_move_focus_click(self, d, test_language):
        menu1 = None
        match test_language:
            case "": menu1 = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_EN_ITEM_TREND_TRADING)
            # case "de": menu1 = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_DE_ITEM_TREND_TRADING)
            case _: pytest.skip(f"For '{test_language}' language "
                                f"the page \"Education->Trend Trading\" doesn't exist on production")
        if len(menu1) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trend Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(menu1[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Trend trading menu item clicked")
        time.sleep(1)
        del menu1
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'What is a margin?' hyperlink.")
    def sub_menu_what_is_a_margin_move_focus_click(self, d, test_language):
        menu = d.find_elements(*MenuUS11WhatIsMargin.SUB_MENU_ALL_WHAT_IS_A_MARGIN)
        if len(menu) > 0:
            ActionChains(d) \
                .move_to_element(menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'What is a margin?' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->What is a margin?\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Psychology Guide' hyperlink.")
    def sub_menu_trading_psychology_guide_move_focus_click(self, d, test_language):
        menu = None
        match test_language:
            case "": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ALL_TRADING_PSYCHOLOGY_GUIDE)
            case "ar": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_AR_TRADING_PSYCHOLOGY_GUIDE)
            case "de": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_DE_TRADING_PSYCHOLOGY_GUIDE)
            case "el": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_EL_TRADING_PSYCHOLOGY_GUIDE)
            case "es": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ES_TRADING_PSYCHOLOGY_GUIDE)
            case "fr": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_FR_TRADING_PSYCHOLOGY_GUIDE)
            case "it": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_IT_TRADING_PSYCHOLOGY_GUIDE)
            case "hu": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_HU_TRADING_PSYCHOLOGY_GUIDE)
            case "nl": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_NL_TRADING_PSYCHOLOGY_GUIDE)
            case "pl": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_PL_TRADING_PSYCHOLOGY_GUIDE)
            case "ro": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RO_TRADING_PSYCHOLOGY_GUIDE)
            case "ru": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RU_TRADING_PSYCHOLOGY_GUIDE)
            case "zh": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ZH_TRADING_PSYCHOLOGY_GUIDE)
            case "cn": menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_CN_TRADING_PSYCHOLOGY_GUIDE)
        if len(menu) > 0:
            ActionChains(d) \
                .move_to_element(menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Trading Psychology Guide menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Psychology Guide\" doesn't exist on production")
        return d.current_url
