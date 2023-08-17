from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Set an implicit wait of 10 seconds

driver.get("https://exifdata.com/")

file_path = r"C:/Capturess.jpg"

try:
    # file_input = driver.find_element(By.NAME, "upfile")
    driver.find_element(By.XPATH, "//*[@id='content']/div/div/form[1]/input[1]").send_keys(file_path)
    driver.save_screenshot("screenshot2.png")
    print("Done")

except NoSuchElementException:
    print("File input element not found")

driver.quit()
