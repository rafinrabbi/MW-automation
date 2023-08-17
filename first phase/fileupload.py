from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

# driver.implicitly_wait(50)
driver.find_element(By.NAME, 'email').send_keys('habeva1274@devswp.com')
driver.find_element(By.NAME, 'password').send_keys('g8pVzvZ5xwn7ULy!')

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

# Wait for the new page to load (you can adjust the wait time as needed)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div/div[2]/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div[1]/div[4]/div[1]/div/div[2]/p").click()
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[1]").click()
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div[2]/button").click()
# driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"Downloads\Capturess.PNG")

driver.implicitly_wait(30)

# Specify the file path to upload
file_path = r"C:/Capturess.jpg"
try:
    driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/input").send_keys(file_path)
    driver.save_screenshot("screenshot3.png")
    time.sleep(50)

except:
    print("failed")

driver.implicitly_wait(30)

driver.quit()
