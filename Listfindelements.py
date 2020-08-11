from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

class Listof_Element():

    def list(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(30)
        driver.maximize_window()

        # //Radio Button#################
        # listofelement=driver.find_elements(By.XPATH, "//input[@name='cars' and @type='radio']")
        # lengthoflele=len(listofelement)
        # print("Lenght of list is " +str(lengthoflele))
        #
        # for radiobutton in listofelement:
        #    is_selected=radiobutton.is_selected()
        #
        #
        #
        #
        #    if not is_selected:
        #        radiobutton.click()
        #        time.sleep(2)

#         Drop Down

        # ele= driver.find_element_by_xpath("//select[@id='carselect']")
        # sel= Select(ele)
        #
        # emw=sel.select_by_visible_text("BMW")
        # print("Selected Value", emw)
        # time.sleep(2)
        #
        # benz=sel.select_by_value("benz")
        # time.sleep(5)
        # print("Selected Value=", benz)
        #
        # honda=sel.select_by_index(2)
        # time.sleep(2)
        # print("selected value=", honda)



# Hideshow element

    #     textboxstate=driver.find_element_by_xpath("//input[@id='displayed-text']").is_displayed()
    #     print("Texbox Visible ?", textboxstate)
    #
    #     driver.find_element_by_xpath("//input[@id='hide-textbox']").click()
    #     textboxstate1 = driver.find_element_by_xpath("//input[@id='displayed-text']").is_displayed()
    #     print("Texbox Visible= ?", textboxstate1)
    #
    #     driver.close()
    #
    #
    # def goibibo(self):
    #     driver = webdriver.Chrome(
    #         executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
    #     driver.get("https://www.goibibo.com/")
    #     driver.maximize_window()
    #     driver.implicitly_wait(30)
    #
    #
    #
    #     driver.find_element_by_xpath("//*[@id='header']/div[1]/ul/li[1]/a/span").click()
    #     # addcitybuttonstate=driver.find_element_by_xpath("//div[@class='dF width100']//span[contains(text(),'Add upto 4 cities')]").is_displayed()
    #     # print("Add cities button is avalabe ?", addcitybuttonstate)
    #     # time.sleep(4)
    #
    #     driver.find_element_by_xpath("//div[@class ='fltSwitchOpt dIF alignItemsCenter ico15'] // span[text()='Multicity']").click()
    #     addcitybuttonstate1 = driver.find_element_by_xpath("//div[@class='dF width100']//span[contains(text(),'Add upto 4 cities')]").is_displayed()
    #     print("Add cities button is avalabe ?", addcitybuttonstate1)
    #     time.sleep(3)


    # Get Text from element

    def getText(self):
        driver = webdriver.Chrome(
            executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\chromedriver.exe")
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(30)
        driver.maximize_window()
        element=driver.find_element_by_xpath("//div[@class='block large-row-spacer']//div[@id='select-class-example']//fieldset[legend]")
        el=element.text
        print(el)



ff=Listof_Element()
# ff.list()
# ff.goibibo()

ff.getText()