from selenium import webdriver
from selenium.webdriver.common.by import By

class Listof_Element():

    def list(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.maximize_window()
        listofinpurtstags= driver.find_elements(By.TAG_NAME, "input")
        number=len(listofinpurtstags)
        print("List of Inputs tags availabe", number)

        listoftextboxes=driver.find_elements(By.XPATH, "//input[@type='text']")
        number1=len(listoftextboxes)
        print("List of Textboxes availbe",number1)

ff=Listof_Element()
ff.list()