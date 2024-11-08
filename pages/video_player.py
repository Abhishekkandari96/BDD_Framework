from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class VideoPlayer:
    def __init__(self, driver):
        self.driver = driver

    def pause_video(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.SPACE).perform()
        sleep(10)


    def continue_watching(self):
        continue_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Continue Watching']//button")))
        continue_button.click()

    def set_volume(self, level):
        action = ActionChains(self.driver)
        for i in range(10):
            action.send_keys(Keys.ARROW_UP).perform()
            sleep(0.3)
        for i in range(level):
            action.send_keys(Keys.ARROW_DOWN).perform()
            sleep(0.3)

    def change_resolution(self, resolution):
        action = ActionChains(self.driver)
        action.send_keys(Keys.SPACE).perform()
        action.send_keys(Keys.SPACE).perform()
        for i in range(6):
            action.send_keys(Keys.TAB).perform()
            sleep(0.3)
        action.send_keys(Keys.ENTER).perform()
        numb=0
        if  resolution=='720p': numb=2
        elif   resolution=='480p': numb=3
        elif resolution == '360p': numb = 4
        for i in range(numb):
                action.send_keys(Keys.ARROW_DOWN).perform()
                sleep(0.3)
        action.send_keys(Keys.ENTER).perform()


    def exit_video(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.SPACE).perform()
        sleep(10)
        back_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Go Back and continue playing video']")))
        sleep(10)
        back_button.click()
