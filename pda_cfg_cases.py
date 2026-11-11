"""Task 3: PDA/CFG case-study recognizers."""

def balanced_parentheses(text: str) -> bool:
    """PDA-style stack check for one bracket type."""
    stack = []
    for symbol in text:
        if symbol == "(":
            stack.append("(")
        elif symbol == ")":
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return not stack

class ExpressionParser:
    """Recursive-descent parser for E -> T ((+|-) T)*,
       T -> F ((*|/) F)*, F -> id | number | (E)."""
    def __init__(self, source: str):
        self.tokens = self._tokenize(source)
        self.pos = 0

    @staticmethod
    def _tokenize(source):
        import re
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[()+*/-]", source)
        compact = re.sub(r"\s+", "", source)
        if "".join(tokens) != compact:
            raise ValueError("Invalid character in expression")
        return tokens

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def take(self, expected=None):
        token = self.peek()
        if token is None or (expected is not None and token != expected):
            raise ValueError("Unexpected token")
        self.pos += 1
        return token

    def factor(self):
        token = self.peek()
        if token == "(":
            self.take("(")
            self.expression()
            self.take(")")
        elif token and (token[0].isalpha() or token[0] == "_" or token[0].isdigit()):
            self.take()
        else:
            raise ValueError("Expected identifier, number, or '('")

    def term(self):
        self.factor()
        while self.peek() in ("*", "/"):
            self.take()
            self.factor()

    def expression(self):
        self.term()
        while self.peek() in ("+", "-"):
            self.take()
            self.term()

    def accepts(self):
        try:
            if not self.tokens:
                return False
            self.expression()
            return self.peek() is None
        except ValueError:
            return False

def valid_even_palindrome(text: str) -> bool:
    """Recognize even-length palindromes over alphabet {a,b}."""
    return all(ch in "ab" for ch in text) and text == text[::-1] and len(text) % 2 == 0

if __name__ == "__main__":
    print("(()):", "ACCEPTED" if balanced_parentheses("(())") else "REJECTED")
    print("a+b*c:", "ACCEPTED" if ExpressionParser("a+b*c").accepts() else "REJECTED")
    print("abba:", "ACCEPTED" if valid_even_palindrome("abba") else "REJECTED")
