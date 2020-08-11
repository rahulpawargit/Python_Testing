from selenium import webdriver

class IEDriver():
    def open_IE_Browser(self):
        driver=webdriver.Ie(executable_path="E:\\Rahul\\Testing Docs\\Python\\Udemy_SeleniumTutorial\\BrowserDriver\\IEDriverServer.exe")
        driver.get("http://www.google.com")
        driver.close()


obj=IEDriver()
obj.open_IE_Browser()