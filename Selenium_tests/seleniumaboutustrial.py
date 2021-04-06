from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/")

print(browser.find_elements_by_xpath("//*[contains(text(), 'About Us')]"))
browser.find_elements_by_xpath("//*[contains(text(), 'About Us')]")[0].click()
