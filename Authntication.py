from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://lngphase2:ueFAe4s94Q_L@lng.qa.asentechdev1.com")
print(driver.title)
cookies= driver.get_cookies()

for ck in cookies:
    print(ck)
