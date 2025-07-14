import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fibonacci(0), 0)

    def test_example2(self):
        self.assertEqual(fibonacci(1), 1)

    def test_example3(self):
        self.assertEqual(fibonacci(10), 55)

    def test_large(self):
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_negative(self):
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertEqual(str(context.exception), "Input must be a non-negative integer.")


if __name__ == "__main__":
    unittest.main()