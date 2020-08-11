from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common import alert



class Alerthamdle():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")


        driver.get("https://learn.letskodeit.com/p/practice/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_id("alertbtn").click()
        time.sleep(2)
        alert1=driver.switch_to.alert
        alert1.accept()

        driver.find_element_by_id("confirmbtn").click()
        alert2 = driver.switch_to.alert
        time.sleep(2)
        alert2.accept()

        driver.find_element_by_id("confirmbtn").click()
        alert3=driver.switch_to.alert
        time.sleep(2)
        alert3.dismiss()





obj=Alerthamdle()
obj.test()
