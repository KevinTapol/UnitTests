# Youtube by Tech With Time https://www.youtube.com/watch?v=NB8OceGZGjA&ab_channel=TechWithTim
# My target site is my client at https://sweettreatvixen.netlify.app/
# install selenium
# in terminal pip install selenium

# require
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# site for download chrome webdriver MUST BE SAME VERSION OF GOOGLE CHROME INSTANCE!!
# https://sites.google.com/chromium.org/driver/
# https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/win64/chromedriver-win64.zip

driver.get("https://sweettreatvixen.netlify.app/")

input_element = driver.find_element(By.CLASS_NAME, "")

time.sleep(10)

driver.quit()