from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os

load_dotenv('./env')

# if os.environ.get("ENV") == "production":
#     CHROME_DRIVER = os.environ.get("SELENIUM_WEB_DRIVER_PATH_PROD")
# else:
#      CHROME_DRIVER = os.environ.get("SELENIUM_WEB_DRIVER_PATH_PROD")

driver = webdriver.Chrome()

driver.get("https://linkedin.com")

email = driver.find_element_by_xpath('//*[@id="session_key"]')
password = driver.find_element_by_xpath('//*[@id="session_password"]')
sign_in = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button')

email.send_keys("panampraisehebron@gmail.com")
password.send_keys('dontmesswithme101')
sign_in.click()

code = str(input("Please enter the code sent to your email: "))


driver.get("https://linkedin.com/mynetwork/")

buttons = driver.find_element(by='name', value='button')
for button in buttons:
    if "Invite" and "Connect" in button.aria_label:
        button.click()