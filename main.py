from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

driver.get("https://www.instagram.com/")

time.sleep(1)

email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
email.send_keys(EMAIL)

password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(5)
driver.get('https://www.instagram.com/cristiano/followers/')

time.sleep(2)
run = 10
while run > 0:
    time.sleep(2)
    scroll = driver.find_element(By.CSS_SELECTOR, '._aano button')
    scroll.send_keys(Keys.END)
    run -= 1

buttons = driver.find_elements(By.CSS_SELECTOR, '.x1dm5mii .x9f619 ._acan')
for i in buttons:
    time.sleep(2)
    i.click()