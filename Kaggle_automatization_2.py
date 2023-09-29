import undetected_chromedriver as uc
import random
import time
import os
import sys
from selenium.webdriver.common.keys import Keys
from secrets import GMAIL, PASSWORD

chrome_options = uc.ChromeOptions()

chrome_options.add_argument("--disable-extensions")

chrome_options.add_argument("--disable-popup-blocking")

chrome_options.add_argument("--profile-directory=Default")

chrome_options.add_argument("--disable-plugins-discovery")

chrome_options.add_argument("--incognito")

chrome_options.add_argument("user_agent=DN")

driver = uc.Chrome(options=chrome_options)

driver.delete_all_cookies()

#driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(GMAIL)
#driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.RETURN)

#time.sleep(2)

#driver.find_element_by_name('password').send_keys(PASSWORD + Keys.RETURN)

#time.sleep(10)

#driver.find_element_by_id("step1").click()

#time.sleep(2)

#driver.find_element_by_xpath('//*[@id="scopesContainer"]/li[2]').click()

#time.sleep(2)

#driver.find_element_by_id('//*[@id="scopesContainer"]/li[2]/span').click()

#time.sleep(2)

#driver.find_element_by_id("authorizeApisButton").click()

#time.sleep(2)

#driver.get("https://kaggle.com")

#time.sleep(25)

driver.get("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F")

time.sleep(1.3)

driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/form/div[2]/div[1]/div/div/input').send_keys(GMAIL)

time.sleep(1.7)

driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/form/div[2]/div[2]/div/div/input').send_keys(PASSWORD)

time.sleep(1.5)

driver.find_element_by_xpath('/html/body/main/div[1]/div[1]/div/form/div[2]/div[3]/button').click()

time.sleep(10)