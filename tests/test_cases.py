import pytest
from pda_cfg.pda import balanced_brackets, palindrome
from pda_cfg.ll1 import FIRST, FOLLOW, is_ll1_conflict

def test_balanced_brackets_accept():
    assert balanced_brackets('')
    assert balanced_brackets('([])')
    assert balanced_brackets('{[()]}')

def test_balanced_brackets_reject():
    assert not balanced_brackets('(]')
    assert not balanced_brackets('(()')
    assert not balanced_brackets('())')

def test_palindrome_language():
    assert palindrome('abba') and palindrome('baab') and palindrome('')
    assert not palindrome('aab')
    assert not palindrome('abc')

def test_expression_first_follow_sets():
    assert FIRST['E'] == {'(', 'id'}
    assert '$' in FOLLOW['E']

def test_conflict_helper():
    assert is_ll1_conflict({'id'}, {'id','('})
    assert not is_ll1_conflict({'a'}, {'b'})
