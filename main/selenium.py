from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os 


def replaceKey(key):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # import tweaks for deployment with heroku
    driver_options = webdriver.ChromeOptions()
    driver_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver_options.add_argument("--headless")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=driver_options)
    driver.get("https://supgrade.eu/api?method=replace&key="+key)
    sleep(5)
    response = driver.find_element_by_tag_name("body").get_attribute("innerHTML")
    return response