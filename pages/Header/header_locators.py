"""
-*- coding: utf-8 -*-
@Time    : 2023/02/08 10:00
@Author  : Alexander Tomelo
"""
from selenium.webdriver.common.by import By


class HeaderElementLocators:
	""" Locators for ..."""
	BUTTON_LOGIN = (By.CSS_SELECTOR, "div.cc-header__wrap > div#wphWrap a#wg_loginBtn")
	BUTTON_SIGNUP = (By.CSS_SELECTOR, ".cc-header__wrap > #wphWrap > .js_signup")
	BUTTON_MY_ACCOUNT = (By.ID, "wg_userarea")
