from pathlib import Path
out = Path(__file__).resolve().parents[1] / 'docs' / 'diagrams'
out.mkdir(parents=True, exist_ok=True)
dot = '''digraph BRACKET_PDA {
 rankdir=LR; node [shape=circle]; start [shape=point]; start -> q0;
 q0 -> q0 [label="(, [, { : push"];
 q0 -> q0 [label=") , ] , } : match and pop"];
 q0 [shape=doublecircle, label="q0\nempty stack at end"];
}'''
(out / 'bracket_pda.dot').write_text(dot, encoding='utf-8')
print('Wrote docs/diagrams/bracket_pda.dot')
