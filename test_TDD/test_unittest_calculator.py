from calculator import SimpleCalculator
import unittest


class CalculatorTests(unittest.TestCase):
    calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        self.assertEqual(self.calc.add(-5, -20), -25)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(7, 2), 5)
        self.assertEqual(self.calc.subtract(-2, -5), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(7, 2), 14)
        self.assertEqual(self.calc.multiply(-2, -5), 10)

    def test_divide(self):
        self.assertEqual(self.calc.divide(14, 2), 7)
        self.assertEqual(self.calc.divide(-10, -2), 5)

import math

class SciCalculator(SimpleCalculator):
    def find_sqrt(self, int1):
        return math.sqrt(int1)

    def find_ceil(self, int1):
        return math.ceil(int1)


# unittest is the core way of testing within python

#pytest is better use in terminal - pytest -v


