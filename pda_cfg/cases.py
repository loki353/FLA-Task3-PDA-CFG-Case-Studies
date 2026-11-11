from .pda import balanced_brackets, palindrome
from .grammar import BRACKET_GRAMMAR, AMBIGUOUS_EXPR_GRAMMAR, PRECEDENCE_GRAMMAR, PALINDROME_GRAMMAR, productions

def run_all():
    return {
      'brackets': {'accepted': ['()', '([])', '{[()]}'], 'rejected': ['(]', '(()', '())'], 'grammar': productions(BRACKET_GRAMMAR)},
      'expressions': {'ambiguous_grammar': productions(AMBIGUOUS_EXPR_GRAMMAR), 'precedence_grammar': productions(PRECEDENCE_GRAMMAR)},
      'palindromes': {'accepted': ['','a','abba','baab'], 'rejected': ['ab','aab'], 'grammar': productions(PALINDROME_GRAMMAR)}
    }

def check_brackets(value): return balanced_brackets(value)
def check_palindrome(value): return palindrome(value)
