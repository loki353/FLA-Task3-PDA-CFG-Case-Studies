import sys
from .cases import run_all, check_brackets, check_palindrome

def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] == 'all':
        for name, details in run_all().items(): print(f'{name}: {details}')
        return 0
    if args[0] == 'brackets' and len(args) == 2:
        print('ACCEPT' if check_brackets(args[1]) else 'REJECT'); return 0
    if args[0] == 'palindrome' and len(args) == 2:
        print('ACCEPT' if check_palindrome(args[1]) else 'REJECT'); return 0
    print('Usage: python -m pda_cfg.cli [all|brackets STRING|palindrome STRING]')
    return 2

if __name__ == '__main__': raise SystemExit(main())
