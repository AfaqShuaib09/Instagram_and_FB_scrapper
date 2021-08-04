# Facebook Gallery Photo save Automation
# Facebook scrapper

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time

# To Disable Alerts from chrome
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs",prefs)

driver_path = 'C:/Users/chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=chrome_options)
driver.get('https://web.facebook.com/')

# name attribute of input field
email_field = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "input[name='email']")))
password = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "input[name='pass']")))
email_field.clear()
password.clear()
# Enter your email in below key
email_field.send_keys("afaq.shoaib09@gmail.com")
# Enter your password in below key
password.send_keys('*********')

login = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                       "button[type='submit']"))).click()
time.sleep(5)
images = list()
for i in ['photos_by', 'photos_of']:
    driver.get(f"https://www.facebook.com/afaq.shoaib.9/{i}/")
    time.sleep(5)

    count_scrolls = 2
    for j in range(0, 2):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(5)
        anchors_tag = driver.find_elements_by_tag_name('a')
        anchors_tag = [a.get_attribute('href') for a in anchors_tag]
        anchors_tag = [a for a in anchors_tag if str(a).startswith('https://web.facebook.com/photo')]

        for a in anchors_tag:
            driver.get(a)
            time.sleep(5)
            img = driver.find_elements_by_tag_name('img')
            images.append(img[1].get_attribute('src'))

print('I scraped ' + str(len(images)) + ' images!')

# Making Directory for storing images
path = os.getcwd()
print(f'Images files stored to: {path}')
path = os.path.join(path, "FB_SCRAPED_IMAGES")
os.mkdir(path)

# storing images using wget module
counter = 1
for img in images:
    filename_path = os.path.join(path,str(counter) + '.jpg')
    wget.download(img, filename_path)
    counter += 1





