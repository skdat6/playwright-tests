from datetime import time

import pytest
import asyncio
from playwright.sync_api import Playwright, sync_playwright, expect

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


### FUNCTIONS ###


### RUNNING ###
def test_login(login_logout, input_username, input_password):
    page = login_logout
    page.goto(BASE_URL)
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(input_username)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(input_password)
    page.locator('#login-button').click()
    expect(page.locator('//*[@id="header_container"]/div[2]/span')).to_be_visible()


def test_filter_a_to_z(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("az")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (A to Z)')


def test_filter_z_to_a(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("za")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Name (Z to A)')


def test_filter_price_lohi(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("lohi")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Price (low to high)')


def test_filter_price_hilo(login_logout, input_username, input_password):
    page = login_logout
    test_login(login_logout, input_username, input_password)
    page.locator('//*[@id="header_container"]/div[2]/div[2]/span/select').select_option("hilo")
    expect(page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span')).to_contain_text('Price (high to low)')



#
# def test_filter_z_to_a(playwright):
#         browser = playwright.chromium.launch(headless=False, slow_mo=50)
#         context = browser.new_context()
#         page = context.new_page()
#         test_login(playwright)
#         page.locator('//*[@id="header_container"]/div[2]/div[2]/span/span').select_option("za")







    # def test_scrollbars(playwright):
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(BASE_URL)
    #     page.click('text=Scrollbars')
    #     page.click('#hidingButton')
    #
    #
    # ## Record click with dynamic id
    # def test_button_dynamic_id(playwright):
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(BASE_URL)
    #     page.click('text=Dynamic ID')
    #     context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #     page.get_by_role("button", name="Button with Dynamic ID").click()
    #     context.tracing.stop(path="trace.zip")
    #
    #
    # def test_button_blue(playwright):
    #     browser = playwright.chromium.launch(headless=False, slow_mo=100)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(BASE_URL)
    #     page.click('text=Class Attribute')
    #     context.tracing.start(screenshots=True, snapshots=True, sources=True)
    #     popup_handler(page, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    #     context.tracing.stop(path="trace.zip")
    #
    #
    # ##WAIT FOR PAGE LOAD AND ELEMENT TO BE VISIBLE
    # def test_wait_for_load(playwright):
    #     browser = playwright.chromium.launch(headless=False, slow_mo=100)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(BASE_URL)
    #     page.click('text=Load Delay')
    #     element = page.wait_for_selector("body > section > div > button")
    #     locator = page.locator("body > section > div > button")
    #     expect(locator).to_be_visible()
    #
    #
    # ## FIND MATCHING DATA AFTER BUTTON IS CLICKED AND IS WAITING FOR ELEMENT TO APPEAR
    # def test_wait_for_ajax_data(playwright):
    #     browser = playwright.chromium.launch(headless=False, slow_mo=100)
    #     context = browser.new_context()
    #     page = context.new_page()
    #     page.goto(BASE_URL)
    #     page.click('text=AJAX Data')
    #     page.locator("#ajaxButton").click()
    #     page.wait_for_selector("#content > p")
    #     locator = page.locator("#content > p")
    #     expect(locator).to_contain_text('Data loaded with AJAX get request.')


    #### POP UP HANDLER - 2 ARGS, page and el where is the element actioned that triggered the pop up ####
def popup_handler(page, el):
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator(el).click()



