from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def enter_pin(self, pin):
        button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "// span[ @class ='cc-1x4xm cc-sdm9t']")))
        button.click()
        pin_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='access-code']")))
        pin_input.send_keys(pin)

    def click_login(self):
        login_button =WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Sign In']")))
        login_button.click()
