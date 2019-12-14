import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")
    def test_add_second(self):
        self.assertEqual(awesome.frown(), ":(")

if __name__ == '__main__':
    unittest.main()
