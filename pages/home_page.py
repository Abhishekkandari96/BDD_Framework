from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def select_test_automation_project(self):
        project_button = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='Test automation project']")))
        project_button.click()

    def click_details_tab(self):
        details_tab = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "detailsSection")))
        details_tab.click()
        sleep(10)

    def click_videos_tab(self):
        videos_tab = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "videosSection")))
        videos_tab.click()

    def play_video(self):
        play_button = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Play Video']//*[name()='svg']")))
        play_button.click()
        sleep(10)


    def logout_from_OTT(self):
        logout_button = self.driver.find_element(By.XPATH, "//a[@id='signOutSideBar']")
        logout_button.click()
