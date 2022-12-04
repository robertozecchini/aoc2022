import unittest

from sol import sol1
from sol import sol2


class TestSol(unittest.TestCase):
    def setUp(self):
        filename = "day01/test_input"
        with open(filename) as f:
            self.input = f.readlines()
    def test_sol1(self):
        result = sol1(self.input)
        self.assertEqual(result, 24000)
    def test_sol2(self):
        result = sol2(self.input)
        self.assertEqual(result, 45000)

if __name__ == '__main__':
    unittest.main()
