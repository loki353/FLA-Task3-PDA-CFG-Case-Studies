# Task 3 – PDA and CFG Case Studies

**Author:** Lokesh Bakkola

## Overview
This project demonstrates:
- Stack-based recognition of balanced parentheses
- Context-free grammar parsing of arithmetic expressions
- Recognition of even-length palindromes over `{a,b}`

## Run
```bash
python pda_cfg_cases.py
```

## Tests
```bash
python -m unittest -v
```

## Files
- `pda_cfg_cases.py` – recognizers and parser
- `test_pda_cfg_cases.py` – unit tests

**Note:** Balanced parentheses uses an explicit stack. The expression recognizer uses recursive descent. The palindrome function checks the language directly; it is not a literal nondeterministic PDA simulator.
