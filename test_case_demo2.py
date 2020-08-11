import pytest

@pytest.fixture()
def setup():
    print("This is setup method which will be executed every time whenever we have applied")

def test_method_C(setup):
    print("This is method of C")

def test_metod_D(setup):
    print("This is method D")
