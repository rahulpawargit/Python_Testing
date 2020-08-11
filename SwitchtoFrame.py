from selenium import webdriver
import time
from selenium.webdriver.common.by import By



class switchframe():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")


        driver.get("https://learn.letskodeit.com/p/practice/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0,1000);")

        driver.switch_to.frame("courses-iframe")
        driver.find_element_by_id("search-courses").send_keys("Testing")
        time.sleep(3)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000)")
        time.sleep(3)


obj=switchframe()
obj.test()