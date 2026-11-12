# Task 3 — Grammar and PDA Notes

## Case Study 1: If-Else Syntax
The grammar uses:
- S → M | U
- M → iMeM | a
- U → iS | iMeU

Here, `i` represents an if statement, `e` represents else, and `a` represents an action. Matched and unmatched productions handle nested if-else structures.

## Case Study 2: Requests and Acknowledgements
The language is **L = { aⁿb²ⁿ : n ≥ 1 }**.
- S → aSbb | abb

For every input `a`, the PDA pushes two stack markers. For every `b`, it pops one marker. It accepts when the input has at least one `a`, all `a` symbols precede the `b` symbols, and the stack returns to its base marker.

## Case Study 3: Balanced Binary Strings
The language contains strings over {0,1} with equal counts of both symbols.
- S → 1X0S | 0Y1S | ε
- X → 1X0X | ε
- Y → 0Y1Y | ε

The PDA cancels an unmatched 0 when it reads a 1, or an unmatched 1 when it reads a 0. Otherwise, it stores the current symbol. It accepts when only the bottom-of-stack marker remains.

## PDA and CFG
A CFG describes how strings in a context-free language can be generated. A PDA recognizes such languages by using a stack to remember information that a finite automaton cannot store.
