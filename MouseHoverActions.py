from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class mouse_hover():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")


        driver.get("https://learn.letskodeit.com/p/practice/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.execute_script('window.scrollBy(0,600);')
        time.sleep(3)
        element=driver.find_element_by_xpath("//button[@id='mousehover']")
        toplink=driver.find_element_by_xpath("//a[@href='#top']")

        try:
            action=ActionChains(driver)
            action.move_to_element(element).perform()
            time.sleep(3)
            print("Clicked on Mousehoever")
            action.move_to_element(toplink).click().perform()
            time.sleep(3)

        except:
            print("Elemet not found")

    def drag_drop(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")

        driver.get("https://jqueryui.com/droppable/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.switch_to.frame(0)
        from_element=driver.find_element_by_id("draggable")
        to_element=driver.find_element_by_id("droppable")

        try:
            action=ActionChains(driver)
            # action.drag_and_drop(from_element,to_element).perform()
            action.click_and_hold(from_element).move_to_element(to_element).release().perform()
            time.sleep(3)
            print("Item is moved")

        except:
            print("Elemets are not availabe")

    def slider(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")

        driver.get("https://jqueryui.com/slider/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.switch_to.frame(0)
        element= driver.find_element_by_id("slider")

        try:
            action=ActionChains(driver)
            action.drag_and_drop_by_offset(element,5000,0).perform()
            time.sleep(3)
            print("Elemetn is moved ")
        except:
            print("Slider process failes")


obj=mouse_hover()
# obj.test()
# obj.drag_drop()
obj.slider()
