from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://popcat.click/')

for i in range(200):
    element = driver.find_element(By.CLASS_NAME, "cat-img").click()

