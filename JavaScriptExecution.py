from selenium import webdriver
import time



class JavascriptExe():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        # driver.get("https://learn.letskodeit.com/")
        driver.execute_script("window.location= 'https://learn.letskodeit.com/';")

        #driver.get("https://learn.letskodeit.com/")
        driver.implicitly_wait(30)
        driver.maximize_window()

        #driver.find_element_by_link_text("Login").click()
        # element = driver.execute_script("return document.getElementByLinktext('Login');")
        # element.click()

        link = driver.find_element_by_link_text('Login')
        driver.execute_script("arguments[0].click();", link)
        time.sleep(5)

        textbox=driver.execute_script("return document.getElementById('user_email');")
        textbox.send_keys("username")
        time.sleep(3)
        # driver.find_element_by_id("user_email").send_keys("pwrahul@gmail.com")
        # driver.find_element_by_name("user[password]").send_keys("12334")
        # time.sleep(5)



obj=JavascriptExe()
obj.test()