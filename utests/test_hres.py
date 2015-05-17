"""
    Unit test for hres.py

    References:
    [1] http://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
    [2] http://www.openp2p.com/pub/a/python/2004/12/02/tdd_pyunit.html
    [3] http://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start

"""
__author__ = 'maxim.shcherbakov'

import unittest


class TestHRES(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_something2(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
