import unittest
import calculation_unittest


class TestClass(unittest.TestCase):

    def test_add(self):
        result = calculation_unittest.add(10, 5)
        # self.assertEqual(result, 15)
        self.assertEqual(calculation_unittest.add(10, 5), 15) # to test: python -m unittest test_calculation.py
        self.assertEqual(calculation_unittest.add(-2, 2), 0)
        self.assertEqual(calculation_unittest.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculation_unittest.subtract(10, 5), 5)
        self.assertEqual(calculation_unittest.subtract(-2, 2), -4)
        self.assertEqual(calculation_unittest.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculation_unittest.multiply(10, 5), 50)  # to test: python -m unittest test_calculation.py
        self.assertEqual(calculation_unittest.multiply(-2, 2), -4)
        self.assertEqual(calculation_unittest.multiply(5, 2), 10)

    def test_divide(self):
        self.assertEqual(calculation_unittest.divide(10, 5), 2)  # to test: python -m unittest test_calculation.py
        self.assertEqual(calculation_unittest.divide(10, 5), 2)  # to test: python -m unittest test_calculation.py
        self.assertEqual(calculation_unittest.divide(-2, 2), -1)
        self.assertEqual(calculation_unittest.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calculation.divide, 10, 0)
        with self.assertRaises(ValueError):
            calculation_unittest.divide(10, 0)


# to test with this command :python  test_calculation.py
if __name__ == '__main__':
    unittest.main()

