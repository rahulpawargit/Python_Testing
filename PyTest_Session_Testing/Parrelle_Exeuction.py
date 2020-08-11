from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.google.com')
    driver.implicitly_wait(10)
    assert driver.title == 'Google'


def facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.facebook.com')
    driver.implicitly_wait(10)
    assert driver.title == 'Facebook – log in or sign up'


def Insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(10)
    assert driver.title == 'Instagram'


def Gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://accounts.google.com/')
    driver.implicitly_wait(10)
    assert driver.title == 'Sign in – Google accounts'




