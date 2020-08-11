from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# #implecitly Wait()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
#
# driver.get("https://app.hubspot.com/login")
# print(driver.title)
# #time.sleep(6)
# #implecitly wait is applies on web element only
# #need to delclare it on globly
# #we can overwrite it.
#
# user_name= driver.find_element(By.ID, 'username')
# user_name.send_keys('test@gmail.com')


#WebDriver Wait (Explicitly Wait)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 10)
wait.until(ec.title_contains('HubSpot'))
print(driver.title)

wait = WebDriverWait(driver, 10)
user_name = wait.until(ec.presence_of_element_located((By.ID,'username')))
user_name.send_keys('test@gmail.com')
