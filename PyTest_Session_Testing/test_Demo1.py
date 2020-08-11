import pytest

def test_demo3():
    print ("This is first method Demo1")
def test_demo4():
    print("This is Second method demo2")

def test_demo5():
    a = 10
    b = 12

    assert a==b, "A and b is same"

def test_demo6():
    assert True

@pytest.mark.home
def test_demo7():
    assert False
@pytest.mark.home
def test_case_demo8():
    a = "rahul"
    assert a == 'Rahul'

@pytest.mark.home
def test_demo_login_Gmail():
    print("Thsi is Gmail login ")

