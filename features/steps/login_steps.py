import json

from behave import given, when, then
from pages.login_page import LoginPage

# Load data from JSON file once and store it for use
with open('./data/data.json') as f:
    data = json.load(f)
    print(data)

@given(u"I am on the Indee login page")
def step_given_login_page(context):
    # opening URL
    context.driver.get(data["login"]["url"])
    context.login_page = LoginPage(context.driver)

@when(u"I log in using the provided PIN")
def step_log_in_with_pin(context):
    # # Log in using the provided PIN.
    context.login_page.enter_pin(data["login"]["pin"])
    context.login_page.click_login()
