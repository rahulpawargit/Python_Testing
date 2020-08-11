from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(20)
# driver.delete_all_cookies()
driver.get("https://www.spicejet.com/default.aspx")
time.sleep(3)



"""Move to Element """

login_ele= driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
action= ActionChains(driver)
action.move_to_element(login_ele).perform()
# time.sleep(3)

spice_club_member= driver.find_element(By.LINK_TEXT, 'SpiceClub Members')
action.move_to_element(spice_club_member).perform()
time.sleep(3)

member_login=driver.find_element(By.LINK_TEXT, 'Member Login')
member_login.click()
time.sleep(3)

driver.quit()

