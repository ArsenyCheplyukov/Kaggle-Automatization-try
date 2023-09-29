from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import random
from secrets import PASSWORD, GMAIL

def random_delay():
    time.sleep(random.uniform(0.5,3))

def configure_firefox():
    profile = webdriver.FirefoxProfile()
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15')
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument('--disable-blink-featuresi=AutomationControlled')
    profile.set_preference('excludeSwitches', 'enable-automation')
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    options.add_argument('--disable-blink-features')
    profile.set_preference("dom.webdriver.enabled", False)
    profile.set_preference('useAutomationExtension', False)
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile, firefox_options=options, executable_path='c:\WebBrowser\geckodriver.exe')

def configure_google():
    return webdriver.Chrome(executable_path='c:\WebBrowser\chromedriver.exe')

def login_kaggle(driver):
    driver.get("https://www.kaggle.com/")
    random_delay()
    python_button = driver.find_elements_by_xpath('//button[@role="button" and @tabindex="0" and @class="sc-psCJM hqBjyr"]')[0]
    python_button.click()
    random_delay()
    python_button = driver.find_elements_by_xpath('//div[@class="sc-qXJnB lgqvqD"]')[0]
    python_button.click()
    random_delay()
    text_request = driver.find_elements_by_xpath('//input[@id="identifierId"]')[0]
    text_request.send_keys("cheplucov32@gmail.com")
    random_delay()
    python_button = driver.find_elements_by_xpath('//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b"]')[0]
    python_button.click()

def login_google(driver):
    driver.get("https://www.gmail.com")
    driver.implicitly_wait(1)
    driver.find_element_by_name("identifier").send_keys(GMAIL+Keys.ENTER)
    driver.implicitly_wait(4)
    driver.find_element_by_name("password").send_keys(PASSWORD)
    driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()

driver = configure_google()

login_google(driver)

sleep(25)

