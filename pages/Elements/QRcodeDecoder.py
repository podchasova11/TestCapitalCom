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

import os
import aspose.barcode as barcode
import urllib.request


class QRCodeDecode(BasePage):

    def arrange_(self, d, cur_item_link, qr_code):
        print(f"\n{datetime.now()}   1. Arrange")

        if not self.current_page_is(cur_item_link):
            self.link = cur_item_link
            self.open_page()

        # locator = ()

        if qr_code == 'investmate':
            self.locator = QRCodeLocators.QR_CODE_INVESTMATE
            self.filename = 'investmate'
        elif qr_code == 'easy_learning':
            self.locator = QRCodeLocators.QR_CODE_EASY_LEARNING
            self.filename = 'easy_learning'
        elif qr_code == 'capital':
            self.locator = QRCodeLocators.QR_CODE_CAPITAL
            self.filename = 'capital'
        else:
            pytest.skip("QR code type is undefined")

        print(f"{datetime.now()}   QR_CODE is visible? =>")
        try:
            if self.browser.find_element(*self.locator):
                print(f"{datetime.now()}   => QR_CODE is visible on the page!")
        except NoSuchElementException:
            print(f"{datetime.now()}   => QR_CODE is not visible on the page!")
            pytest.skip("Checking element QR_CODE is not on this page")

    @allure.step("Save and decode QR_CODE on page")
    def element_decode(self):
        print(f"\n{datetime.now()}   2. Act")
        print(f"{datetime.now()}   QR_CODE is present? =>")
        button_list = self.browser.find_elements(*self.locator)
        if len(button_list) == 0:
            print(f"{datetime.now()}   => QR_CODE is not present on the page!")
            del button_list
            return False
        print(f"{datetime.now()}   => QR_CODE is present on the page!")

        print(f"{datetime.now()}   QR_CODE scroll =>")

        self.browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[0]
        )

        # self.element_is_clickable(button_list[0], 5)

        try:
            # button_list[0].click()
            # img = cv2.imread('')
            # reader = zxing.BarCodeReader()
            # print(reader.zxing_version, reader.zxing_version_info)
            # barcode = reader.decode("download.png")
            # print(barcode.raw)


            # # Name of the QR Code Image file
            # filename = "pages/Elements/1.png"
            # # read the QRCODE image
            # image = cv2.imread(filename)
            # # initialize the cv2 QRCode detector
            # detector = cv2.QRCodeDetector()
            # # detect and decode
            # data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
            # # if there is a QR code
            # # print the data
            # try:
            #     print("QRCode data:")
            #     print(data)
            # except Exception as e:
            #     print(e)




            # qreader = QReader()
            # # image = cv2.cvtColor(cv2.imread("pages/Elements/download.png"), cv2.COLOR_BGR2RGB)
            # image = cv2.cvtColor(cv2.imread("pages/Elements/output.png"), cv2.COLOR_BGR2RGB)
            # decoded_text = qreader.detect_and_decode(image=image)
            # print(f"decoded_text_is: {decoded_text}")


            qr_code = self.browser.find_element(*self.locator)
            src = qr_code.get_attribute('src')
            # download the image
            print(f"{datetime.now()}   => QR_CODE download started.")
            urllib.request.urlretrieve(src, f"test_data/{self.filename}.png")
            print(f"{datetime.now()}   => QR_CODE downloaded.")
            print(f"{datetime.now()}   => QR_CODE scanning started.")

            # Load QR code image
            reader = barcode.barcoderecognition.BarCodeReader(f"test_data/{self.filename}.png")

            # Read QR codes
            recognized_results = reader.read_bar_codes()

            # Show results
            # for x in recognized_results:
            #     print("Code Text: " + x.code_text)
            #     print("Type: " + x.code_type_name)
            for x in recognized_results:
                url_end = x.code_text.find(" ")
                url_2 = x.code_text[0:url_end]
            self.browser.get(url_2)
            os.remove(f"test_data/{self.filename}.png")


            print(f"{datetime.now()}   => QR_CODE scanned!")
        except ElementClickInterceptedException:
            print(f"{datetime.now()}   => QR_CODE NOT CLICKED")
            print(f"{datetime.now()}   'Sign up' form or page is auto opened")

        del button_list
        return True
