import time
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options

# launch browser and load web page
# profile = webdriver.FirefoxProfile()
# profile.set_preference("general.useragent.override",
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0")

# setup profile 1
profile = webdriver.FirefoxProfile('C:\\Users\\Cavan\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\wb7o96xx.default-release')
PROXY_HOST = "51.38.71.101"
PROXY_PORT = "8080"
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("network.proxy.http", PROXY_HOST)
# profile.set_preference("network.proxy.http_port", int(PROXY_PORT))
profile.set_preference("dom.webdriver.enabled", False)
# profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX
driver1 = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired)

# setup profile 2
# profile2 = webdriver.FirefoxProfile('C:\\Users\\Cavan\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\jxkpet14.default')
# PROXY_HOST = "51.38.71.101"
# PROXY_PORT = "8080"
# profile2.set_preference("network.proxy.type", 1)
# profile2.set_preference("network.proxy.http", PROXY_HOST)
# profile2.set_preference("network.proxy.http_port", int(PROXY_PORT))
# profile2.set_preference("dom.webdriver.enabled", False)
# profile2.set_preference('useAutomationExtension', False)
# profile2.update_preferences()
# desired2 = DesiredCapabilities.FIREFOX
# driver2 = webdriver.Firefox(firefox_profile=profile2, desired_capabilities=desired2)

counter1 = 0
# counter2 = 0
for i in range(1, 25):
    # switch browser profile after each reCAPTCHA
    # if i % 2 == 0:
    counter1 += 1
    print("Profile 1 Test: ", counter1)
    driver = driver1
    # else:
    #     counter2 += 1
    #     print("Profile 2 Test: ", counter2)
    #     driver = driver2
    # driver = driver2

    # open new tab
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

    driver.get("https://www.google.com/recaptcha/api2/demo")
    # driver.execute_async_script("navigator.webdriver = undefined;")

    # set cookie and print cookies
    # cookie = {'name': 'foo', 'value': 'bar'}
    # driver.add_cookie(cookie)
    # print(driver.get_cookies())

    # get iframe location
    iframe = driver.find_elements_by_css_selector("iframe")[0]  # find iframe
    # frameLocation = iframe.location  # get iframe location - returns dictionary with x and y as keys
    # print("Frame Location:", frameLocation)  # can click recaptcha from here

    # wait for iframe to load
    Wait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//iframe')))

    # find recaptcha checkbox and get location within iframe and size (useful later for mouse movement?)
    # recaptcha = driver.find_element_by_id("recaptcha-anchor")
    # recaptchaLocation = recaptcha.location
    # size = recaptcha.size
    # print("Size:", size)

    # calculate page location of recaptcha
    # xPos = float(frameLocation['x']) + float(recaptchaLocation['x'])
    # yPos = float(frameLocation['y']) + float(recaptchaLocation['y'])
    # print("X position:", xPos)
    # print("Y position", yPos)
    # recaptcha.click()  # Here we get image recaptcha

    # exit iframe
    driver.switch_to.default_content()

    # move mouse
    actionChains = ActionChains(driver)
    # actionChains.move_by_offset(100, 250).perform()
    # actionChains.move_by_offset(int(frameLocation['x']), int(frameLocation['y'])).click().perform()

    # time.sleep(0.01)
    # actionChains.move_to_element(iframe).click().perform()  # alternative to jump to recaptcha click

    time.sleep(30)

    # driver.close()
