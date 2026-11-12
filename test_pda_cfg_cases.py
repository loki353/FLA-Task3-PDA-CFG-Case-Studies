import unittest

from pda_cfg_cases import (
    IF_ELSE_GRAMMAR,
    REQUEST_ACK_GRAMMAR,
    BALANCED_BINARY_GRAMMAR,
    balanced_binary_pda,
    cfg_accepts,
    if_else_pda,
    request_ack_pda,
)

class PDACFGTests(unittest.TestCase):
    def test_if_else_language(self):
        for value in ["a", "ia", "iaea", "iiaea"]:
            self.assertTrue(if_else_pda(value), value)
            self.assertTrue(cfg_accepts(value, IF_ELSE_GRAMMAR), value)
        for value in ["", "i", "iea", "ae", "aa"]:
            self.assertFalse(if_else_pda(value), value)

    def test_request_ack_language(self):
        for value in ["abb", "aabbbb", "aaabbbbbb", "aaaabbbbbbbb"]:
            self.assertTrue(request_ack_pda(value), value)
            self.assertTrue(cfg_accepts(value, REQUEST_ACK_GRAMMAR), value)
        for value in ["", "ab", "abbb", "aabbb", "bba"]:
            self.assertFalse(request_ack_pda(value), value)

    def test_balanced_binary_language(self):
        for value in ["", "10", "01", "1100", "0110"]:
            self.assertTrue(balanced_binary_pda(value), value)
            self.assertTrue(cfg_accepts(value, BALANCED_BINARY_GRAMMAR), value)
        for value in ["1", "110", "0001", "10100", "011"]:
            self.assertFalse(balanced_binary_pda(value), value)

if __name__ == "__main__":
    unittest.main()
