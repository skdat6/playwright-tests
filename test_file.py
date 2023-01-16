
import pytest
import asyncio
from playwright.sync_api import Playwright, sync_playwright, expect



BASE_URL = "http://uitestingplayground.com/"
PASSWORD = "pwd"
USERNAME = "theo"
IMOB_URL = "https://www.imobiliare.ro/"


### FUNCTIONS ###



### RUNNING ###
with sync_playwright() as playwright:    
        def test_login(playwright) -> None:
                browser = playwright.chromium.launch(headless=False, slow_mo=50)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.get_by_role("link", name="Sample App").click()
                page.get_by_placeholder("User Name").click()
                page.get_by_placeholder("User Name").fill(USERNAME)
                page.get_by_placeholder("********").click()
                page.get_by_placeholder("********").fill(PASSWORD)
                page.locator("section").click()
                page.get_by_placeholder("********").click()
                page.get_by_placeholder("********").fill("pwd")
                page.get_by_role("button", name="Log In").click()
                page.get_by_text("Welcome, theo!").click()

        def test_scrollbars(playwright):
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.click('text=Scrollbars')
                page.click('#hidingButton')
        
        ## Record click with dynamic id
        def test_button_dynamic_id(playwright):
                browser = playwright.chromium.launch(headless=False)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.click('text=Dynamic ID')
                context.tracing.start(screenshots=True, snapshots=True, sources=True)
                page.get_by_role("button", name="Button with Dynamic ID").click()
                context.tracing.stop(path = "trace.zip")
                
        def test_button_blue(playwright):
                browser = playwright.chromium.launch(headless=False, slow_mo=100)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.click('text=Class Attribute')
                context.tracing.start(screenshots=True, snapshots=True, sources=True)
                popup_handler(page, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
                context.tracing.stop(path = "trace.zip")
        
        ##WAIT FOR PAGE LOAD AND ELEMENT TO BE VISIBLE
        def test_wait_for_load(playwright):
                browser = playwright.chromium.launch(headless=False, slow_mo=100)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.click('text=Load Delay')
                element = page.wait_for_selector("body > section > div > button")
                locator = page.locator("body > section > div > button")
                expect(locator).to_be_visible()
                
        ## FIND MATCHING DATA AFTER BUTTON IS CLICKED AND IS WAITING FOR ELEMENT TO APPEAR        
        def test_wait_for_ajax_data(playwright):
                browser = playwright.chromium.launch(headless=False, slow_mo=100)
                context = browser.new_context()
                page = context.new_page()
                page.goto(BASE_URL)
                page.click('text=AJAX Data')
                page.locator("#ajaxButton").click()
                page.wait_for_selector("#content > p")
                locator = page.locator("#content > p")
                expect(locator).to_contain_text('Data loaded with AJAX get request.')

                

        #### POP UP HANDLER - 2 ARGS, page and el where is the element actioned that triggered the pop up ####        
        def popup_handler(page, el):
                page.once("dialog", lambda dialog: dialog.dismiss())
                page.locator(el).click()



