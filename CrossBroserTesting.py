from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

import time
# from selenium.webdriver.common.keys import Keys

browser ="safari"

if browser == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browser == 'firefox':
    driver = webdriver.Firefox (executable_path=GeckoDriverManager().install())
elif browser == 'edge':
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
elif browser == "IE":
    driver = webdriver.Ie(IEDriverManager().install())


else:
    print("Please enter brower name", browser)
    raise Exception("Driver not found")
driver.get("http://www.google.com")
# driver.find_element_by_name("q").send_keys("Naveen Automation Labs")
# driver.find_element_by_name("").send_keys(Keys.ENTER)


time.sleep(4)
