"""
-*- coding: utf-8 -*-
@Time    : 2023/04/13 18:25
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class HeaderButtonLoginLocators:
    """ Locators for ..."""
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")


class HeaderButtonTradeLocators:
    BUTTON_TRADE = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")


class VideoBannerLocators:
    VIDEO_BANNER = (By.CSS_SELECTOR, "div.side-video.side-video--vertical video")


class ButtonUnderVideoBannerLocators:
    BUTTON_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a[href='https://capital.com/trading/signup']")
    BUTTON_CREATE_ACCOUNT_UNDER_VIDEO_BANNER = \
        (By.CSS_SELECTOR, "div.side-video.side-video--vertical > div > a.js_signup")


class VerHorBannerButtonLocators:
    VER_HOR_BANNER_BUTTON = (By.CSS_SELECTOR, ".grid  div.seo-banner a[href='/trading/signup']")

    # VER_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")
    # HOR_BANNER_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.seo-banner > div > a[href='/trading/signup']")


class ButtonFreeDemoOnHorizontalBannerLocators:
    BUTTON_FREE_DEMO_ON_HOR_BANNER = (By.CSS_SELECTOR, "")


class BlockStepTradingLocators:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "section.regSteps i.regSteps__item.js_signup")
    BUT_CREATE_YOUR_ACCOUNT_DE = (By.CSS_SELECTOR, "#cc_ab42 div.js_signup")


class ButtonInBannerLocators:
    BUTTON_IN_BANNER = (By.CSS_SELECTOR, ".grid .detail__aside .inBanner > a")


class ButtonTradeOnWidgetMostTradedLocators:
    MOST_TRADED = (By.CSS_SELECTOR, "div.mostTraded__market > a[href*='spotlight']")  # List
    # MOST_TRADED_1 = (By.CSS_SELECTOR, "div:nth-child(1) > div.mostTraded__market > a")
    # MOST_TRADED_2 = (By.CSS_SELECTOR, "div:nth-child(2) > div.mostTraded__market > a")
    # MOST_TRADED_3 = (By.CSS_SELECTOR, "div:nth-child(3) > div.mostTraded__market > a")
    # MOST_TRADED_4 = (By.CSS_SELECTOR, "div:nth-child(4) > div.mostTraded__market > a")
    # MOST_TRADED_5 = (By.CSS_SELECTOR, "div:nth-child(5) > div.mostTraded__market > a")


class BlockOurCoursesLocators:
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "div [href='https://capital.com/trading/signup']")


class CoursesPage:
    COURSES_PAGES_LIST = (By.CSS_SELECTOR, "li.courseCard__row > a")


class SubPages:
    SUB_PAGES_LIST = (By.CSS_SELECTOR, "div.side-nav__wrap > div.side-nav > a")


class ButtonsOnPageLocators:
    BUTTON_START_TRADING_IN_ARTICLE = (By.CSS_SELECTOR, "ul > li:nth-child(1) > a.js_signup")
    BUTTON_START_TRADING_IN_ARTICLE2 = (By.CSS_SELECTOR, ".hidden-xs.no-wrap.ready-starting__btn > a")
    BUTTON_TRADING_SELL = (By.CSS_SELECTOR, "a.button-main.sell.ln-auto.js_signup")
    BUTTON_TRADING_BUY = (By.CSS_SELECTOR, "a.button-main.buy.ln-auto.js_signup")
    BUTTON_CREATE_ACCOUNT = (By.CSS_SELECTOR, "div li [href='https://capital.com/trading/platform/']")

    # Tables with Sell/Buy
    # Tabs
    TAB_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR, "div.main__tab--wrap > div > a:nth-child(1)")
    TAB_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR, "div.main__tab--wrap > div > a:nth-child(2)")
    TAB_TRADING_ITEM_TOP_FALLERS = (By.CSS_SELECTOR, "div.main__tab--wrap > div > a:nth-child(3)")
    TAB_TRADING_ITEM_MOST_VOLATILE = (By.CSS_SELECTOR, "div.main__tab--wrap > div > a:nth-child(4)")
    # Item name
    SPAN_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-mosttraded > table > "
                                                      "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-risers > table > "
                                                     "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_TOP_FALLERS = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-fallers > table > "
                                                      "tbody > tr > td.name > a > span.table-tools__title")
    SPAN_TRADING_ITEM_MOST_VOLATILE = (By.CSS_SELECTOR, ".table-tools.catTabs.tab-volatile > table > "
                                                        "tbody > tr > td.name > a > span.table-tools__title")
    # Buttons
    BUTTON_TRADING_SELL_MOST_TRADED = (By.CSS_SELECTOR, ".tab-mosttraded > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_MOST_TRADED = (By.CSS_SELECTOR, ".tab-mosttraded > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_TOP_RISERS = (By.CSS_SELECTOR, ".tab-risers > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_TOP_RISERS = (By.CSS_SELECTOR, ".tab-risers > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_TOP_FALLERS = (By.CSS_SELECTOR, ".tab-fallers > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_TOP_FALLERS = (By.CSS_SELECTOR, ".tab-fallers > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_TRADING_SELL_MOST_VOLATILE = (By.CSS_SELECTOR, ".tab-volatile > table > tbody > tr > td:nth-child(3) > a")
    BUTTON_TRADING_BUY_MOST_VOLATILE = (By.CSS_SELECTOR, ".tab-volatile > table > tbody > tr > td:nth-child(5) > a")

    BUTTON_ON_STICKY_BAR = (By.CSS_SELECTOR, "div.encStickyBar > div > a")
    BUTTON_SIGNUP_LOGIN = (By.CSS_SELECTOR, "a[href='/trading/signup'][class*='__cp_b'][class*='ln-auto']")


class MainBannerLocators:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--darkText.js_signup")
    BUTTON_TRY_DEMO = (By.CSS_SELECTOR, "a.cc-banner__btn.btn.btn--emptyblack.js_signup.hideXs")

class RightBannerLocators:
    BUTTON_TRY_DEMO_RIGHT_BANNER = (By.CSS_SELECTOR, "btn inBanner__btn rounded-lg ln-auto")
