# test_calculator.py
import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(8, 0), ValueError)

if __name__ == '__main__':
    unittest.main()
