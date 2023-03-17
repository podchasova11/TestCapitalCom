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
        wait = WebDriverWait(self.browser, 10)

        # Wait for the new tab to finish loading content
        print(f"{datetime.now()}   Wait until load title =>")
        wait.until(EC.title_is("Trading Platform | Capital.com"))
        print(f'{datetime.now()}   => Title "Trading Platform | Capital.com" loaded')
        # platform_url = "https://capital.com/trading/platform/"
        # self.check_current_page_is(platform_url)

        print(f"{datetime.now()}   Is there a LOGO? =>")
        if self.element_is_present(*TopBarLocators.LOGO):
            print(f"{datetime.now()}   => LOGO is on the page!")
            return True
        else:
            print(f"{datetime.now()}   => LOGO is not present on the page!")
            return False
