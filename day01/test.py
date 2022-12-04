import unittest

from sol import sol1
import os


class TestSol(unittest.TestCase):
    def test_sol1(self):
        """
        Test sol1
        """
        filename = "day01/test_input"
        with open(filename) as f:
            input = f.readlines()
        result = sol1(input)
        self.assertEqual(result, 24000)

if __name__ == '__main__':
    unittest.main()
