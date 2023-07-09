"""
-*- coding: utf-8 -*-
@Time    : 2023/04/20 22:00
@Author  : Suleyman Alirzaev
"""
from datetime import datetime
import pytest
import allure
from pages.base_page import BasePage
from pages.Elements.testing_elements_locators import QRCodeLocators
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# import cv2
# from pyzbar import pyzbar
# import zxing
# from qreader import QReader

# import os
# import aspose.barcode as barcode
# import urllib.request


class QRCodeDecode(BasePage):

    def arrange_(self, d, cur_item_link, qr_code):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # locator = ()

        if qr_code == 'investmate':
            self.locator = QRCodeLocators.QR_CODE_INVESTMATE
            self.locator_link = QRCodeLocators.QR_CODE_INVESTMATE_LINK
            self.filename = 'investmate'
        elif qr_code == 'easy_learning':
            self.locator = QRCodeLocators.QR_CODE_EASY_LEARNING
            self.locator_link = QRCodeLocators.QR_CODE_EASY_LEARNING_LINK
            self.filename = 'easy_learning'
        elif qr_code == 'capital':
            self.locator = QRCodeLocators.QR_CODE_CAPITAL
            self.locator_link = QRCodeLocators.QR_CODE_CAPITAL_LINK
            self.filename = 'capital'
        else:
            pytest.skip("QR code type is undefined")

        print(f"{datetime.now()}   QR_CODE is visible? =>")
        try:
            if self.browser.find_element(*self.locator_link):
                print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is not visible on the page!")
            pytest.skip(f"Checking element QR_CODE_{self.filename.upper()} is not on this page")

    @allure.step("Save and decode QR_CODE on page")
    def element_decode(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} is present? =>")
        button_list = self.browser.find_elements(*self.locator_link)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} is present on the page!")

        print(f"{datetime.now()}   QR_CODE_{self.filename.upper()} scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        try:
            # qr_code_locator = self.browser.find_element(*self.locator)
            # link = qr_code_locator.get_attribute
            link = self.get_attribute("title", *self.locator_link)
            print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} found")
            print(f"{datetime.now()}   => Opening link from QR_CODE")
            self.browser.get(link)

            ############ Не удалять ############
            # qr_code = self.browser.find_element(*self.locator)
            # src = qr_code.get_attribute('src')
            # # Download the image
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} download started.")
            # urllib.request.urlretrieve(src, f"test_data/{self.filename}.png")
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} downloaded.")
            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanning started.")
            #
            # # Load QR code image
            # reader = barcode.barcoderecognition.BarCodeReader(f"test_data/{self.filename}.png")
            #
            # # Read QR codes
            # recognized_results = reader.read_bar_codes()
            #
            # for x in recognized_results:
            #     url_end = x.code_text.find(" ")
            #     url_2 = x.code_text[0:url_end]
            # self.browser.get(url_2)
            # os.remove(f"test_data/{self.filename}.png")

            # print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} scanned!")
            ####################################
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => QR_CODE_{self.filename.upper()} NOT CLICKED")

        del button_list
        return True
