import  pytest

# class Test_Class():

@pytest.yield_fixture()
def setUp():
        print("Yeild method exected before every method")

        print("Yield mehtod executed after every mehtod")
        yield

def test_method_a(setUp):
        print("This is method of A")

def test_methoc_b(setUp):
        print("This is method of B")


