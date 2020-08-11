from selenium import webdriver
import time
from selenium.webdriver.common.by import By



class CaptureSCR():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")


        driver.get("https://learn.letskodeit.com/p/practice/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        windowhandle=driver.current_window_handle
        print(windowhandle)

        driver.find_element_by_id("openwindow").click()
        time.sleep(3)
        handles = driver.window_handles
        for hdl in handles:
            print(hdl)
            if hdl not in windowhandle:
               driver.switch_to.window(hdl)
               time.sleep(2)
               searchBox = driver.find_element(By.ID, "search-courses")
               searchBox.send_keys("python")

               time.sleep(3)
               driver.close()
               break
        driver.switch_to.window(windowhandle)
        time.sleep(3)



obj=CaptureSCR()
obj.test()