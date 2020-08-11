from selenium import webdriver
import time



class Findheightwidth():

    def test(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        # driver.get("https://learn.letskodeit.com/")
        driver.execute_script("window.location= 'https://learn.letskodeit.com/p/practice';")

        # #Find the Height and Widht
        # height=driver.execute_script("return window.innerHeight;")
        # widht= driver.execute_script("return window.innerWidth;")
        # print(height)
        # print(widht)

        #Scrool donw
        driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(3)

        #Scroll UP

        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)

        #Scroll element into view
        element=driver.find_element_by_id("mousehover")
        driver.execute_script("argument[0].scrollIntoView(true);", element)
        time.sleep(3)
        driver.execute_script("window.scrollBy(0, -150);")

        #Native way into view
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1000);")
        location=element.location_once_scrolled_into_view
        print(location)




obj=Findheightwidth()
obj.test()