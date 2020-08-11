
from  selenium import webdriver

class FindelementbyXpath_Css():


     driver=webdriver.Chrome(executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
     driver.get("https://learn.letskodeit.com/p/practice")
     driver.maximize_window()

     #def find_byXpath(self):
     xpathid= driver.find_element_by_xpath("//input[@id='name']")
     xpathid.send_keys("Rahul")
     print("Field is available adn value is entered")



     cssselector=driver.find_element_by_css_selector("#displayed-text")
     cssselector.send_keys("Pawar")
     print("Field is available adn value is entered")

     driver.close()


obj=FindelementbyXpath_Css()

