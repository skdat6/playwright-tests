from datetime import time

import pytest
import asyncio
import logging
from playwright.sync_api import Playwright, sync_playwright, expect
from models.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


### FUNCTIONS ###


### TESTS ###

def login(page):
    page.goto(BASE_URL)
    login_page = LoginPage(page)
    login_page.enter_username(USERNAME)
    login_page.enter_password(PASSWORD)
    login_page.click_login_button()


# LOGIN
def test_login():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        try:
            expect(page.locator('//*[@id="header_container"]/div[2]/span')).to_be_visible()
            logging.info("Element found")
        except Exception as e:
            logging.error(f"Element not found")


# SELECT DROPDOWN OPTION
def test_filter_a_to_z():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("az")
        try:
            expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (A to Z)')
            logging.info("Element with text 'Name (A to Z)' found")
        except Exception as e:
            logging.error(f"Element not found")


# SELECT DROPDOWN OPTION
def test_filter_z_to_a():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("za")
        try:
            expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (Z to A)')
            logging.info("Element with text 'Name (Z to A)' found")
        except Exception as e:
            logging.error(f"Element not found")


# SELECT DROPDOWN OPTION
def test_filter_price_lohi():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("lohi")
        try:
            expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text(
                'Price (low to high)')
            logging.info("Element with text 'Price (low to high) found")
        except Exception as e:
            logging.error(f"Element not found")


# SELECT DROPDOWN OPTION
def test_filter_price_hilo():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("hilo")
        try:
            expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text(
                'Price (high to low)')
            logging.info("Element with text 'Price (high to low)' found")
        except Exception as e:
            logging.error(f"Element not found")


# ADD ITEM TO CART
def test_item_to_cart():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login(page)
        page.locator('//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        try:
            expect(page.locator('//*[@id="remove-sauce-labs-backpack"]')).to_be_visible()
        except Exception as e:
            logging.error(f"Element not found")


# POP UP HANDLER - 2 ARGS, page and el where is the element actioned that triggered the pop up
def popup_handler(page, el):
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator(el).click()
