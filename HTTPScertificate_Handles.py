from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
# #
driver.get("https://expired.badssl.com")
option = Options()
# # # option.add_argument('allow-running-insecure-content')
# # # option.add_argument('--ignore-certificate-errors')
handlSSLErr = DesiredCapabilities.CHROME.copy()
handlSSLErr['acceptInsucureCerts']=True

print(driver.find_element(By.TAG_NAME, 'h1').text)


#Firefox
# driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("https://expired.badssl.com")
# desired_capabilities = DesiredCapabilities.FIREFOX.copy()
# desired_capabilities['acceptInsucureCerts']=True
# print (driver.find_element(By.TAG_NAME, 'h1').text)



