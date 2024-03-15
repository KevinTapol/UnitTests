# https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim
# 29:02

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

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()