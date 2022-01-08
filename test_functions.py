from unittest import TestCase
from functions import divide

class TestFunctions(TestCase):
    def test_divide_result(self):
        divident = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(divident, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        divident = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(divident,divisor), expected_result, delta=0.0001)

    def test_divide_zero(self):
        divident = 0
        divisor = 5
        expected_result = 0
        self.assertAlmostEqual(divide(divident,divisor), expected_result)