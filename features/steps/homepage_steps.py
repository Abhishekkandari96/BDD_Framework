from itertools import repeat

from behave import given, when, then
from pages.home_page import HomePage
import time

@given(u"Iam at homepage")
def initialise_homepage(context):
    # homepage initialisation
    context.home_page = HomePage(context.driver)

@given(u"I navigate to the Test Automation Project")
def step_navigate_to_project(context):
    # Navigate to the 'Test Automation Project':
    context.home_page.select_test_automation_project()

@then(u"I switch to the Details tab")
def step_switch_to_details_tab(context):
    # Switch to the 'Details' Tab:
    context.home_page.click_details_tab()
    # waiting as per requirement document
    time.sleep(10)

@then(u"I return to the Videos tab")
def step_return_to_videos_tab(context):
    # Return to the 'Videos' Tab:
    context.home_page.click_videos_tab()

@then(u"I play the video")
def step_play_video(context):
    # Play the Video:
    context.home_page.play_video()
    # waiting as per requirement document
    time.sleep(10)

@then(u"I log out of the platform")
def step_log_out(context):
    #  Logout:
    context.home_page.logout_from_OTT()
