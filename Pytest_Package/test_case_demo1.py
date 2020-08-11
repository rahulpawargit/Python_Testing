import pytest

@pytest.fixture()
def setup():
    print("This is setup method which will be executed every time whenever we have applied")

def test_method_A(setup):
    print("This is method of A")

def test_metod_B(setup):
    print("This is method B")
