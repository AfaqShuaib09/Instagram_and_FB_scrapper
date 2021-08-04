# Task
"""how to log into your insta account
   How to search for specific hashtag
   How to save image from that specific hashtag on your pc
"""
import os
from selenium import webdriver
import time
import wget
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Download Chrome Driver corresponding to version of the chrome
driver_path = 'C:/Users/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('https://www.instagram.com/')

# name attribute of input field
username = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "input[name='username']")))
password = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "input[name='password']")))
username.clear()
password.clear()
# Enter your username in below key
username.send_keys("afaq_shoaib")
# Enter your password in below key
password.send_keys('*********')

login = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "button[type='submit']"))).click()
# // for contains text
save_login = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                          "//button[contains(text(),'Not Now')]"))).click()
save_login_2 = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                          "//button[contains(text(),'Not Now')]"))).click()
# @ for attribute
searchbox = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
hashtag = input("Enter #tag which you want to search: ")
searchbox.send_keys(hashtag)
time.sleep(5) # Wait 5 seconds
# my_link = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
# my_link.click()

driver.get("https://www.instagram.com/explore/tags/" + hashtag[1:] + "/")
time.sleep(5)
driver.execute_script("window.scrollTo(0,4000);")
images = driver.find_elements_by_tag_name('img')
images = [img.get_attribute('src') for img in images]

path = os.getcwd()
print(f'Images files stored to: {path}')
path = os.path.join(path, hashtag[1:]+'s')
os.mkdir(path)

counter = 1
for img in images:
    filename_path = os.path.join(path, hashtag[1:] + str(counter) + '.jpg')
    wget.download(img, filename_path)
    counter += 1