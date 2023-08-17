from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

driver.implicitly_wait(50)
driver.find_element(By.NAME, 'email').send_keys('habeva1274@devswp.com')
driver.find_element(By.NAME, 'password').send_keys('g8pVzvZ5xwn7ULy!')
# driver.find_element(By.NAME, 'Login').click()
# driver.find_element(By.CLASS_NAME, 'sc-iHGNWf hFnguK').click()
driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
driver.implicitly_wait(50)
actual_headline = driver.find_element(By.TAG_NAME, 'h1').text

print(actual_headline)
expected_headline = "Welcome to the MASTER Hub"

#
# actual_title = driver.title
# expected_title = "OrangeHRM"


if actual_headline == expected_headline:
    print("passed")
else:
    print("failed")
# driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
