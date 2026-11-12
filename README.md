# Task 3 — PDA and CFG Case Studies

**Course:** Formal Language and Automata (21CSC301T)  
**Student:** Bakkola Lokesh  
**Register Number:** RA2411026050060  
**Department:** CSE AIML  
**Institution:** SRM Institute of Science and Technology, Tiruchirappalli

## Overview
This project implements three language-recognition case studies using Pushdown Automata (PDA) and Context-Free Grammars (CFG).

## Case studies

### 1. If-Else Syntax Validation
Recognizes simplified if-else statement strings using the symbols `i` (if), `e` (else), and `a` (action). The grammar distinguishes matched and unmatched if statements.

### 2. Requests and Acknowledgements
Recognizes the language **L = { aⁿb²ⁿ : n ≥ 1 }**. The PDA pushes two stack symbols for each `a` and pops one for each `b`.

### 3. Balanced Binary Strings
Recognizes binary strings containing equal numbers of `0` and `1`. The PDA uses its stack to cancel an unmatched opposite symbol.

## Project files
- `pda_cfg_cases.py` — CFG parser, PDA recognizers, test data, and output display.
- `test_pda_cfg_cases.py` — Unit tests for all three case studies.
- `tests/test_cases.py` — Test discovery entry point.

## Run the program
```bash
python pda_cfg_cases.py
python -m unittest -v
```

Python 3.9+ is recommended. The implementation uses only the Python standard library.
