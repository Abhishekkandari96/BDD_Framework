from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # Initialize ChromeDriver using Service
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--no-sandbox")  # Additional option for stability
    chrome_options.add_argument("--disable-dev-shm-usage")  # Useful for running in Docker or limited environments
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service,options=chrome_options)


def after_all(context):
    # Quit the driver after all tests are completed
    if hasattr(context, 'driver'):
        context.driver.quit()
