import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# initialize the webdriver, specify we're using the chrome browser
driver = webdriver.Chrome(executable_path="C:/Users/Dr. Ikedinma/PycharmProjects/100 Days of Python/chromedriver.exe")
# opens up the Chrome browser and go to the specified url
driver.get(url="https://www.yahoo.com")

# click the sign in link
signin_link = driver.find_element(By.XPATH, '//*[@id="ybar-inner-wrap"]/div[3]/div/div[3]/div[1]/div/a')
signin_link.click()

# focus on the email input and enter the email
email_input = driver.find_element(By.NAME, "username")
email_input.send_keys(os.environ["EMAIL"])

# click on the next button
next_button = driver.find_element(By.NAME, "signin")
next_button.click()

# focus on the password input and enter the password
password_input = driver.find_element(By.XPATH, '//*[@id="login-passwd"]')
password_input.send_keys(os.environ["PASSWORD"])

# click the next button
next_button = driver.find_element(By.NAME, "verifyPassword")
next_button.click()
