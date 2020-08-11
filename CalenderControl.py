from selenium import webdriver
import time

class calender():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://www.expedia.co.in/")
        driver.maximize_window()
        driver.implicitly_wait(30)
        # flight=driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']//span[contains(@class,'uitk-icon uitk-icon-flights')]")
        # flight.click()
        # time.sleep(5)
        # driver.find_element_by_xpath("//input[@id='hotel-checkin-hp-hotel']").click()
        time.sleep(5)

        dates=driver.find_element_by_xpath("// div[@class ='datepicker-cal-month'][position()=1] // button[@ class ='datepicker-cal-date' and contains(text(),17)")
        dates.click()





obj=calender()
obj.test()