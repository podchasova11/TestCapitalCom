import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pages.base_page import BasePage
from pages.Capital.Trading.Platform.Topbar.topbar_locators import TopBarLocators


class TopBar(BasePage):

    @allure.step("Check if the element is present on the page")
    def trading_platform_logo_is_present(self):
        # Setup wait for later
        print(f"{datetime.now()}   Start Check method =>")
        wait = WebDriverWait(self.browser, 15)

        # Wait for the new tab to finish loading content
        print(f"{datetime.now()}   Wait until load title =>")
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        print(f'{datetime.now()}   => Page with title "Trading Platform | Capital.com" loaded')

        print(f"{datetime.now()}   Is there a LOGO? =>")
        if self.element_is_present(*TopBarLocators.LOGO) and self.element_is_visible(TopBarLocators.LOGO, 5):
            print(f"{datetime.now()}   => LOGO is present on the page!")
            return True
        else:
            print(f"{datetime.now()}   => LOGO is not present on the page!")
            return False
