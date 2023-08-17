from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.masterwizr.com/")

driver.implicitly_wait(50)
driver.find_element(By.NAME, 'email').send_keys('*********')
driver.find_element(By.NAME, 'password').send_keys('*************')

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()
driver.implicitly_wait(50)
actual_headline = driver.find_element(By.TAG_NAME, 'h1').text

print(actual_headline)
expected_headline = "Welcome to the MASTER Hub"

if actual_headline == expected_headline:
    print("passed")
else:
    xpath = '//*[@id="root"]/div[1]/div/div[2]/div[3]/div/div[3]/div[3]/div/div[2]/div[2]/div/div[1]/h2'

    # Find the element using the correct XPath
    element = driver.find_element(By.XPATH, xpath)

    # Get the text of the element
    element_text = element.text

    # Check if the text contains the desired string
    desired_text = 'Choose a payment plan'
    if desired_text in element_text:
        print("License needed to login")
    else:
        print("Error happens")

driver.quit()
