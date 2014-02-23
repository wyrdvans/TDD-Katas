from fizzbuzz import fizzbuzz
import unittest

class FizzBuzzTests(unittest.TestCase):

    def test_returns_list(self):
        self.assertIsInstance(fizzbuzz(), list)

    def test_returns_100_values(self):
        self.assertEqual(len(fizzbuzz()),100)

    def test_list_values_are_strings(self):
        for value in fizzbuzz():
            self.assertIsInstance(value, str)

    def test_multiples_of_three(self):
        values = [3, 6, 9]
        self.assertEqual(fizzbuzz(values), ["fizz", "fizz", "fizz"])

    def test_multiples_of_five(self):
        values = [5, 10, 20]
        self.assertEqual(fizzbuzz(values), ["buzz", "buzz", "buzz"])

    def test_multiples_of_three_and_five(self):
        values = [15, 30, 60]
        self.assertEqual(fizzbuzz(values), ["fizzbuzz", "fizzbuzz", "fizzbuzz"])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
