"""Small helpers for displaying CFG productions and derivations."""

BRACKET_GRAMMAR = {'S': ('SS', '(S)', '[S]', '{S}', '()', '[]', '{}')}
AMBIGUOUS_EXPR_GRAMMAR = {'E': ('E+E', 'E*E', '(E)', 'id')}
PRECEDENCE_GRAMMAR = {'E': ('E+T', 'T'), 'T': ('T*F', 'F'), 'F': ('(E)', 'id')}
PALINDROME_GRAMMAR = {'S': ('aSa', 'bSb', 'a', 'b', '')}

def productions(grammar):
    return '\n'.join(f"{nt} -> {' | '.join('ε' if p == '' else p for p in choices)}" for nt, choices in grammar.items())
