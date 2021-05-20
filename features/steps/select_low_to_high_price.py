from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *

@when(u'select low to high price')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.select_price_low_to_high).click()

@then(u'lowest price is in first list')
def step_impl(context):
    price = context.config.userdata.get("lowest_price")
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.first_product)
    lowest_price = context.browser.find_element(By.XPATH,locator.first_product_price).text
    assert_that(lowest_price,contains_string(price))
