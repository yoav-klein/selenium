

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='ec2-44-211-197-185.compute-1.amazonaws.com:4444',
    options=options
)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

time.sleep(60)

driver.quit()