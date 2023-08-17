from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

driver.implicitly_wait(50)
# driver.find_element(By.NAME, 'email').send_keys('habeva1274@devswp.com')
# driver.find_element(By.NAME, 'password').send_keys('g8pVzvZ5xwn7ULy!')

driver.find_element(By.NAME, 'email').send_keys('rawhaturrafin@gmail.com')
driver.find_element(By.NAME, 'password').send_keys('g8pVzvZ5xwn7ULy!')

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

# Wait for the new page to load (you can adjust the wait time as needed)
driver.implicitly_wait(30)

try:
    # Verify a welcome message element
    welcome_message = driver.find_element(By.XPATH, "//h1[contains(text(), 'Welcome to the MASTER Hub')]")
    print("Login successful")
except NoSuchElementException:
    print("Login failed")

# Close the WebDriver session
driver.quit()
