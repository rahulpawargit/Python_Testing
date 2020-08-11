from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


driver = None


@pytest.fixture()
def init_drive():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://www.google.com")
    driver.implicitly_wait(10)
    yield
    driver.quit()


# def teardown_module(module):
#     driver.quit()

def test_verifyTitle(init_drive):
    assert driver.title == "Google1"
    time.sleep(2)

def test_VerifyURL(init_drive):
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
    time.sleep(2)

def test_VerifyURL2(init_drive):
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
    time.sleep(2)

