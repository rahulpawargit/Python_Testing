from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class dynamicElement():

    def findelement(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://learn.letskodeit.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("pwrahul@gmail.com")
        driver.find_element_by_name("user[password]").send_keys("123456")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@class='btn btn-primary btn-md login-button']").click()


        #search
        driver.find_element_by_xpath("//input[@class='form-control search input-lg']").send_keys("Javascript")
        driver.find_element_by_xpath("//i[@class='fa fa-search']").click()
        time.sleep(10)

        _course=driver.find_element_by_xpath("//div[contains(@class, 'course-listing-title')and contains(text(),'{0}')]")
        _courselocation=_course.format("JavaScript for beginners")
        driver.find_element(By.XPATH,"_courselocation").click()
        time.sleep(10)




ff=dynamicElement()
ff.findelement()
