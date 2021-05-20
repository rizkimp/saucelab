from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *

@given(u'there is first product')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.first_product)

@when(u'click button add to cart on first product')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.first_product_button_addtocart).click()

@then(u'first product is added in cart and counter')
def step_impl(context):
    one_product = context.browser.find_element(By.XPATH,locator.counter_shopping_cart).text
    assert_that(one_product,contains_string("1"))

@then(u'go to cart and click button checkout')
def step_impl(context):
    context.browser.find_element(By.ID,locator.icon_shopping_cart).click()
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.ID,locator.button_checkout).click()

@then(u'enter valid information and click button continue')
def step_impl(context):
    first = context.config.userdata.get("first_name")
    last = context.config.userdata.get("last_name")
    code =  context.config.userdata.get("postal_code")
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.ID,locator.input_first_name).send_keys(first)
    context.browser.find_element(By.ID,locator.input_last_name).send_keys(last)
    context.browser.find_element(By.ID,locator.input_postal_code).send_keys(code)
    context.browser.find_element(By.ID,locator.button_continue).click()

@then(u'redirect to checkout overview')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.first_cart_list)

@when(u'click button finish')
def step_impl(context):
    context.browser.find_element(By.ID,locator.button_finish).click()

@then(u'success checkout first product')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.thankyou_order)
    context.browser.find_element(By.ID,locator.button_back_home).click()
