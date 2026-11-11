# Task 3 — PDA and CFG Case Studies

**Author:** Lokesh Bakkola

## Overview
This project studies three context-free language examples using context-free grammars (CFGs), pushdown automata (PDAs), derivations, and stack behavior.

## Project structure
```text
pda_cfg/
  __init__.py
  grammar.py
  pda.py
  ll1.py
  cases.py
  cli.py
tests/test_cases.py
docs/diagrams/
tools/make_diagrams.py
```

## Case studies
1. **Balanced brackets:** a CFG generates properly nested (), [] and {}. A PDA uses its stack to remember opening brackets and match each closing bracket.
2. **Arithmetic expressions:** an ambiguous expression grammar is compared with a precedence grammar where multiplication binds more tightly than addition.
3. **Palindromes:** CFG S → aSa | bSb | a | b | ε generates even/odd palindromes over {a,b}. A PDA needs nondeterministic guessing for the midpoint in the unmarked form.

## Run
```bash
python -m pda_cfg.cli all
python -m pda_cfg.cli brackets
python -m pda_cfg.cli palindrome abba
python -m pytest -q
python tools/make_diagrams.py
```

Python 3.9+; core implementation uses only the standard library. Pytest is required for tests. Diagram tool writes Graphviz DOT source.

## Why finite automata are insufficient
Balanced nesting requires remembering an unbounded number of unmatched opening brackets. A finite automaton has only finitely many states and cannot maintain an unbounded stack-like count. A PDA adds a stack, making it suitable for these context-free patterns.
