from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.google.com')
    driver.implicitly_wait(10)
    assert driver.title == 'Google'
    driver.close()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.facebook.com')
    driver.implicitly_wait(10)
    assert driver.title == 'Facebook – log in or sign up'
    driver.close()


def test_Insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/')
    driver.implicitly_wait(10)
    assert driver.title == 'Instagram'
    driver.close()


def test_Gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://accounts.google.com/')
    driver.implicitly_wait(10)
    assert driver.title == 'Sign in – Google accounts'
    driver.close()




