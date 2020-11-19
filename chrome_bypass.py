from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("user-data-dir=C:\\Users\\Cavan\\Downloads\\Chrome\\Chrome\\User Data")
options.add_argument('--proxy-server=51.38.71.101:8080')

driver = webdriver.Chrome(options=options, executable_path=r'C:\Webdrivers\chromedriver.exe')

# options.add_argument("user-data-dir=C:\\Users\\Cavan\\AppData\\Local\\Google\\Chrome\\User Data")
# options.add_argument('--proxy-server=51.38.71.101:8080')
#
# driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\Cavan\Documents\NetBeansProjects\DarkWebCrawler\chromedriver.exe')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# Launches page with navigator.webdriver set to undefined. Can't bypass as I have no chrome browser history
driver.get("https://www.google.com/recaptcha/api2/demo")

# ck1 = {'name': 'GAPS', 'value': '1:5w235u_rt4OdRK9SKABqENMraLbErS1aGR00iE7hJpzHhcb9is5Sl-4oPsxZDeYPJuE1Da-gOMHmMkzuJH1fXnTq7Qi_7g:BEXOZ1cy6zAAlg3G'}
# ck2 = {'name': 'ACCOUNT_CHOOSER', 'value': 'AFx_qI4_YWZmrAc5FkBclKPELWXGpUqI4R6qwMRzuDgep-zLpV4y-D3bzmUz3HFyiWT0fkOElrzvOIcFPjINlYdzTduWHRkvyjfwUoJhAxw2gj_WlMuweNfiDATOwoPI6zgPnL6qXLmK25NrbsVS3KzmsUi7IqdAtw'}
# ck3 = {'name': 'LSID', 'value': 'o.console.cloud.google.com|s.GB|s.youtube|youtube:swdizRvGv5IPItwNg7ANtmu8hKmlB2adaE9iRSkCu7C8cyTX9DyYZ-Woh9EUFNY9zGL8uA.'}
# ck4 = {'name': 'SMSV', 'value': 'ADHTe-CiPQM74sDqBEBVWpuSwEga2dkaDlPlSdOMo2Q3xso4E-ERylfJf8VdUPWzVlYAhyJDDXEvSut1euDwnVTlfKBcXTb3X_uI1zTab35Zu-6wQaKaxO8'}
# ck5 = {'name': '__Host-3PLSID', 'value': 'o.console.cloud.google.com|s.GB|s.youtube|youtube:swdizRvGv5IPItwNg7ANtmu8hKmlB2adaE9iRSkCu7C8cyTXhyi0p7U5wzsgNGFuj12qgQ.'}
# ck6 = {'name': '__utma', 'value': '73091649.618681434.1579618410.1579618410.1579618410.1'}
# ck7 = {'name': '__utmz', 'value': '73091649.1579618410.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'}
# ck8 = {'name': 'COMPASS', 'value': 'drivev2=EPjAsPEFGqYBAAlriVfl00vkLHQFPY9bsZJkaU0mJWhUTsiD9EOeqzjqy_gKT2Diq5LC8CiccjT2eEAZxReNYYAvzHuToMJR8cf3myakUv5LhOi9zYeonTjLhphOi9bOufCQEYg6FPlW62BgIYil1kk_5uBXd0BoDvJ_yeactrfyY7rY_AnfsTEus7Xz2BsjGnEgYn5ca_YIdQrj8EGm5a5y0cP9_SNn5OOGOcuowQ'}
# ck9 = {'name': '_ga', 'value': 'GA1.3.1668579343.1580243571'}
# ck10 = {'name': '_gcl_au', 'value': '1.1.1715063474.1580243571'}
# ck11 = {'name': 'OSID', 'value': 'tAdizZ2E13R-lYbS3k_yrQWUmCdPNVc7-U6uTJ5bmqf6r7DOIG9_0Tazl3lAnlA-EKnhrQ.'}
# ck12 = {'name': '__Secure-OSID', 'value': ''}
# ck13 = {'name': 'APISID', 'value': 'ayWscFOX1uJLHwUq/ABSbj3ptCY_8jhtRv'}
# ck14 = {'name': 'CONSENT', 'value': 'YES+GB.en+20150913-13-0'}
# ck15 = {'name': 'HSID', 'value': 'AcT5rlbyyR3v0jqdP'}
# ck16 = {'name': 'NID', 'value': '196=PT_9BmS6pFqP0mjPtewErLzJhj3-apmeguNjY60w4WHXxhajpiEKovOByT6TtNrYfJzZ0ra_-6yIpmVLC8DtODnNds_gE6Zc7B962qVVXNhyD4ucBFf4WU5b7oKHM_f-Q2kkJjXTD0A9Wkcs2ihyWBOh5DvBEWXqG01hwFrNJ2c'}
# ck17 = {'name': 'SAPISID', 'value': 'c8k85kP-Mh7BiW41/AKKUFJW6xuuZvT3S9'}
# ck18 = {'name': 'SID', 'value': 'swdizXo3iJqYRfENYse9VTgUiXfArw4km-kAWr-ZFD6RifyBDlTuo3bRujSpbCypR3rS-w.'}
# ck19 = {'name': 'SSID', 'value': 'Azj728FNiGpo8jbr6'}
# ck20 = {'name': '__Secure-3PAPISID', 'value': 'c8k85kP-Mh7BiW41/AKKUFJW6xuuZvT3S9'}
# ck21 = {'name': '__Secure-3PSID', 'value': 'swdizXo3iJqYRfENYse9VTgUiXfArw4km-kAWr-ZFD6RifyBzyT5DlXIT7wwG45VoFN5-A.'}
# ck22 = {'name': '__Secure-APISID', 'value': 'ayWscFOX1uJLHwUq/ABSbj3ptCY_8jhtRv'}
# ck23 = {'name': '__Secure-HSID', 'value': 'AcT5rlbyyR3v0jqdP'}
# ck24 = {'name': '__Secure-SSID', 'value': 'Azj728FNiGpo8jbr6'}
# ck25 = {'name': '1P_JAR', 'value': '2020-2-1-16'}
# ck26 = {'name': 'SIDCC', 'value': 'AN0-TYuYTZ3lpTfos6NLibZkaZAMDC7sgsaqdifm_6LdB0zkrZHxuVZLY2e_zlLjZ4cbavvm2Eg'}
# ck27 = {'name': 'OTZ', 'value': '5293295_56_56_123900_52_436380'}
#
# driver.add_cookie(ck1)
# driver.add_cookie(ck2)
# driver.add_cookie(ck3)
# driver.add_cookie(ck4)
# driver.add_cookie(ck5)
# driver.add_cookie(ck6)
# driver.add_cookie(ck7)
# driver.add_cookie(ck8)
# driver.add_cookie(ck9)
# driver.add_cookie(ck10)
# driver.add_cookie(ck11)
# driver.add_cookie(ck12)
# driver.add_cookie(ck13)
# driver.add_cookie(ck14)
# driver.add_cookie(ck15)
# driver.add_cookie(ck16)
# driver.add_cookie(ck17)
# driver.add_cookie(ck18)
# driver.add_cookie(ck19)
# driver.add_cookie(ck20)
# driver.add_cookie(ck21)
# driver.add_cookie(ck22)
# driver.add_cookie(ck23)
# driver.add_cookie(ck24)
# driver.add_cookie(ck25)
# driver.add_cookie(ck26)
# driver.add_cookie(ck27)
