from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

try:
    driver.find_element(By.NAME, 'email').send_keys('************')
    driver.find_element(By.NAME, 'password').send_keys('********')

    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    driver.implicitly_wait(30)

    try:
        # Click the first button
        button1 = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div[2]/div[3]/div/div[3]/div[1]/div/div[2]/button[2]")
        button1.click()

        # Click the nested button
        try:
            button2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/div[1]/button')
            button2.click()

            random_number = random.randint(10000, 99999)  # Generate a random 5-digit number
            random_text = f"SeleniumT{random_number}"
            
            input_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/form/div/input')
            input_element.send_keys(random_text)
            
            submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div[1]/form/div/button')
            submit_button.click()

        except Exception as nested_exception:
            print("Error while interacting with the nested button:", nested_exception)

    except Exception as button1_exception:
        print("Error while clicking the first button:", button1_exception)

except Exception as main_exception:
    print("Error in the main automation process:", main_exception)

finally:
    time.sleep(10)  # Ensure the browser window is open for a while
    driver.quit()
