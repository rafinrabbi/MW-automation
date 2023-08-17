from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

# driver.implicitly_wait(50)
driver.find_element(By.NAME, 'email').send_keys('habeva1274@devswp.com')
driver.find_element(By.NAME, 'password').send_keys('g8pVzvZ5xwn7ULy!')

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

driver.implicitly_wait(30)

# clicking library
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div/div[2]/button[2]").click()
# clicking universal menu
driver.find_element(By.CLASS_NAME, "universal-icon").click()
# clicking accounts option from universal menu
driver.find_element(By.CSS_SELECTOR, "div[title='Accounts']").click()
# clicking create new portal button
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div[2]/div/form/div[2]/button[1]").click()
# write data in input field
portal_field = driver.find_element(By.ID, "rename")
portal_field.clear()
portal_field.send_keys("SeleniumT2")
# clicking done button
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/button[2]").click()
time.sleep(50)
