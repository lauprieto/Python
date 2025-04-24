import unittest
from operaciones import sumar, restar, multiplicar

class TestOperaciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 4), 1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

if __name__ == "__main__":
    unittest.main()
