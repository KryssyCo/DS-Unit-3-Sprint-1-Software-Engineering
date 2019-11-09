'''Sprint Challenge Unit 3 Sprint 1 - Part 5 Measure Twice, Test Once'''

#!/usr/bin/env python
"""Tests for Acme Python modules."""

import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Another day, another anvil')
        self.assertEqual(prod.weight, 20)

    def test_default_boxing_weight(self):
        """Test weight of default boxing gloves"""
        glove = BoxingGlove('Punch Puncher')
        self.assertEqual(glove.weight, 10)

    def test_stealable_and_explode(self):
        """Is a product stealable or explosive...or both?"""
        babomb = Product('Danger!', price=20, weight=20, flammability=2.5)
        self.assertEqual(babomb.stealability(), 'Very stealable!')
        self.assertEqual(babomb.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Running unittest on products."""
    def test_default_num_products(self):
        """Check that Acme makes 30 products by default."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Check that all products have valid names."""
        for product in generate_products():
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
