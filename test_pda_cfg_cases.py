import unittest
from pda_cfg_cases import balanced_parentheses, ExpressionParser, valid_even_palindrome

class CaseStudyTests(unittest.TestCase):
    def test_parentheses(self):
        self.assertTrue(balanced_parentheses("(())()"))
        self.assertTrue(balanced_parentheses(""))
        self.assertFalse(balanced_parentheses("(()"))
        self.assertFalse(balanced_parentheses("())("))

    def test_expression(self):
        self.assertTrue(ExpressionParser("a+b*c").accepts())
        self.assertTrue(ExpressionParser("(a+b)*c").accepts())
        self.assertFalse(ExpressionParser("a+*b").accepts())
        self.assertFalse(ExpressionParser("(a+b").accepts())

    def test_palindrome(self):
        self.assertTrue(valid_even_palindrome("abba"))
        self.assertTrue(valid_even_palindrome("baab"))
        self.assertFalse(valid_even_palindrome("aba"))
        self.assertFalse(valid_even_palindrome("abc"))

if __name__ == "__main__":
    unittest.main()
