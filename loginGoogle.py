import pickle
import pprint
import time
from selenium import webdriver

def load_cookies(driver, cookies):
    with open(cookies) as textFile:
        for line in [line.split() for line in textFile]:
            driver.add_cookie({'name': line[0], 'value': line[1], 'path': line[3], 'expiry': line[4]})

# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "cookies.pkl"

# Initial load of the domain that we want to save cookies for
# chrome = webdriver.Firefox(executable_path='C:\\webbrowser\\geckodriver.exe')
# chrome.get("https://www.hackerrank.com/login")
# chrome.find_element_by_xpath("//input[@id='login']").send_keys("infunig1986")
# chrome.find_element_by_xpath("(//input[@id='password'])[2]").send_keys("testuseraccount")
# chrome.find_element_by_xpath("(//button[@name='commit'])[2]").click()
# save_cookies(chrome, cookies_location)
# chrome.quit()

# Load of the page you cant access without cookies, this one will fail
# chrome = webdriver.Chrome()
# chrome.get("https://www.hackerrank.com/settings/profile")

# Load of the page you cant access without cookies, this one will go through
chrome = webdriver.Chrome(executable_path='chromedriver.exe')
load_cookies(chrome, cookies_location)
chrome.get("https://www.kaggle.com/")

# chrome = webdriver.Chrome()
# chrome.get("https://google.com")
# time.sleep(2)
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome, domains=["www.google.com"])
# pprint.pprint(chrome.get_cookies())
# print "=========================\n"
#
# delete_cookies(chrome)
# pprint.pprint(chrome.get_cookies())