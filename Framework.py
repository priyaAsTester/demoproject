from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/")
driver.find_element(By.XPATH,"//input[@name='uid']").send_keys("mngr604283")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("AdUpuvy")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

