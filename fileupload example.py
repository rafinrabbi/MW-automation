from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

# driver.implicitly_wait(50)
driver.find_element(By.NAME, 'email').send_keys('******')
driver.find_element(By.NAME, 'password').send_keys('*******')

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

# Wait for the new page to load (you can adjust the wait time as needed)
driver.implicitly_wait(30)

driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div/div[2]/button[2]").click()
time.sleep(10)
try:
        # Hover over the element
        hover_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[1]')
        ActionChains(driver).move_to_element(hover_element).perform()

        # Click the button after hovering
        try:
            button_to_click = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[2]/div[2]/button[1]')
            button_to_click.click()
            driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[4]/div[2]/div[1]/div[2]/div/div[1]/button').click()

        except Exception as nested_exception:
            print("Error while clicking the button after hovering:", nested_exception)

except Exception as hover_exception:
    print("Error while hovering over the element:", hover_exception)

driver.implicitly_wait(30)

# Specify the file path to upload
file_path = r"c:\Users\rawha\Downloads\Rawhatur.jpg"
try:
    driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/input").send_keys(file_path)
    time.sleep(20)
    driver.save_screenshot("screenshot3.png")

except:
    print("failed to upload")

# driver.implicitly_wait(30)

driver.quit()
