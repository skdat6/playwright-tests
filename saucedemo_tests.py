from datetime import time

import pytest
import asyncio
from playwright.sync_api import Playwright, sync_playwright, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


### FUNCTIONS ###


### TESTS ###

# LOGIN
def test_login(login_logout, input_username, input_password):
    page = login_logout
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(input_username)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(input_password)
    page.locator('#login-button').click()
    expect(page.locator('//*[@id="header_container"]/div[2]/span')).to_be_visible()


# SELECT DROPDOWN OPTION
def test_filter_a_to_z(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("az")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (A to Z)')


# SELECT DROPDOWN OPTION
def test_filter_z_to_a(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("za")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (Z to A)')


# SELECT DROPDOWN OPTION
def test_filter_price_lohi(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("lohi")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Price (low to high)')


# SELECT DROPDOWN OPTION
def test_filter_price_hilo(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("hilo")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Price (high to low)')


# ADD ITEM TO CART
def test_item_to_cart(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator('//*[@id="remove-sauce-labs-backpack"]')).to_be_visible()


# POP UP HANDLER - 2 ARGS, page and el where is the element actioned that triggered the pop up
def popup_handler(page, el):
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator(el).click()



