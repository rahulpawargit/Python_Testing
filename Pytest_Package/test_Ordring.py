import pytest

# class test_ordring():
@pytest.yield_fixture()
def SetUp():
    print("this is will exeucted befor")
    yield
    print("This will exeucte after")

@pytest.fixture()
def test_methodA(self):
    print("This is Method A")
@pytest.fixture()
def test_methodB(self):
     print("this is Method B")
@pytest.fixture()
def test_MethodC(self):
    print("This is method C")

# obj=test_ordring
# obj.test_methodA()
# obj.test_methodB()
# obj.test_MethodC()
