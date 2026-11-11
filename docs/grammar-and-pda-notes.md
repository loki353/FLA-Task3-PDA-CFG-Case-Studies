# Grammar and PDA notes

## Balanced brackets
The grammar S → SS | (S) | [S] | {S} | () | [] | {} describes concatenation and nesting. A PDA pushes each opening bracket and pops only the matching opening symbol when it reads a closing bracket. It accepts when the input ends with an empty stack.

## Arithmetic expressions
The grammar E → E+E | E*E | (E) | id is ambiguous: an expression such as id+id*id can have different parse structures. The precedence grammar E → E+T | T; T → T*F | F; F → (E) | id gives multiplication higher precedence than addition.

## Palindromes
S → aSa | bSb | a | b | ε generates palindromes over {a,b}. If a separator c is inserted between the two halves, a deterministic PDA can use it to identify the midpoint. Without a marker, a PDA can nondeterministically guess the midpoint.

## PDA versus DFA
The stack stores an unbounded sequence of unmatched opening symbols, which finite-state control alone cannot do.
