from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestBcgLogin(BaseTest):
    @pytest.mark.parametrize(
                      "username, password",
                      [
                        ("admin@gmail.com", "admin123"),
                        ("naveen@gmailcom", "naveen123")
                       ]
                   )
    def test_login(self, username, password):

        """
        This is Parameterrzation
        :param username:
        :type username:
        :param password:
        :type password:
        :return:
        :rtype:
        """

        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)

