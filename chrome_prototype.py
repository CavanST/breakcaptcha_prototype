from selenium import webdriver

options = webdriver.ChromeOptions()  # (DebanjanB, 2020)
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # (DebanjanB, 2020)
options.add_experimental_option('useAutomationExtension', False)  # (DebanjanB, 2020)
# replace <user> with windows username
options.add_argument("user-data-dir=C:\\Users\\<user>\\AppData\\Local\\Google\\Chrome\\User Data")  # Adapted from: (MadRabbit, 2015)
# replace executable_path with path to chromedriver
driver = webdriver.Chrome(options=options, executable_path=r'C:\Webdrivers\chromedriver.exe')  # Adapted from: (DebanjanB, 2020)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {  # (Elias Vargas, 2020)
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# Launches page with navigator.webdriver set to undefined.
driver.get("https://www.google.com/recaptcha/api2/demo")

"""
REFERENCES:

DebanjanB, Elias Vargas., (2020). Selenium webdriver: Modifying navigator.webdriver flag to prevent selenium detection. [online].
Stack Overflow. [Viewed 18 June 2020]. Available from:
https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec

MadRabbit., (2015). How to load default profile in chrome using Python Selenium Webdriver?. [online].
Stack Overflow. [Viewed 18 June 2020]. Available from:
https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver

"""

"""
LINE COUNT

Total:      13
Reused:     0 (0 referenced)
Written:    1
Referenced: 12

"""
