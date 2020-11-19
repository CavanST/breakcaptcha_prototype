import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains

# load custom browser profile
profile = webdriver.FirefoxProfile('C:\\Users\\Cavan\\PycharmProjects\\wb7o96xx.default-release')  # Adapted from: (Gabriel Devillers, 2019)
# profile = webdriver.FirefoxProfile('C:\\Users\\Cavan\\Documents\\wb7o96xx.default-release')  # Adapted from: (Gabriel Devillers, 2019)

# set navigator.webdriver to false
profile.set_preference("dom.webdriver.enabled", False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

# initialize web driver
driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

# open a new tab
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')  # (Yi Zeng, 2013)

# visit reCAPTCHA demo website
driver.get("https://signup.heroku.com/")

# wait for iFrame to load
Wait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//iframe')))  # Adapted from: (DebanjanB, 2018)

# find iframe
iFrame = driver.find_elements_by_css_selector("iframe")[0]

# get iframe location - returns dictionary with x and y as keys
frameLocation = iFrame.location

# move mouse to reCAPTCHA and click it
actionChains = ActionChains(driver)
time.sleep(0.01)
actionChains.move_by_offset(int(frameLocation['x']), int(frameLocation['y'])).click().perform()
time.sleep(10)
# driver.close()

"""
REFERENCES:

Gabriel Devillers., (2019). How to load firefox profile with Python Selenium?. [online].
Stack Overflow. [Viewed 18 June 2020]. Available from:
https://stackoverflow.com/questions/50321278/how-to-load-firefox-profile-with-python-selenium

Yi Zeng., (2013). How to open a new tab using Selenium WebDriver?. [online].
Stack Overflow. [Viewed 18 June 2020]. Available from:
https://stackoverflow.com/questions/17547473/how-to-open-a-new-tab-using-selenium-webdriver

DebanjanB., (2018). Python Selenium: How to wait and switch to a dynamic iframe?. [online].
Stack Overflow. [Viewed 18 June 2020]. Available from:
https://stackoverflow.com/questions/51144220/python-selenium-how-to-wait-and-switch-to-a-dynamic-iframe

"""

"""
LINE COUNT

Total:      15
Reused:     0 (0 referenced)
Written:    12
Referenced: 3

"""
