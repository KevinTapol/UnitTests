# https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim

# pip install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# search dom by class id etc
from selenium.webdriver.common.by import By

# allows us to type keys like ENTER
from selenium.webdriver.common.keys import Keys

# allows us to wait for the presence of an element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# software that controls chrome for us
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

# this will look for text contained in an anchor tag
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(10)

driver.quit()