try:
    import unittest
    from app import fibonacci, factorial

except Exception as e:
    print("Some modules are missing {}".format(e))


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 1346269)


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_10(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
