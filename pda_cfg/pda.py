"""Deterministic stack checkers for bracket strings."""

PAIRS = {')': '(', ']': '[', '}': '{'}
OPEN = set(PAIRS.values())

def balanced_brackets(value):
    stack = []
    for symbol in value:
        if symbol in OPEN:
            stack.append(symbol)
        elif symbol in PAIRS:
            if not stack or stack.pop() != PAIRS[symbol]:
                return False
        else:
            return False
    return not stack

def palindrome(value):
    return value == value[::-1] and set(value) <= {'a', 'b'}
