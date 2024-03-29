import unittest
from check_pwd import check_pwd
import string

class TestCase(unittest.TestCase):
    def test1_init_test(self):
        input = '1'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test2_string_length_less_8(self):
        input = '123456'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test3_string_length_greater_than_20(self):
        input = '1234567890123456789012345'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test4_pwd_contains_lowercase_letter(self):
        input = '123456789A'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test5_pwd_contains_uppercase_letter(self):
        input = '123456789a'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test6_pwd_contains_digits_letter(self):
        input = 'AAAAAAAAaaaa'
        expected = False
        self.assertFalse(check_pwd(input), expected)

    def test7_pwd_contains_symbols(self):
        symbols = '~`!@#$%^&*()_+-='
        input = 'AAAAAAAAaaaa1123'
        expected = False
        self.assertFalse(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()

