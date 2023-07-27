from selenium.webdriver.common.by import By


class TradingPlatformSignupFormLocators:
    SIGNUP_FRAME = (By.CSS_SELECTOR, "signup-component")
    LOGIN_FRAME = (By.CSS_SELECTOR, "login-component")
    FRAME_TITLE = (By.CSS_SELECTOR, "div.modal__header-title")
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "button.button-main")


class TopBarLocators:
    LOGO = (By.CSS_SELECTOR, "div logo object[data='./assets/pic/logo.svg'].logo")
