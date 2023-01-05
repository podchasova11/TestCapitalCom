from selenium.webdriver.common.by import By


class OnTrastLocators:
    BUTTON_ACCEPT_ALL_COOKIE = (By.CSS_SELECTOR, "#onetrust-button-group > #onetrust-accept-btn-handler")


class CapitalPageLocators:
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ".cc-header__wrap #wg_loginBtn")
    BUTTON_TRADE_NOW = (By.CSS_SELECTOR, ".cc-header__wrap [data-type='btn_header']")
    HEADER_OF_CAPITAL_COM = (By.CSS_SELECTOR, ".cc-header__wrap")
    WIDGET_TRADING = (By.CSS_SELECTOR, ".tools > .tab-list")


class HeaderElementLocators:
    BUTTON_LOGIN_LOCATOR = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
    # BUTTON_LOGIN = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_login")
    BUTTON_SIGNUP_LOCATOR = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")
    BUTTON_SIGNUP = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")


class FooterElementLocators:
    pass


class SignupLoginFormLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")
    SIGNUP_FORM = (By.CSS_SELECTOR, "#s_overlay > div > button")
    LOGIN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay > div input[type=checkbox]")
    SIGNUP_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form a.l_btn_signup")
    BUTTON_CLOSE_ON_LOGIN_FORM = (By.CSS_SELECTOR, "#l_overlay > div > button")
    BUTTON_CLOSE_ON_SIGNUP_FORM = (By.CSS_SELECTOR, "button.s_cancel")

    LOGIN_REF_SIGNUP_LOCATOR = (By.CSS_SELECTOR, "#l_overlay a.l_btn_signup")
    LOGIN_INPUT_USERNAME = (By.CSS_SELECTOR, "")
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "")
    LOGIN_CHECKBOX_LOCATOR = (By.CSS_SELECTOR, "label > input[type=checkbox]")
    LOGIN_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#l_overlay form > button[type=submit]")
    SIGNUP_REF_LOGIN_LOCATOR = (By.CSS_SELECTOR, "div.signup-form a.l_btn_signup")
    SIGNUP_INPUT_USERNAME_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_INPUT_PASSWORD_LOCATOR = (By.CSS_SELECTOR, "")
    SIGNUP_SUBMIT_BTN_LOCATOR = (By.CSS_SELECTOR, "#s_overlay .signup-form button[type=submit]")


class MainBaner:
    TAB1 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='0']")
    TAB1_TRADE_NOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_trade_cfds']")
    TAB1_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_trade_cfds_demo']")
    TAB1_OPEN_ACCOUNT = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_spread_betting']")
    TAB2 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='1']")
    TAB2_START_TRADING = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB2_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB2_TAKE_ME_THERE = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_edu']")
    TAB3 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='2']")
    TAB3_L1_LEARN_MORE_ASIC = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_pro_au']")
    TAB3_L1_START_TRADING_ASIC = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_pro_au_demo']")
    TAB3_L2_START_TRADING_FCA = (By.CSS_SELECTOR,
                                 "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22']")
    TAB3_L2_PRACTISE_FOR_FREE_FCA = (By.CSS_SELECTOR,
                                     "div.bannersHome__buttons > a[data-type='topbanner_best_platform_22_demo']")
    TAB3_SHOW_ME_HOW = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='topbanner_esg']")
    TAB4 = (By.CSS_SELECTOR, "button.bannersHome__switcher[data-slick-index='3']")
    TAB4_EXPLORE_FEATURES = (By.CSS_SELECTOR, "div.bannersHome__buttons > a[data-type='banner-tradingview']")


class WidgetStillLookingFor:
    BUT_CREATE_YOUR_ACCOUNT = (By.CSS_SELECTOR, "div.regSteps__shape > i.regSteps__item.js_signup")


class WidgetPromoMarket:
    SLIDER_FADE = (By.CSS_SELECTOR, "div.js-sliderFade.cc-sliderFade")
    LIST_SLIDER_FADE_ITEMS = (By.CSS_SELECTOR, "div.cc-sliderFade__item")
    BUTTON_ON_ITEM = (By.CSS_SELECTOR, "div.promoMarket__col[data-type='wdg_singlemarket']")
    LIST_BUTTONS_TRADE_NOW = (By.CSS_SELECTOR, "div.promoMarket__col[data-type='wdg_singlemarket']")
    ACTIVE_BUTTON_TRADE_NOW = (By.CSS_SELECTOR, "div.active div.promoMarket__col[data-type='wdg_singlemarket']")
    LIST_BUTs_TRADE_NOW_2 = (By.CSS_SELECTOR,
                             ".cc-sliderFade__item > .promoMarket > .promoMarket__inner > .btn.js_signup")
    BUT_1_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(1) > .promoMarket > .promoMarket__inner > div.btn.js_signup")
    BUT_2_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(2) > .promoMarket > .promoMarket__inner > div.btn.js_signup")
    BUT_3_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(3) > .promoMarket > .promoMarket__inner > div.btn.js_signup")
    BUT_4_TRADE_NOW_ACTIVE = (
        By.CSS_SELECTOR,
        "div.cc-sliderFade__item:nth-child(4) > .promoMarket > .promoMarket__inner > div.btn.js_signup")


class WidgetTradingInstrument:
    TABS_NAVIGATOR = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] > div.tabs__nav")
    FLAG_LAYOUT = (By.CSS_SELECTOR, "div.tools > div.tools__item--head > span:nth-child(3)")
    LIST_TABS_1 = (By.CSS_SELECTOR, "div[data-type='wdg_markets'] li[data-type='wdg_markets_tab']")
    LIST_BUTTONS_TRADE_FOR_MTR_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='mtr'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_COM_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='com'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_IND_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='ind'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_CRY_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='cryp'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_SHAR_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='shar'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_FX_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='fx'] td > a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_ETF_1 = (By.CSS_SELECTOR, "tbody[data-tab-content='etf'] td > a.js_signup_new")
    LIST_TABS_2 = (By.CSS_SELECTOR, "div.mainConstuctor__widget div.tools a.tab-list__item")
    LIST_BUTTONS_TRADE_FOR_MTR_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Most a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_COM_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Commodities a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_IND_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Indices a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_CRY_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Crypto a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_SHAR_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Shares a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_FX_2 = (By.CSS_SELECTOR, "div.tools div.ihome-Forex a.js_signup_new")
    LIST_BUTTONS_TRADE_FOR_ETF_2 = (By.CSS_SELECTOR, "div.tools div.ihome-ETFs a.js_signup_new")


class WidgetExploreOurPlatform:
    BUTTON_TRY_NOW = (By.CSS_SELECTOR, "section a.btn.js_signup:nth-child(2)")


class WidgetNewToTrading:
    SECTION_NEW_TO_TRADING = (By.CSS_SELECTOR, "main > section.newToTrading")
    BUTTON_PRACTISE_FOR_FREE = (By.CSS_SELECTOR, "section.newToTrading a.btn.js_signup")


class WidgetTradingCalculator:
    BUTTON_START_TRADING = (By.CSS_SELECTOR, "#calcWrap .tradingCalc__footer > div.btn.js_signup_new")


class WidgetTradersDashboard:
    LIST_BUTTONS_TRADE = (By.CSS_SELECTOR, ".tradersDashboard button.js_signup")


class BannerOfCounters:
    BUTTON_TRY_NOW = (By.CSS_SELECTOR, ".cc-counter__body > .btn.js_signup")