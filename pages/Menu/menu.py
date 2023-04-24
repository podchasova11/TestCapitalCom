"""
-*- coding: utf-8 -*-
@Time    : 2023/01/27 10:00
@Author  : Alexander Tomelo
"""
import time

import allure
import datetime
import pytest
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from pages.Menu.menu_locators import (
    Menu,
    MenuUS11Glossary,
    Menu1101,
    MenuUS11TradingCourses,
    MenuUS11CommoditiesTrading
)


class MenuSection(BasePage):

    @allure.step(f"{datetime.datetime.now()}.   Click button [Burger menu].")
    def burger_menu_click(self, d):
        
        menu1 = d.find_element(*Menu.MENU)

        self.element_is_clickable(menu1)
        menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Learn to trade' menu section.")
    def menu_education_move_focus(self, d, test_language):
        match test_language:
            case "ar":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_AR_LEARN_TO_TRADE)  # not Glossary
            case "bg":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_BG_LEARN_TO_TRADE)
            case "cn":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_CN_LEARN_TO_TRADE)  # not Glossary
            case "cs":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_CS_LEARN_TO_TRADE)
            case "da":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_DA_LEARN_TO_TRADE)
            case "de":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_DE_LEARN_TO_TRADE)
            case "el":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_EL_LEARN_TO_TRADE)
            case "":    menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_EN_LEARN_TO_TRADE)
            case "es":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ES_LEARN_TO_TRADE)
            case "et":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ET_LEARN_TO_TRADE)
            case "fi":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_FI_LEARN_TO_TRADE)
            case "fr":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_FR_LEARN_TO_TRADE)
            case "hr":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_HR_LEARN_TO_TRADE)
            case "hu":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_HU_LEARN_TO_TRADE)
            # case "id":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ID_LEARN_TO_TRADE)  # not Education
            case "it":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_IT_LEARN_TO_TRADE)
            case "lt":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_LT_LEARN_TO_TRADE)
            case "lv":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_LV_LEARN_TO_TRADE)
            case "nl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_NL_LEARN_TO_TRADE)
            case "pl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_PL_LEARN_TO_TRADE)
            case "pt":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_PT_LEARN_TO_TRADE)
            case "ro":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_RO_LEARN_TO_TRADE)
            case "ru":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_RU_LEARN_TO_TRADE)
            case "sk":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SK_LEARN_TO_TRADE)
            case "sl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SL_LEARN_TO_TRADE)
            case "sv":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SV_LEARN_TO_TRADE)
            case "zh":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ZH_LEARN_TO_TRADE)
            # case "th":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_TH_LEARN_TO_TRADE)  # not Education
            case "vi":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_VI_LEARN_TO_TRADE)  # not Glossary

            case _:     pytest.fail(f"For '{test_language}' not submenu [Education]")

        ActionChains(d)\
            .move_to_element(menu1)\
            .pause(1)\
            .perform()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Glossary' hyperlink.")
    def sub_menu_glossary_move_focus_click(self, d, test_language):
        match test_language:
            # case "ar":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_AR_GLOSSARY)
            case "bg":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_BG_GLOSSARY)
            case "cs":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_CS_GLOSSARY)
            case "da":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_DA_GLOSSARY)
            case "de":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_DE_GLOSSARY)
            case "el":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_EL_GLOSSARY)
            case "":    menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_EN_GLOSSARY)
            case "es":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ES_GLOSSARY)
            case "et":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ET_GLOSSARY)
            case "fi":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_FI_GLOSSARY)
            case "fr":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_FR_GLOSSARY)
            case "hr":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_HR_GLOSSARY)
            case "hu":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_HU_GLOSSARY)
            # case "id":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ID_GLOSSARY)
            case "it":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_IT_GLOSSARY)
            case "lt":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_LT_GLOSSARY)
            case "lv":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_LV_GLOSSARY)
            case "nl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_NL_GLOSSARY)
            case "pl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_PL_GLOSSARY)
            case "pt":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_PT_GLOSSARY)
            case "ro":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_RO_GLOSSARY)
            case "ru":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_RU_GLOSSARY)
            case "sk":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SK_GLOSSARY)
            case "sl":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SL_GLOSSARY)
            case "sv":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_SV_GLOSSARY)
            case "zh":  menu1 = d.find_element(*MenuUS11Glossary.SUB_MENU_ZH_GLOSSARY)

            case _:     pytest.fail(f"For '{test_language}' language test in development")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url

        # ActionBuilder(d).clear_actions()
        # self.element_is_clickable(menu1)
        # menu1.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Basics_of_trading' hyperlink.")
    def sub_menu_basics_of_trading_move_focus_click(self, d, test_language):
        match test_language:
            case "":  menu2 = d.find_element(*Menu1101.SUB_MENU_EN_ITEM_BASICS_OF_TRADING)
            case "de":  menu2 = d.find_element(*Menu1101.SUB_MENU_DE_ITEM_BASICS_OF_TRADING)
            case "ru":  menu2 = d.find_element(*Menu1101.SUB_MENU_RU_ITEM_BASICS_OF_TRADING)
            case "bg":  menu2 = d.find_element(*Menu1101.SUB_MENU_BG_ITEM_BASICS_OF_TRADING)
            case "cs":  menu2 = d.find_element(*Menu1101.SUB_MENU_CS_ITEM_BASICS_OF_TRADING)
            case "fr":  menu2 = d.find_element(*Menu1101.SUB_MENU_FR_ITEM_BASICS_OF_TRADING)
            # case "ar":  menu2 = d.find_element(*Menu1101.SUB_MENU_AR_ITEM_BASICS_OF_TRADING)
            case "et":  menu2 = d.find_element(*Menu1101.SUB_MENU_ET_ITEM_BASICS_OF_TRADING)
            case "da":  menu2 = d.find_element(*Menu1101.SUB_MENU_DA_ITEM_BASICS_OF_TRADING)
            case "el":  menu2 = d.find_element(*Menu1101.SUB_MENU_EL_ITEM_BASICS_OF_TRADING)
            case "es":  menu2 = d.find_element(*Menu1101.SUB_MENU_ES_ITEM_BASICS_OF_TRADING)
            case "hr":  menu2 = d.find_element(*Menu1101.SUB_MENU_HR_ITEM_BASICS_OF_TRADING)
            case "it":  menu2 = d.find_element(*Menu1101.SUB_MENU_IT_ITEM_BASICS_OF_TRADING)
            case "lv":  menu2 = d.find_element(*Menu1101.SUB_MENU_LV_ITEM_BASICS_OF_TRADING)
            case "hu":  menu2 = d.find_element(*Menu1101.SUB_MENU_HU_ITEM_BASICS_OF_TRADING)
            case "nl":  menu2 = d.find_element(*Menu1101.SUB_MENU_NL_ITEM_BASICS_OF_TRADING)
            case "pl":  menu2 = d.find_element(*Menu1101.SUB_MENU_PL_ITEM_BASICS_OF_TRADING)
            case "pt":  menu2 = d.find_element(*Menu1101.SUB_MENU_PT_ITEM_BASICS_OF_TRADING)
            case "ro":  menu2 = d.find_element(*Menu1101.SUB_MENU_RO_ITEM_BASICS_OF_TRADING)
            case "sk":  menu2 = d.find_element(*Menu1101.SUB_MENU_SK_ITEM_BASICS_OF_TRADING)
            case "sl":  menu2 = d.find_element(*Menu1101.SUB_MENU_SL_ITEM_BASICS_OF_TRADING)
            case "fi":  menu2 = d.find_element(*Menu1101.SUB_MENU_FI_ITEM_BASICS_OF_TRADING)
            case "sv":  menu2 = d.find_element(*Menu1101.SUB_MENU_SV_ITEM_BASICS_OF_TRADING)
            # case "vi":  menu2 = d.find_element(*Menu1101.SUB_MENU_VI_ITEM_BASICS_OF_TRADING)
            case "zh":  menu2 = d.find_element(*Menu1101.SUB_MENU_ZH_ITEM_BASICS_OF_TRADING)
            case "lt":  menu2 = d.find_element(*Menu1101.SUB_MENU_LT_ITEM_BASICS_OF_TRADING)
            # case "cn":  menu2 = d.find_element(*Menu1101.SUB_MENU_CN_ITEM_BASICS_OF_TRADING)
            # case "id": menu2 = d.find_element(*Menu1101.SUB_MENU_ID_ITEM_BASICS_OF_TRADING)
            case _:     pytest.fail(f"For '{test_language}' language test in development")
        ActionChains(d) \
            .move_to_element(menu2) \
            .click() \
            .perform()
        ActionChains(d) \
            .pause(1) \
            .perform()

        return d.current_url



        # self.element_is_clickable(menu2)
        # menu2.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Trading courses hyperlink.")
    def sub_menu_trading_courses_move_focus_click(self, d, test_language):
        match test_language:
            case "":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_EN_ITEM_TRADING_COURSES)
            case "de":  menu2 = d.find_element(MenuUS11TradingCourses.SUB_MENU_DE_ITEM_TRADING_COURSES)
            case "ru":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_RU_ITEM_TRADING_COURSES)
            case "bg":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_BG_ITEM_TRADING_COURSES)
            case "cs":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_CS_ITEM_TRADING_COURSES)
            case "fr":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_FR_ITEM_TRADING_COURSES)
            case "ar":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_AR_ITEM_TRADING_COURSES)
            case "et":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_ET_ITEM_TRADING_COURSES)
            case "da":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_DA_ITEM_TRADING_COURSES)
            case "el":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_EL_ITEM_TRADING_COURSES)
            case "es":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_ES_ITEM_TRADING_COURSES)
            case "hr":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_HR_ITEM_TRADING_COURSES)
            case "it":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_IT_ITEM_TRADING_COURSES)
            case "lv":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_LV_ITEM_TRADING_COURSES)
            case "hu":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_HU_ITEM_TRADING_COURSES)
            case "nl":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_NL_ITEM_TRADING_COURSES)
            case "pl":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_PL_ITEM_TRADING_COURSES)
            case "pt":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_PT_ITEM_TRADING_COURSES)
            case "ro":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_RO_ITEM_TRADING_COURSES)
            case "sk":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_SK_ITEM_TRADING_COURSES)
            case "sl":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_SL_ITEM_TRADING_COURSES)
            case "fi":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_FI_ITEM_TRADING_COURSES)
            case "sv":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_SV_ITEM_TRADING_COURSES)
            case "vi":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_VI_ITEM_TRADING_COURSES)
            case "zh":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_ZH_ITEM_TRADING_COURSES)
            case "lt":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_LT_ITEM_TRADING_COURSES)
            case "cn":  menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_CN_ITEM_TRADING_COURSES)
            case "id": menu2 = d.find_element(*MenuUS11TradingCourses.SUB_MENU_ID_ITEM_TRADING_COURSES)
            case _:     pytest.fail(f"For '{test_language}' language test in development")
        ActionChains(d) \
            .move_to_element(menu2) \
            .click() \
            .perform()
        ActionChains(d) \
            .pause(1) \
            .perform()

        return d.current_url

        # self.element_is_clickable(menu2)
        # menu2.click()

    @allure.step(f"{datetime.datetime.now()}.   Click 'Commodities trading' hyperlink.")
    def sub_menu_commodities_trading_move_focus_click(self, d, test_language):
        match test_language:
            case "ar":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_AR_COMMODITIES_TRADING)
            # case "bg":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_BG_COMMODITIES_TRADING) # Нет такой страницы
            # case "cs":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CS_COMMODITIES_TRADING) # Нет такой страницы
            case "cn": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_CN_COMMODITIES_TRADING)
            # case "da":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DA_COMMODITIES_TRADING) # Нет такой страницы
            case "de":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_DE_COMMODITIES_TRADING)
            # case "el":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EL_COMMODITIES_TRADING) # Нет такой страницы
            case "":    menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_EN_COMMODITIES_TRADING)
            case "es":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ES_COMMODITIES_TRADING)
            # case "et":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ET_COMMODITIES_TRADING) # Нет такой страницы
            # case "fi":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FI_COMMODITIES_TRADING) # Нет такой страницы
            case "fr":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_FR_COMMODITIES_TRADING)
            # case "hr":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HR_COMMODITIES_TRADING) # Нет такой страницы
            # case "hu":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_HU_COMMODITIES_TRADING) # Нет такой страницы
            # case "id":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ID_COMMODITIES_TRADING) # Нет такой страницы
            case "it":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_IT_COMMODITIES_TRADING)
            # case "lt":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LT_COMMODITIES_TRADING) # Нет такой страницы
            # case "lv":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_LV_COMMODITIES_TRADING) # Нет такой страницы
            case "nl":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_NL_COMMODITIES_TRADING)
            case "pl":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PL_COMMODITIES_TRADING)
            # case "pt":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_PT_COMMODITIES_TRADING) # Нет такой страницы
            case "ro":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_RO_COMMODITIES_TRADING)
            case "ru":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_RU_COMMODITIES_TRADING)
            # case "sk":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SK_COMMODITIES_TRADING) # Нет такой страницы
            # case "sl":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SL_COMMODITIES_TRADING) # Нет такой страницы
            # case "sv":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_SV_COMMODITIES_TRADING) # Нет такой страницы
            case "zh":  menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_ZH_COMMODITIES_TRADING)
            # case "th": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_TH_COMMODITIES_TRADING)  # Нет такой страницы
            case "vi": menu1 = d.find_element(*MenuUS11CommoditiesTrading.SUB_MENU_VI_COMMODITIES_TRADING)

            case _:     pytest.fail(f"For '{test_language}' language test in development")

        ActionChains(d)\
            .move_to_element(menu1)\
            .click()\
            .perform()

        time.sleep(1)
        return d.current_url



    # @allure.step(f"{datetime.datetime.now()}.  Click ' Education to trade' hyperlink.")
    # def click_learn_to_trade_item(self, d, test_language):
    #     if test_language == "":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_EN_ITEM_LEARN_TO_TRADE)
    #         print("1")
    #     elif test_language == "de":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_DE_ITEM_LEARN_TO_TRADE)
    #     elif test_language == "ru":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_RU_ITEM_LEARN_TO_TRADE)
    #     elif test_language == "bg":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_BG_ITEM_LEARN_TO_TRADE)
    #     elif test_language == "cs":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_CS_ITEM_LEARN_TO_TRADE)
    #     elif test_language == "fr":
    #         menu2 = d.find_element(MenuUS03.SUB_MENU_FR_ITEM_LEARN_TO_TRADE)
    #     else:
    #         pytest.fail(f"For '{test_language}' language test in development")
    #
    #     self.browser.execute_script(
    #         'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
    #         menu2)
    #     print("2")
    #
    #     self.element_is_clickable(menu2, 5)
    #     print("3")
    #     menu2.click()
    #     print("4")

