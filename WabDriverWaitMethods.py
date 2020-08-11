from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())

#Alert to be present
# driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
# driver.find_element(By.NAME, 'proceed').click()
#
# wait = WebDriverWait(driver, 10)
#
# alr = wait.until(ec.alert_is_present())
# print(alr.text)
# alr.accept()


# Element to be cliclabele
driver.get('https://app.hubspot.com/login')

wait = WebDriverWait(driver, 20)
link = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Sign up')))
link.click()
wait = WebDriverWait(driver, 20)
firstname = wait.until(ec.presence_of_element_located((By.NAME, 'uid-firstName-5')))
firstname.send_keys('Rahul')