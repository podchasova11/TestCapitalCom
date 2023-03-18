from selenium.webdriver.common.by import By


class MyAccountLocator:
    LOGOUT = (By.CSS_SELECTOR, "#userPanel div.logout-user")
    TRADING_PLATFORM = (By.CSS_SELECTOR, "#userPanel button.tradingPlatformBtn")
    CLOSE = (By.CSS_SELECTOR, "#userPanel span.user-panel-close")
