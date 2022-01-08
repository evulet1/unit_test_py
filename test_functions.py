from unittest import TestCase
from functions import divide

class TestFunctions(TestCase):
    def test_divide_result(self):
        divident = 15
        divisor = 3
        expected_result = 4.0
        self.assertAlmostEqual(divide(divident, divisor), expected_result)