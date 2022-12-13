import unittest
from prod.model.entity import *


class TestProduct(unittest.TestCase):
    def test_setter_positive(self):
        product = Product()
        product.price = 10

        expected = 10

        actual = product.price

        self.assertEqual(expected, actual)

    def test_setter_without_price(self):
        product = Product()

        expected = 0

        actual = product.price

        self.assertEqual(expected, actual)

    def test_setter_negative(self):
        product = Product()

        self.assertRaises(ValueError, product.set_price, 10)


if __name__ == "__main__":
    unittest.main()
