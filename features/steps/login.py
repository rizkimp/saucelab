from behave import *
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *

@given(u'in login page')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.form_login)

@when(u'enter valid username and password')
def step_impl(context):
    username = context.config.userdata.get("username")
    password = context.config.userdata.get("password")
    context.browser.find_element(By.ID,locator.input_username).send_keys(username)
    context.browser.find_element(By.ID,locator.input_password).send_keys(password)

@when(u'click button login')
def step_impl(context):
    context.browser.find_element(By.ID,locator.button_login).click()

@then(u'success login')
def step_impl(context):
    url_home = context.config.userdata.get("home")
    context.browser.implicitly_wait(10)
    home = context.browser.current_url
    assert_that(home,contains_string(url_home))
