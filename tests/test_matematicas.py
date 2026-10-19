import unittest

from mathlib import factorial, gcd, is_prime, lcm, square


class SquareTests(unittest.TestCase):
    def test_square_of_positive_integer(self):
        # Para la demo: cambia 16 por 15 y sube el commit para que falle.
        self.assertEqual(square(4), 16)

    def test_square_of_negative_and_decimal_numbers(self):
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(1.5), 2.25)

    def test_square_rejects_non_numeric_values(self):
        with self.assertRaises(TypeError):
            square("4")


class FactorialTests(unittest.TestCase):
    def test_factorial_of_positive_integers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_zero_is_one(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_rejects_negative_integers(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            factorial(3.5)


class IsPrimeTests(unittest.TestCase):
    def test_identifies_prime_integers(self):
        self.assertIs(is_prime(2), True)
        self.assertIs(is_prime(29), True)

    def test_identifies_non_prime_integers(self):
        self.assertIs(is_prime(1), False)
        self.assertIs(is_prime(21), False)

    def test_is_prime_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            is_prime(2.5)


class GcdTests(unittest.TestCase):
    def test_gcd_of_positive_integers(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)

    def test_gcd_normalizes_signs_and_handles_zero(self):
        self.assertEqual(gcd(-24, 18), 6)
        self.assertEqual(gcd(0, 7), 7)

    def test_gcd_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            gcd(4, 2.5)


class LcmTests(unittest.TestCase):
    def test_lcm_of_positive_integers(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(7, 3), 21)

    def test_lcm_normalizes_signs_and_handles_zero(self):
        self.assertEqual(lcm(-3, 7), 21)
        self.assertEqual(lcm(0, 8), 0)

    def test_lcm_rejects_non_integers(self):
        with self.assertRaises(TypeError):
            lcm(4, 2.5)


if __name__ == "__main__":
    unittest.main()
