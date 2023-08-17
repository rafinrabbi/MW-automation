import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a CSV file to store the results
csv_file = open("login_results.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Email", "Message"])

# Read email and password pairs from the text file
with open("login_credentials.txt", "r") as credentials_file:
    for line in credentials_file:
        email, password = line.strip().split()
        
        driver = webdriver.Chrome()
        driver.get("https://accounts.masterwizr.com/")

        try:
            driver.find_element(By.NAME, 'email').clear()  # Clear the email field
            driver.find_element(By.NAME, 'email').send_keys(email)
            driver.find_element(By.NAME, 'password').send_keys(password)
            driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
            time.sleep(10)

            # print("*"*8,driver.current_url)
            if "https://accounts.masterwizr.com/hub/home" in driver.current_url:
                message = "passed"

            else:
                xpath = '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[3]/div[3]/div/div[2]/div[2]/div/div[1]/h2'
                element = driver.find_element(By.XPATH, xpath)

                element_text = element.text
                desired_text = 'Choose a payment plan'
                if desired_text in element_text:
                    message = "License needed"
                else:
                    message = "Error happens"

            csv_writer.writerow([email, message])

        finally:
            driver.quit()  

csv_file.close()
