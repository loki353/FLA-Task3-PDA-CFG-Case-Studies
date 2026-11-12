from functools import lru_cache

IF_ELSE_GRAMMAR = {
    "S": ("M", "U"),
    "M": ("iMeM", "a"),
    "U": ("iS", "iMeU"),
}

REQUEST_ACK_GRAMMAR = {
    "S": ("aSbb", "abb"),
}

BALANCED_BINARY_GRAMMAR = {
    "S": ("1X0S", "0Y1S", ""),
    "X": ("1X0X", ""),
    "Y": ("0Y1Y", ""),
}

def cfg_accepts(text, grammar):
    nonterminals = set(grammar)

    @lru_cache(maxsize=None)
    def parse_symbol(symbol, position):
        if symbol not in nonterminals:
            return {position + 1} if position < len(text) and text[position] == symbol else set()

        results = set()
        for production in grammar[symbol]:
            positions = {position}
            for part in production:
                next_positions = set()
                for current in positions:
                    next_positions.update(parse_symbol(part, current))
                positions = next_positions
                if not positions:
                    break
            results.update(positions)
        return results

    return len(text) in parse_symbol("S", 0)

def if_else_pda(text):
    return cfg_accepts(text, IF_ELSE_GRAMMAR)

def request_ack_pda(text):
    stack = ["Z"]
    phase = "a"
    count_a = 0

    for symbol in text:
        if symbol == "a":
            if phase != "a":
                return False
            stack.extend(["A", "A"])
            count_a += 1
        elif symbol == "b":
            phase = "b"
            if len(stack) == 1 or stack[-1] != "A":
                return False
            stack.pop()
        else:
            return False

    return count_a >= 1 and len(stack) == 1 and phase == "b"

def balanced_binary_pda(text):
    stack = ["Z"]

    for symbol in text:
        if symbol == "0":
            if stack[-1] == "1":
                stack.pop()
            else:
                stack.append("0")
        elif symbol == "1":
            if stack[-1] == "0":
                stack.pop()
            else:
                stack.append("1")
        else:
            return False

    return len(stack) == 1

def display_results(title, inputs, pda_function, cfg_function):
    print("\\n" + "=" * 76)
    print(title)
    print("=" * 76)
    print(f"{'INPUT':<22}{'EXPECTED RESULT':<22}{'PDA RESULT':<16}{'CFG RESULT'}")
    print("-" * 76)

    for value, expected in inputs:
        pda_result = pda_function(value)
        cfg_result = cfg_function(value)
        expected_text = "ACCEPTED" if expected else "REJECTED"
        pda_text = "ACCEPTED" if pda_result else "REJECTED"
        cfg_text = "ACCEPTED" if cfg_result else "REJECTED"
        print(f"{value or 'ε':<22}{expected_text:<22}{pda_text:<16}{cfg_text}")

def run_all():
    if_else_tests = [
        ("a", True), ("ia", True), ("iaea", True),
        ("iiaea", True), ("iiaeaea", True),
        ("", False), ("i", False), ("iea", False),
        ("ae", False), ("aa", False),
    ]

    request_tests = [
        ("abb", True), ("aabbbb", True), ("aaabbbbbb", True),
        ("aaaabbbbbbbb", True), ("aaaaabbbbbbbbbb", True),
        ("", False), ("ab", False), ("abbb", False),
        ("aabbb", False), ("bba", False),
    ]

    balanced_tests = [
        ("", True), ("10", True), ("01", True),
        ("1100", True), ("0110", True),
        ("1", False), ("110", False), ("0001", False),
        ("10100", False), ("011", False),
    ]

    display_results("CASE STUDY 1: IF-ELSE SYNTAX VALIDATION",
                    if_else_tests, if_else_pda,
                    lambda value: cfg_accepts(value, IF_ELSE_GRAMMAR))
    display_results("CASE STUDY 2: REQUESTS AND ACKNOWLEDGEMENTS",
                    request_tests, request_ack_pda,
                    lambda value: cfg_accepts(value, REQUEST_ACK_GRAMMAR))
    display_results("CASE STUDY 3: BALANCED BINARY STRINGS",
                    balanced_tests, balanced_binary_pda,
                    lambda value: cfg_accepts(value, BALANCED_BINARY_GRAMMAR))
    print("\\n" + "*" * 76)
    print("ALL PDA AND CFG TESTS COMPLETED")
    print("*" * 76)

if __name__ == "__main__":
    run_all()
