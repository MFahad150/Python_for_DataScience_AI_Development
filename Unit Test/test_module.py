# Unit Test Library (Freamework that have test functionality)
import unittest 

from module import square, doubler

class Testmodule(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)  # test when 2 is given as input the output is 4.

    def test_doubler(self):
        self.assertEqual(doubler(0), 0) # test when 0 is given as input the output is 0.

if __name__ == '__main__':
    unittest.main()