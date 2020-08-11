from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():
    driver = webdriver.Chrome(
        executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
    driver.get("https://learn.letskodeit.com/p/practice")
    driver.maximize_window()
    driver.find_element(By.ID, "bmwcheck").click()
    print("By . ID is available ")

    driver.find_element(By.XPATH,"//input[@id='benzradio']").click()
    print("By.Xpath is available")


obj=ByDemo()