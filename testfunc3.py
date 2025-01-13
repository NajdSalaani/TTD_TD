import unittest
from func3 import *  
class TestCalculatrice(unittest.TestCase):

    def test_addition(self):
        result = addition(2, 3)
        self.assertEqual(result, 5)

    def test_soustraction(self):
        result = soustraction(5, 3)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = multiplication(4, 3)
        self.assertEqual(result, 12)

    def test_division(self):
        result = division(6, 2)
        self.assertEqual(result, 3)

    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            division(6, 0)

    def test_puissance(self):
        result = puissance(2, 3)
        self.assertEqual(result, 8)

    def test_puissance_negative_base(self):
        result = puissance(-2, 3)
        self.assertEqual(result, -8)

    def test_puissance_fractionnaire(self):
        result = puissance(-2, 0.5)
        self.assertEqual(result, "Erreur : Impossible de calculer une puissance fractionnaire pour un nombre négatif.")

    def test_modulo(self):
        result = modulo(5, 2)
        self.assertEqual(result, 1)

    def test_modulo_par_zero(self):
        with self.assertRaises(ValueError):
            modulo(5, 0)


if __name__ == '__main__':
    unittest.main()
