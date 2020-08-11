import pytest
import time

@pytest.mark.home
def test_demo_login_Outlook():
    currenttime = time.localtime()
    print(currenttime)
    assert True

@pytest.mark.home
def test_demo_login_Outlook1():
    currenttime = time.localtime()
    print(currenttime)
    assert False

@pytest.mark.home
def test_demo_login_Outlook1():
        currenttime = time.localtime()
        print(currenttime)
        assert False
