# https://github.com/gracerveragonzalez-ops/lab10-GR-LM
# Partner 1: Grace Rivera Gonzalez
# Partner 2: Lucas Michael


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(5, 10), 50)
        self.assertEqual(mul(-5, 10), -50)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(5, 10), 2)
        self.assertAlmostEqual(div(3, 1), 0.3333333)
        self.assertEqual(div(-2, 10), -5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 5), 5)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()