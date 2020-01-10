from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os 


def replaceKey(key):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    driver_options = Options()
    driver_options.add_argument("--headless")
    driver = webdriver.Chrome(dir_path + "/driver/chromedriver", options=driver_options)
    driver.get("https://supgrade.eu/api?method=replace&key="+key)
    sleep(5)
    response = driver.find_element_by_tag_name("body").get_attribute("innerHTML")
    return response