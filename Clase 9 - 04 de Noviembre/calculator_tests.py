import unittest
from CalculatorClass import Calculator

class TestSimpleCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculator = Calculator()
        print("Hola soy setUpClass")

    def setUp(self):
        print("Hola soy setUp")

    def test_add_two_integers(self):
        self.assertEqual(2,2)

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 3), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(2, 0)


if __name__ == '__main__':
    unittest.main()