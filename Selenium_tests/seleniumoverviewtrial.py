from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/")

print(browser.find_elements_by_xpath("//*[contains(text(), 'Overview')]"))
browser.find_elements_by_xpath("//*[contains(text(), 'Overview')]")[1].click()

print(browser.find_elements_by_xpath("//*[contains(text(), 'Learn More')]"))
browser.find_elements_by_xpath("//*[contains(text(), 'Learn More')]")[1].click()