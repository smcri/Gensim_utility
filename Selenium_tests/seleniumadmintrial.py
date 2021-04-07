from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

user_name = "admin"
password = "a1s2d3f4"

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/")

print(browser.find_elements_by_xpath("//*[contains(text(), 'Login')]"))
browser.find_elements_by_xpath("//*[contains(text(), 'Login')]")[2].click()

browser.find_element_by_id("id_username").send_keys(user_name)
browser.find_element_by_id("id_password").send_keys(password)
browser.find_element_by_id("id_password").send_keys(Keys.RETURN)
