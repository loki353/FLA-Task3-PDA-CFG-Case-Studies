"""FIRST/FOLLOW demonstration for a small expression grammar."""

FIRST = {'E': {'(', 'id'}, 'T': {'(', 'id'}, 'F': {'(', 'id'}}
FOLLOW = {'E': {')', '$'}, 'T': {'+', ')', '$'}, 'F': {'*', '+', ')', '$'}}

def is_ll1_conflict(f1, f2):
    return bool(set(f1) & set(f2))
