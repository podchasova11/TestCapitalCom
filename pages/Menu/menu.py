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
    MenuUS11TradingPsychologyGuide, MenuUS11PositionTrading, MenuUS11SwingTrading, MenuUS11ScalpTrading
)


class MenuSection(BasePage):

    @allure.step(f"{datetime.now()}.   Click 'Education' menu section.")
    def menu_education_move_focus(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_AR_LEARN_TO_TRADE)  # not Glossary
            case "bg": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_BG_LEARN_TO_TRADE)
            case "cn": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_CN_LEARN_TO_TRADE)  # not Glossary
            case "cs": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_CS_LEARN_TO_TRADE)
            case "da": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_DA_LEARN_TO_TRADE)
            case "de": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_DE_LEARN_TO_TRADE)
            case "el": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_EL_LEARN_TO_TRADE)
            case "": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_EN_LEARN_TO_TRADE)
            case "es": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_ES_LEARN_TO_TRADE)
            case "et": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_ET_LEARN_TO_TRADE)
            case "fi": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_FI_LEARN_TO_TRADE)
            case "fr": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_FR_LEARN_TO_TRADE)
            case "hr": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_HR_LEARN_TO_TRADE)
            case "hu": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_HU_LEARN_TO_TRADE)
            case "id": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_ID_LEARN_TO_TRADE)  # not Education
            case "it": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_IT_LEARN_TO_TRADE)
            case "lt": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_LT_LEARN_TO_TRADE)
            case "lv": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_LV_LEARN_TO_TRADE)
            case "nl": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_NL_LEARN_TO_TRADE)
            case "pl": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_PL_LEARN_TO_TRADE)
            case "pt": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_PT_LEARN_TO_TRADE)
            case "ro": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_RO_LEARN_TO_TRADE)
            case "ru": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_RU_LEARN_TO_TRADE)
            case "sk": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_SK_LEARN_TO_TRADE)
            case "sl": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_SL_LEARN_TO_TRADE)
            case "sv": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_SV_LEARN_TO_TRADE)
            case "zh": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_ZH_LEARN_TO_TRADE)
            case "th": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_TH_LEARN_TO_TRADE)  # not Education
            case "vi": sub_menu = d.find_elements(*MenuUS11Education.SUB_MENU_VI_LEARN_TO_TRADE)  # not Glossary

        if len(sub_menu) == 0:
            pytest.skip(f"For '{test_language}' language menu [Education] not present")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .perform()
        del sub_menu

        print(f"\n\n{datetime.now()}   => Education menu focus moved")

    @allure.step(f"{datetime.now()}.   Click 'learning hub' menu section.")
    def sub_menu_learning_hub_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_AR_ITEM_LEARNING_HUB)
            case "bg": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_BG_ITEM_LEARNING_HUB)
            case "cn": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CN_ITEM_LEARNING_HUB)
            case "cs": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_CS_ITEM_LEARNING_HUB)
            case "da": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DA_ITEM_LEARNING_HUB)
            case "de": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_DE_ITEM_LEARNING_HUB)
            case "el": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EL_ITEM_LEARNING_HUB)
            case "": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_EN_ITEM_LEARNING_HUB)
            case "es": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ES_ITEM_LEARNING_HUB)
            case "et": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ET_ITEM_LEARNING_HUB)
            case "fi": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FI_ITEM_LEARNING_HUB)
            case "fr": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_FR_ITEM_LEARNING_HUB)
            case "hr": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HR_ITEM_LEARNING_HUB)
            case "hu": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_HU_ITEM_LEARNING_HUB)
            case "id": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ID_ITEM_LEARNING_HUB)  # not Education
            case "it": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_IT_ITEM_LEARNING_HUB)
            case "lt": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_LT_ITEM_LEARNING_HUB)
            case "lv": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_LV_ITEM_LEARNING_HUB)
            case "nl": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_NL_ITEM_LEARNING_HUB)
            case "pl": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PL_ITEM_LEARNING_HUB)
            case "pt": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_PT_ITEM_LEARNING_HUB)
            case "ro": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RO_ITEM_LEARNING_HUB)
            case "ru": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_RU_ITEM_LEARNING_HUB)
            case "sk": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SK_ITEM_LEARNING_HUB)
            case "sl": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SL_ITEM_LEARNING_HUB)
            case "sv": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_SV_ITEM_LEARNING_HUB)
            case "zh": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_ZH_ITEM_LEARNING_HUB)
            case "th": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_TH_ITEM_LEARNING_HUB)  # not Education
            case "vi": sub_menu = d.find_elements(*MenuUS11LearningHub.SUB_MENU_VI_ITEM_LEARNING_HUB)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Learning hub\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()
        del sub_menu

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Glossary' hyperlink.")
    def sub_menu_glossary_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EN_GLOSSARY)
            case "ar": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_AR_GLOSSARY)
            case "id": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ID_GLOSSARY)
            case "bg": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_BG_GLOSSARY)
            case "cn": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_CN_GLOSSARY)
            case "cs": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_CS_GLOSSARY)
            case "da": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_DA_GLOSSARY)
            case "de": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_DE_GLOSSARY)
            case "el": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_EL_GLOSSARY)
            case "es": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ES_GLOSSARY)
            case "et": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ET_GLOSSARY)
            case "fi": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_FI_GLOSSARY)
            case "fr": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_FR_GLOSSARY)
            case "hr": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HR_GLOSSARY)
            case "hu": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_HU_GLOSSARY)
            case "it": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_IT_GLOSSARY)
            case "lt": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_LT_GLOSSARY)
            case "lv": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_LV_GLOSSARY)
            case "nl": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_NL_GLOSSARY)
            case "pl": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_PL_GLOSSARY)
            case "pt": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_PT_GLOSSARY)
            case "ro": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RO_GLOSSARY)
            case "ru": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_RU_GLOSSARY)
            case "sk": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SK_GLOSSARY)
            case "sl": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SL_GLOSSARY)
            case "sv": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_SV_GLOSSARY)
            case "th": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_TH_GLOSSARY)
            case "vi": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_VI_GLOSSARY)
            case "zh": sub_menu = d.find_elements(*MenuUS11Glossary.SUB_MENU_ZH_GLOSSARY)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Glossary of trading terms\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Glossary sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Forex trading' submenu.")
    def sub_menu_forex_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EN_FOREX_TRADING)
            case "ar": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_AR_FOREX_TRADING)
            case "id": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ID_FOREX_TRADING)
            case "bg": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_BG_FOREX_TRADING)
            case "cn": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CN_FOREX_TRADING)  # одна страница
            case "cs": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_CS_FOREX_TRADING)
            case "da": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DA_FOREX_TRADING)
            case "de": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_DE_FOREX_TRADING)
            case "el": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_EL_FOREX_TRADING)
            case "es": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ES_FOREX_TRADING)
            case "et": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ET_FOREX_TRADING)
            case "fi": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FI_FOREX_TRADING)
            case "fr": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_FR_FOREX_TRADING)  # одна страница
            case "hr": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_HR_FOREX_TRADING)
            case "hu": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_HU_FOREX_TRADING)
            case "it": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_IT_FOREX_TRADING)
            case "lt": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_LT_FOREX_TRADING)
            case "lv": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_LV_FOREX_TRADING)
            case "nl": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_NL_FOREX_TRADING)
            case "pl": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_PL_FOREX_TRADING)
            case "pt": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_PT_FOREX_TRADING)
            case "ro": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RO_FOREX_TRADING)
            case "ru": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_RU_FOREX_TRADING)  # одна страница
            case "sk": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SK_FOREX_TRADING)
            case "sl": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SL_FOREX_TRADING)
            case "sv": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_SV_FOREX_TRADING)
            # для th Контекст есть, но нет подпункта меню
            case "th": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_TH_FOREX_TRADING)
            case "vi": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_VI_FOREX_TRADING)  # одна страница
            case "zh": sub_menu = d.find_elements(*MenuUS11ForexTrading.SUB_MENU_ZH_FOREX_TRADING)  # одна страница

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Forex Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Forex trading sub-menu clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Basics_of_trading' hyperlink.")
    def sub_menu_basics_of_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*Menu1101.SUB_MENU_EN_ITEM_BASICS_OF_TRADING)
            case "de": sub_menu = d.find_elements(*Menu1101.SUB_MENU_DE_ITEM_BASICS_OF_TRADING)
            case "ru": sub_menu = d.find_elements(*Menu1101.SUB_MENU_RU_ITEM_BASICS_OF_TRADING)
            case "bg": sub_menu = d.find_elements(*Menu1101.SUB_MENU_BG_ITEM_BASICS_OF_TRADING)
            case "cs": sub_menu = d.find_elements(*Menu1101.SUB_MENU_CS_ITEM_BASICS_OF_TRADING)
            case "fr": sub_menu = d.find_elements(*Menu1101.SUB_MENU_FR_ITEM_BASICS_OF_TRADING)
            case "ar": sub_menu = d.find_elements(*Menu1101.SUB_MENU_AR_ITEM_BASICS_OF_TRADING)
            case "et": sub_menu = d.find_elements(*Menu1101.SUB_MENU_ET_ITEM_BASICS_OF_TRADING)
            case "da": sub_menu = d.find_elements(*Menu1101.SUB_MENU_DA_ITEM_BASICS_OF_TRADING)
            case "el": sub_menu = d.find_elements(*Menu1101.SUB_MENU_EL_ITEM_BASICS_OF_TRADING)
            case "es": sub_menu = d.find_elements(*Menu1101.SUB_MENU_ES_ITEM_BASICS_OF_TRADING)
            case "hr": sub_menu = d.find_elements(*Menu1101.SUB_MENU_HR_ITEM_BASICS_OF_TRADING)
            case "it": sub_menu = d.find_elements(*Menu1101.SUB_MENU_IT_ITEM_BASICS_OF_TRADING)
            case "lv": sub_menu = d.find_elements(*Menu1101.SUB_MENU_LV_ITEM_BASICS_OF_TRADING)
            case "hu": sub_menu = d.find_elements(*Menu1101.SUB_MENU_HU_ITEM_BASICS_OF_TRADING)
            case "nl": sub_menu = d.find_elements(*Menu1101.SUB_MENU_NL_ITEM_BASICS_OF_TRADING)
            case "pl": sub_menu = d.find_elements(*Menu1101.SUB_MENU_PL_ITEM_BASICS_OF_TRADING)
            case "pt": sub_menu = d.find_elements(*Menu1101.SUB_MENU_PT_ITEM_BASICS_OF_TRADING)
            case "ro": sub_menu = d.find_elements(*Menu1101.SUB_MENU_RO_ITEM_BASICS_OF_TRADING)
            case "sk": sub_menu = d.find_elements(*Menu1101.SUB_MENU_SK_ITEM_BASICS_OF_TRADING)
            case "sl": sub_menu = d.find_elements(*Menu1101.SUB_MENU_SL_ITEM_BASICS_OF_TRADING)
            case "fi": sub_menu = d.find_elements(*Menu1101.SUB_MENU_FI_ITEM_BASICS_OF_TRADING)
            case "sv": sub_menu = d.find_elements(*Menu1101.SUB_MENU_SV_ITEM_BASICS_OF_TRADING)
            case "vi": sub_menu = d.find_elements(*Menu1101.SUB_MENU_VI_ITEM_BASICS_OF_TRADING)
            case "zh": sub_menu = d.find_elements(*Menu1101.SUB_MENU_ZH_ITEM_BASICS_OF_TRADING)
            case "lt": sub_menu = d.find_elements(*Menu1101.SUB_MENU_LT_ITEM_BASICS_OF_TRADING)
            case "cn": sub_menu = d.find_elements(*Menu1101.SUB_MENU_CN_ITEM_BASICS_OF_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Menu item [The basics of trading]\" "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading courses hyperlink.")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "bg": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_BG_ITEM_TRADING_COURSES)
            case "cs": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CS_ITEM_TRADING_COURSES)
            case "fr": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "et": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ET_ITEM_TRADING_COURSES)
            case "da": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_DA_ITEM_TRADING_COURSES)
            case "el": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "hr": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HR_ITEM_TRADING_COURSES)
            case "it": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "lv": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LV_ITEM_TRADING_COURSES)
            case "hu": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "pt": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_PT_ITEM_TRADING_COURSES)
            case "ro": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "sk": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SK_ITEM_TRADING_COURSES)
            case "sl": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SL_ITEM_TRADING_COURSES)
            case "fi": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_FI_ITEM_TRADING_COURSES)
            case "sv": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_SV_ITEM_TRADING_COURSES)
            case "vi": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_VI_ITEM_TRADING_COURSES)
            case "zh": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "lt": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_LT_ITEM_TRADING_COURSES)
            case "cn": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)
            case "id": sub_menu = d.find_elements(*MenuUS11TradingCourses.SUB_MENU_ID_ITEM_TRADING_COURSES)

        if len(sub_menu) == 0:
            pytest.skip(f"For '{test_language}' language [Trading courses] submenu item "
                        f"doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Commodities trading' hyperlink.")
    def sub_menu_commodities_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_AR_COMMODITIES_TRADING)
            # case "bg":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_BG_COMMODITIES_TRADING) # Нет такой страницы
            # case "cs":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CS_COMMODITIES_TRADING) # Нет такой страницы
            case "cn": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_CN_COMMODITIES_TRADING)
            # case "da":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DA_COMMODITIES_TRADING) # Нет такой страницы
            case "de": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_DE_COMMODITIES_TRADING)
            # case "el":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EL_COMMODITIES_TRADING) # Нет такой страницы
            case "": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_EN_COMMODITIES_TRADING)
            case "es": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ES_COMMODITIES_TRADING)
            # case "et":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ET_COMMODITIES_TRADING) # Нет такой страницы
            # case "fi":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FI_COMMODITIES_TRADING) # Нет такой страницы
            case "fr": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_FR_COMMODITIES_TRADING)
            # case "hr":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HR_COMMODITIES_TRADING) # Нет такой страницы
            # case "hu":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HU_COMMODITIES_TRADING) # Нет такой страницы
            # case "id":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ID_COMMODITIES_TRADING) # Нет такой страницы
            case "it": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_IT_COMMODITIES_TRADING)
            # case "lt":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LT_COMMODITIES_TRADING) # Нет такой страницы
            # case "lv":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LV_COMMODITIES_TRADING) # Нет такой страницы
            case "nl": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_NL_COMMODITIES_TRADING)
            case "pl": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_PL_COMMODITIES_TRADING)
            # case "pt":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PT_COMMODITIES_TRADING) # Нет такой страницы
            case "ro": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RO_COMMODITIES_TRADING)
            case "ru": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_RU_COMMODITIES_TRADING)
            # case "sk":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SK_COMMODITIES_TRADING) # Нет такой страницы
            # case "sl":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SL_COMMODITIES_TRADING) # Нет такой страницы
            # case "sv":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SV_COMMODITIES_TRADING) # Нет такой страницы
            case "zh": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_ZH_COMMODITIES_TRADING)
            # case "th":
            # sub_menu = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_TH_COMMODITIES_TRADING)  # Нет такой страницы
            case "vi": sub_menu = d.find_elements(*MenuUS11CommoditiesTrading.SUB_MENU_VI_COMMODITIES_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Commodities Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Market guides hyperlink.")
    def sub_menu_market_guides_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EN_ITEM_MARKET_GUIDES)
            case "de": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_DE_ITEM_MARKET_GUIDES)
            case "ru": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RU_ITEM_MARKET_GUIDES)
            case "bg": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_BG_ITEM_MARKET_GUIDES)
            case "cs": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_CS_ITEM_MARKET_GUIDES)
            case "fr": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_FR_ITEM_MARKET_GUIDES)
            case "ar": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_AR_ITEM_MARKET_GUIDES)
            case "et": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ET_ITEM_MARKET_GUIDES)
            case "da": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_DA_ITEM_MARKET_GUIDES)
            case "el": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_EL_ITEM_MARKET_GUIDES)
            case "es": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ES_ITEM_MARKET_GUIDES)
            case "hr": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_HR_ITEM_MARKET_GUIDES)
            case "it": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_IT_ITEM_MARKET_GUIDES)
            case "lv": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_LV_ITEM_MARKET_GUIDES)
            case "hu": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_HU_ITEM_MARKET_GUIDES)
            case "nl": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_NL_ITEM_MARKET_GUIDES)
            case "pl": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_PL_ITEM_MARKET_GUIDES)
            case "pt": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_PT_ITEM_MARKET_GUIDES)
            case "ro": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_RO_ITEM_MARKET_GUIDES)
            case "sk": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SK_ITEM_MARKET_GUIDES)
            case "sl": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SL_ITEM_MARKET_GUIDES)
            case "fi": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_FI_ITEM_MARKET_GUIDES)
            case "sv": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_SV_ITEM_MARKET_GUIDES)
            case "vi": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_VI_ITEM_MARKET_GUIDES)
            case "zh": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_ZH_ITEM_MARKET_GUIDES)
            case "lt": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_LT_ITEM_MARKET_GUIDES)
            case "cn": sub_menu = d.find_elements(*MenuUS11MarketGuides.SUB_MENU_CN_ITEM_MARKET_GUIDES)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education | Menu title [Market Guides]\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Cryptocurrency trading' hyperlink.")
    def sub_menu_cryptocurrency_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            # case "ar":  sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_AR_CRYPTOCURRENCY_TRADING)
            # case "bg": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_BG_CRYPTOCURRENCY_TRADING)
            # case "cs": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_CS_CRYPTOCURRENCY_TRADING)
            case "cn": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_CN_CRYPTOCURRENCY_TRADING)
            # case "da": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_DA_CRYPTOCURRENCY_TRADING)
            case "de": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_DE_CRYPTOCURRENCY_TRADING)
            # case "el": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_EL_CRYPTOCURRENCY_TRADING)
            case "": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_EN_CRYPTOCURRENCY_TRADING)
            case "es": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ES_CRYPTOCURRENCY_TRADING)
            # case "et": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ET_CRYPTOCURRENCY_TRADING)
            # case "fi": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_FI_CRYPTOCURRENCY_TRADING)
            case "fr": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_FR_CRYPTOCURRENCY_TRADING)
            # case "hr": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_HR_CRYPTOCURRENCY_TRADING)
            # case "hu": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_HU_CRYPTOCURRENCY_TRADING)
            case "it": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_IT_CRYPTOCURRENCY_TRADING)
            # case "id": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ID_CRYPTOCURRENCY_TRADING)
            # case "lt": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_LT_CRYPTOCURRENCY_TRADING)
            # case "lv": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_LV_CRYPTOCURRENCY_TRADING)
            # case "nl":  sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_NL_CRYPTOCURRENCY_TRADING)
            case "pl": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_PL_CRYPTOCURRENCY_TRADING)
            # case "pt": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_PT_CRYPTOCURRENCY_TRADING)
            case "ro": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RO_CRYPTOCURRENCY_TRADING)
            case "ru": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_RU_CRYPTOCURRENCY_TRADING)
            # case "sk": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SK_CRYPTOCURRENCY_TRADING)
            # case "sl": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SL_CRYPTOCURRENCY_TRADING)
            # case "sv": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_SV_CRYPTOCURRENCY_TRADING)
            # case "th": \
            # sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_TH_CRYPTOCURRENCY_TRADING)
            case "vi": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_VI_CRYPTOCURRENCY_TRADING)
            case "zh": sub_menu = d.find_elements(*MenuUS11CryptocurrencyTrading.SUB_MENU_ZH_CRYPTOCURRENCY_TRADING)

        if len(sub_menu):
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Cryptocurrency trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'CFD trading guide' hyperlink.")
    def sub_menu_cfd_trading_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            # case "ar":  sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_AR_CFD_TRADING_GUIDE)
            case "bg": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_BG_CFD_TRADING_GUIDE)
            # case "cn": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_CN_CFD_TRADING_GUIDE)
            case "cs": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_CS_CFD_TRADING_GUIDE)
            # case "da": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_DA_CFD_TRADING_GUIDE)
            case "de": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_DE_CFD_TRADING_GUIDE)
            # case "el": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EL_CFD_TRADING_GUIDE)
            case "": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_EN_CFD_TRADING_GUIDE)
            case "es": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ES_CFD_TRADING_GUIDE)
            # case "et": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ET_CFD_TRADING_GUIDE)
            # case "fi": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_FI_CFD_TRADING_GUIDE)
            case "fr": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_FR_CFD_TRADING_GUIDE)
            # case "hr": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_HR_CFD_TRADING_GUIDE)
            # case "hu": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_HU_CFD_TRADING_GUIDE)
            # case "id": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ID_CFD_TRADING_GUIDE)
            case "it": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_IT_CFD_TRADING_GUIDE)
            # case "lt": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_LT_CFD_TRADING_GUIDE)
            # case "lv": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_LV_CFD_TRADING_GUIDE)
            case "nl": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_NL_CFD_TRADING_GUIDE)
            case "pl": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_PL_CFD_TRADING_GUIDE)
            # case "pt": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_PT_CFD_TRADING_GUIDE)
            case "ro": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RO_CFD_TRADING_GUIDE)
            case "ru": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_RU_CFD_TRADING_GUIDE)
            # case "sk": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SK_CFD_TRADING_GUIDE)
            # case "sl": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SL_CFD_TRADING_GUIDE)
            case "sv": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_SV_CFD_TRADING_GUIDE)
            # case "th": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_TH_CFD_TRADING_GUIDE)
            case "vi": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_VI_CFD_TRADING_GUIDE)
            case "zh": sub_menu = d.find_elements(*MenuUS11CFDTradingGuide.SUB_MENU_ZH_CFD_TRADING_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->CFD trading guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Spread betting guide' hyperlink.")
    def sub_menu_spread_betting_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_EN_SPREAD_BETTING_GUIDE)
            case "es": sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_ES_SPREAD_BETTING_GUIDE)
            case "pl": sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_PL_SPREAD_BETTING_GUIDE)
            case "cn": sub_menu = d.find_elements(*MenuUS11SpreadBettingGuide.SUB_MENU_CN_SPREAD_BETTING_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education > Spread betting guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'ETF trading' hyperlink.")
    def sub_menu_etf_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "ar": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_AR_ETF_TRADING)
            # case "bg": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_BG_ETF_TRADING)
            # case "cs": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_CS_ETF_TRADING)
            case "cn": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_CN_ETF_TRADING)
            # case "da": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_DA_ETF_TRADING)
            case "de": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_DE_ETF_TRADING)
            # case "el": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_EL_ETF_TRADING)
            case "": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_EN_ETF_TRADING)
            case "es": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ES_ETF_TRADING)
            # case "et": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ET_ETF_TRADING)
            # case "fi": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_FI_ETF_TRADING)
            # case "fr": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_FR_ETF_TRADING)
            # case "hr": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_HR_ETF_TRADING)
            # case "hu": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_HU_ETF_TRADING)
            case "it": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_IT_ETF_TRADING)
            # case "id": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ID_ETF_TRADING)
            # case "lt": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_LT_ETF_TRADING)
            # case "lv": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_LV_ETF_TRADING)
            # case "nl": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_NL_ETF_TRADING)
            # case "pl": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_PL_ETF_TRADING)
            # case "pt": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_PT_ETF_TRADING)
            # case "ro": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_RO_ETF_TRADING)
            case "ru": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_RU_ETF_TRADING)
            # case "sk": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_SK_ETF_TRADING)
            # case "sl": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_SL_ETF_TRADING)
            # case "sv": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_SV_ETF_TRADING)
            # case "th": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_TH_ETF_TRADING)
            case "vi": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_VI_ETF_TRADING)
            # case "zh": sub_menu = d.find_elements(*MenuUS11ETFTrading.SUB_MENU_ZH_ETF_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->ETF trading\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Strategies Guide' hyperlink.")
    def sub_menu_trading_strategies_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EN_TRADING_STRATEGIES_GUIDE)
            case "ar": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_AR_TRADING_STRATEGIES_GUIDE)
            case "bg": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_BG_TRADING_STRATEGIES_GUIDE)
            case "cn": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CN_TRADING_STRATEGIES_GUIDE)
            case "cs": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_CS_TRADING_STRATEGIES_GUIDE)
            case "da": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DA_TRADING_STRATEGIES_GUIDE)
            case "de": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_DE_TRADING_STRATEGIES_GUIDE)
            case "el": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_EL_TRADING_STRATEGIES_GUIDE)
            case "es": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ES_TRADING_STRATEGIES_GUIDE)
            case "et": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ET_TRADING_STRATEGIES_GUIDE)
            case "fi": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FI_TRADING_STRATEGIES_GUIDE)
            case "fr": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_FR_TRADING_STRATEGIES_GUIDE)
            case "hr": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HR_TRADING_STRATEGIES_GUIDE)
            case "hu": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_HU_TRADING_STRATEGIES_GUIDE)
            case "id": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ID_TRADING_STRATEGIES_GUIDE)
            case "it": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_IT_TRADING_STRATEGIES_GUIDE)
            case "lt": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LT_TRADING_STRATEGIES_GUIDE)
            case "lv": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_LV_TRADING_STRATEGIES_GUIDE)
            case "nl": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_NL_TRADING_STRATEGIES_GUIDE)
            case "pl": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PL_TRADING_STRATEGIES_GUIDE)
            case "pt": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_PT_TRADING_STRATEGIES_GUIDE)
            case "ro": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RO_TRADING_STRATEGIES_GUIDE)
            case "ru": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_RU_TRADING_STRATEGIES_GUIDE)
            case "sk": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SK_TRADING_STRATEGIES_GUIDE)
            case "sl": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SL_TRADING_STRATEGIES_GUIDE)
            case "sv": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_SV_TRADING_STRATEGIES_GUIDE)
            case "zh": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_ZH_TRADING_STRATEGIES_GUIDE)
            case "th": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_TH_TRADING_STRATEGIES_GUIDE)
            case "vi": sub_menu = d.find_elements(*MenuUS11TradingStrategiesGuide.SUB_MENU_VI_TRADING_STRATEGIES_GUIDE)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Strategies Guide\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Day Trading' hyperlink.")
    def sub_menu_day_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_DE_DAY_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ES_DAY_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11DayTrading.SUB_MENU_ALL_DAY_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Day Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Indices Trading' hyperlink.")
    def sub_menu_indices_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "id":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ID_INDICES_TRADING)
            case "de":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_DE_INDICES_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_IT_INDICES_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_RU_INDICES_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11IndicesTrading.SUB_MENU_ALL_INDICES_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Indices Trading menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Indices Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Investmate app' hyperlink.")
    def sub_menu_investmate_app_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            # case "ar": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_AR_INVESTMATE_APP)
            # case "bg": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_BG_INVESTMATE_APP)
            # case "cs": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_CS_INVESTMATE_APP)
            case "cn": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_CN_INVESTMATE_APP)
            # case "da": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_DA_INVESTMATE_APP)
            case "de": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_DE_INVESTMATE_APP)
            case "el": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_EL_INVESTMATE_APP)
            case "": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_EN_INVESTMATE_APP)
            case "es": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ES_INVESTMATE_APP)
            # case "et": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ET_INVESTMATE_APP)
            # case "fi": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_FI_INVESTMATE_APP)
            case "fr": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_FR_INVESTMATE_APP)
            # case "hr": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_HR_INVESTMATE_APP)
            # case "hu": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_HU_INVESTMATE_APP)
            case "it": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_IT_INVESTMATE_APP)
            # case "id": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ID_INVESTMATE_APP)
            # case "lt": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_LT_INVESTMATE_APP)
            # case "lv": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_LV_INVESTMATE_APP)
            case "nl": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_NL_INVESTMATE_APP)
            case "pl": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_PL_INVESTMATE_APP)
            case "pt": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_PT_INVESTMATE_APP)
            case "ro": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_RO_INVESTMATE_APP)
            case "ru": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_RU_INVESTMATE_APP)
            # case "sk": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_SK_INVESTMATE_APP)
            # case "sl": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_SL_INVESTMATE_APP)
            # case "sv": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_SV_INVESTMATE_APP)
            # case "th": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_TH_INVESTMATE_APP)
            case "vi": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_VI_INVESTMATE_APP)
            case "zh": sub_menu = d.find_elements(*MenuUS11InvestmateApp.SUB_MENU_ZH_INVESTMATE_APP)

        if len(sub_menu):
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Investmate app\" doesn't exist on production")

        ActionChains(d) \
            .move_to_element(sub_menu[0]) \
            .click() \
            .perform()

        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trend Trading' menu item.")
    def sub_menu_trend_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_EN_ITEM_TREND_TRADING)
            # case "de": sub_menu = d.find_elements(*MenuUS11TrendTrading.SUB_MENU_DE_ITEM_TREND_TRADING)

        if len(sub_menu) == 0:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trend Trading\" doesn't exist on production")

        ActionChains(d)\
            .move_to_element(sub_menu[0])\
            .click()\
            .perform()
        print(f"\n\n{datetime.now()}   => Trend trading menu item clicked")

        del sub_menu
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'What is a margin?' hyperlink.")
    def sub_menu_what_is_a_margin_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case _: sub_menu = d.find_elements(*MenuUS11WhatIsMargin.SUB_MENU_ALL_WHAT_IS_A_MARGIN)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'What is a margin?' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->What is a margin?\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Trading Psychology Guide' hyperlink.")
    def sub_menu_trading_psychology_guide_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ALL_TRADING_PSYCHOLOGY_GUIDE)
            case "ar": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_AR_TRADING_PSYCHOLOGY_GUIDE)
            case "de": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_DE_TRADING_PSYCHOLOGY_GUIDE)
            case "el": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_EL_TRADING_PSYCHOLOGY_GUIDE)
            case "es": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ES_TRADING_PSYCHOLOGY_GUIDE)
            case "fr": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_FR_TRADING_PSYCHOLOGY_GUIDE)
            case "it": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_IT_TRADING_PSYCHOLOGY_GUIDE)
            case "hu": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_HU_TRADING_PSYCHOLOGY_GUIDE)
            case "nl": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_NL_TRADING_PSYCHOLOGY_GUIDE)
            case "pl": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_PL_TRADING_PSYCHOLOGY_GUIDE)
            case "ro": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RO_TRADING_PSYCHOLOGY_GUIDE)
            case "ru": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_RU_TRADING_PSYCHOLOGY_GUIDE)
            case "zh": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_ZH_TRADING_PSYCHOLOGY_GUIDE)
            case "cn": sub_menu = d.find_elements(*MenuUS11TradingPsychologyGuide.SUB_MENU_CN_TRADING_PSYCHOLOGY_GUIDE)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => Trading Psychology Guide menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Trading Psychology Guide\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Position Trading' hyperlink.")
    def sub_menu_position_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_DE_POSITION_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_ES_POSITION_TRADING)
            case "ru":
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_RU_POSITION_TRADING)
            case "it":
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_IT_POSITION_TRADING)
            case "zh":
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_ZH_POSITION_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11PositionTrading.SUB_MENU_ALL_POSITION_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Position Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Position Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Swing Trading' hyperlink.")
    def sub_menu_swing_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11SwingTrading.SUB_MENU_DE_SWING_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11SwingTrading.SUB_MENU_ALL_SWING_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Swing Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Swing Trading\" doesn't exist on production")
        return d.current_url

    @allure.step(f"{datetime.now()}.   Click 'Scalp Trading' hyperlink.")
    def sub_menu_scalp_trading_move_focus_click(self, d, test_language):
        sub_menu = list()
        match test_language:
            case "de":
                sub_menu = d.find_elements(*MenuUS11ScalpTrading.SUB_MENU_DE_SCALP_TRADING)
            case "es":
                sub_menu = d.find_elements(*MenuUS11ScalpTrading.SUB_MENU_DE_SCALP_TRADING)
            case _:
                sub_menu = d.find_elements(*MenuUS11ScalpTrading.SUB_MENU_ALL_SCALP_TRADING)

        if len(sub_menu) > 0:
            ActionChains(d) \
                .move_to_element(sub_menu[0]) \
                .click() \
                .perform()
            print(f"\n\n{datetime.now()}   => 'Scalp Trading' menu click")
        else:
            pytest.skip(f"For test language '{test_language}' "
                        f"the page \"Education->Scalp Trading\" doesn't exist on production")
        return d.current_url
