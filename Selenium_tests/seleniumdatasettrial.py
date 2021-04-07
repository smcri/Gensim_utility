from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/")

print(browser.find_elements_by_xpath("//*[contains(text(), 'Choose Datasets')]"))
browser.find_elements_by_xpath("//*[contains(text(), 'Choose Datasets')]")[0].click()

browser.find_element_by_xpath("//select[@name='pd1']/option[text()='AirQuality']").click()

browser.find_elements_by_xpath("//*[contains(text(), 'Submit')]")[0].click()
browser.find_elements_by_xpath("//*[contains(text(), 'Submit')]")[2].click()

browser.find_elements_by_xpath("//*[contains(text(), 'Generate Result')]")[0].click()

WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@name='generated-reports']"))).click()

#print(browser.find_elements_by_xpath("//*[contains(text(), 'Learn More')]"))
#browser.find_elements_by_xpath("//*[contains(text(), 'Learn More')]")[1].click()