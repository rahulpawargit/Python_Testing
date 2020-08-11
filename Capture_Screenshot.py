from selenium import webdriver
import time



class CaptureSCR():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://learn.letskodeit.com/")

        driver.get("https://learn.letskodeit.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys("pwrahul@gmail.com")
        driver.find_element_by_name("user[password]").send_keys("12334")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@class='btn btn-primary btn-md login-button']").click()
        self.takescreenshot(driver)

    def takescreenshot(self,driver):

            filename=str(round(time.time()* 1000))+ " .png"
            folder = "E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\Screenshot\\"
            destinationfolder=folder+filename

            try:
                driver.save_screenshot(destinationfolder )
                print("Screenshot saved in ", destinationfolder)
            except:
                print("Folder not found")




obj=CaptureSCR()
obj.test()