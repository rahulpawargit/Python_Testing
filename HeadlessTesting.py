from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


#Chome Headless
options= webdriver.ChromeOptions()
# options.headless = False
options.add_argument('--incognito')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get("https://lngphase2:ueFAe4s94Q_L@lng.qa.asentechdev1.com")
print(driver.title)

#Firefox

# options = webdriver.FirefoxOptions()
#
# options.headless = True
#
# driver = webdriver.Firefox (executable_path= GeckoDriverManager().install(), options=options)
#
# driver.get("https://lngphase2:ueFAe4s94Q_L@lng.qa.asentechdev1.com")
# print(driver.title)