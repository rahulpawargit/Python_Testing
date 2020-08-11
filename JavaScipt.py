from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.get('https://www.amazon.in/')
# driver.implicitly_wait(10)
#
# mobile = driver.find_element(By.LINK_TEXT,'Mobiles')
# driver.execute_script("arguments[0].click();", mobile)
# title = driver.execute_script("return document.title")
# driver.execute_script("arguments[0].style.border = '4px solid red';", mobile)
# print(title)

# Send Keys

driver.get('https://app.hubspot.com/login')
driver.implicitly_wait(10)

email = driver.find_element(By.ID, 'username')
driver.execute_script("document.getElementById('username').value='rahul.pawar', email;")

