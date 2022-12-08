import unittest

from sol import sol1
from sol import sol2
from sol import get_folder_name
from sol import read_input


class TestSol(unittest.TestCase):
    def setUp(self):
        self.input = read_input(f"{get_folder_name()}/test_input")
        self.expected1 = "CMZ"
        self.expected2 = 0
    def test_sol1(self):
        result = sol1(self.input)
        self.assertEqual(result, self.expected1)
    def test_sol2(self):
        result = sol2(self.input)
        self.assertEqual(result, self.expected2)

if __name__ == '__main__':
    unittest.main()
