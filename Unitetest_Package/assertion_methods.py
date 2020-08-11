import unittest

class assertTrueandFalse(unittest.TestCase):

    def test_assertTrueFalse(self):

        a=True

        self.assertTrue(a, 'a is not fales')

        b=False
        self.assertFalse(b, 'b is not true')

    def test_assertEquals(self):

        a='Test'
        b='Test'

        self.assertEqual(a,b, msg='A is Equal to B')


if __name__=='__main__':
    unittest.main(verbosity=2)