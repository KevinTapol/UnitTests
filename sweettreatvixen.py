# Youtube by Tech With Time https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim
# My target site is my client at https://sweettreatvixen.netlify.app/
# install selenium
# in terminal pip install selenium

# require
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# site for download chrome webdriver MUST BE SAME VERSION OF GOOGLE CHROME INSTANCE!!
# https://sites.google.com/chromium.org/driver/
# https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/win64/chromedriver-win64.zip

driver.get("https://sweettreatvixen.netlify.app/")

caterId = "experiment"
cakeId = "cakesID"
contactId = "contactForm"

time.sleep(3)

# this block of code waits for the Catering Navbar to show then clicks it open
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, caterId))
)
cater = driver.find_element(By.ID, caterId)
cater.click()

# time.sleep(3)
# this block of code waits for the Cakes button to show in the Catering Navbar then clicks it open
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.ID, cakeId))
# )
# cake = driver.find_element(By.ID, cakeId)
# cake.click()

time.sleep(3)
# this block of code waits for the Catering Navbar to be open and clicks Contacts
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, contactId))
)

contact = driver.find_element(By.ID, contactId)
contact.click()

# next step is to fill out the input form and then click submit

time.sleep(10)

# driver.quit()