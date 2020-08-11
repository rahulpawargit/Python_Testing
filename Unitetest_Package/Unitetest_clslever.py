import unittest

class test_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*" * 30)
        print("I will be exeucted only one time before all tests")

    def setUp(self):
        print("I will be executed before every test method")
    def test_case_Method1(self):
        print("This is first testcase mehtod_1")
    def test_case_Method2(self):
        print("This is secods  test case mehotd")
    def tearDown(self):
        print("This will execute after every test method**********")

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("I will be executed only one time after all tests")

if __name__=='__main__':
    unittest.TestCase
